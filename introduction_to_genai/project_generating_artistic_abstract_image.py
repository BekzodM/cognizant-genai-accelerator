import os
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import UnidentifiedImageError
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten, Reshape, LeakyReLU, Dropout, UpSampling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import array_to_img
from tensorflow.keras.callbacks import Callback

# Load dataset
image_folder = "abstract_art/"
ds = tf.keras.utils.image_dataset_from_directory(
    image_folder,
    image_size=(128, 128),  # Resize images
    batch_size=32,          # Process images in batches
    shuffle=True,
    label_mode=None
)

dataiterator = ds.as_numpy_iterator()

def scale_images(image):
    return image / 255

ds = ds.map(scale_images)
ds = ds.cache()
ds = ds.shuffle(60000)
ds = ds.prefetch(16)
print(ds.as_numpy_iterator().next().shape)

def build_generator():
    model = Sequential()

    model.add(Dense(7*7*128, input_dim=128))
    model.add(LeakyReLU(0.2))
    model.add(Reshape((7,7,128)))

    model.add(UpSampling2D())
    model.add(Conv2D(128, 5, padding='same'))
    model.add(LeakyReLU(0.2))

    model.add(UpSampling2D())
    model.add(Conv2D(128, 5, padding='same'))
    model.add(LeakyReLU(0.2))

    model.add(Conv2D(128, 4, padding='same'))
    model.add(LeakyReLU(0.2))

    model.add(Conv2D(128, 4, padding='same'))
    model.add(LeakyReLU(0.2))

    model.add(UpSampling2D())  # 28x28 -> 56x56
    model.add(Conv2D(128, 5, padding='same'))
    model.add(LeakyReLU(0.2))

    model.add(UpSampling2D())  # 56x56 -> 112x112
    model.add(Conv2D(64, 5, padding='same'))
    model.add(LeakyReLU(0.2))

    model.add(UpSampling2D())  # 112x112 -> 224x224
    model.add(Conv2D(32, 5, padding='same'))
    model.add(LeakyReLU(0.2))

    # Resize down to 128x128
    model.add(Conv2D(3, 5, padding='same', activation='sigmoid'))  # RGB output
    model.add(tf.keras.layers.Resizing(128, 128))  # Downsample final output

    return model

def build_discriminator():
    model = Sequential()

    model.add(Conv2D(32, 5, input_shape = (128, 128, 3)))
    model.add(LeakyReLU(0.2))
    model.add(Dropout(0.4))

    model.add(Conv2D(64, 5))
    model.add(LeakyReLU(0.2))
    model.add(Dropout(0.4))

    model.add(Conv2D(128, 5))
    model.add(LeakyReLU(0.2))
    model.add(Dropout(0.4))

    model.add(Conv2D(256, 5))
    model.add(LeakyReLU(0.2))
    model.add(Dropout(0.4))

    model.add(Flatten())
    model.add(Dropout(0.4))
    model.add(Dense(1, activation='sigmoid'))

    return model

generator = build_generator()
discriminator = build_discriminator()

g_opt = Adam(learning_rate=0.0001) 
d_opt = Adam(learning_rate=0.00001) 
g_loss = BinaryCrossentropy()
d_loss = BinaryCrossentropy()

class ArtGAN(Model): 
    def __init__(self, generator, discriminator, latent_dim, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generator = generator 
        self.discriminator = discriminator 
        self.latent_dim = latent_dim  # e.g., 128

    def compile(self, g_opt, d_opt, g_loss, d_loss, *args, **kwargs): 
        super().compile(*args, **kwargs)
        self.g_opt = g_opt
        self.d_opt = d_opt
        self.g_loss = g_loss
        self.d_loss = d_loss 

    def train_step(self, batch):
        real_images = batch  # Unpack tuple
        batch_size = tf.shape(real_images)[0]

        # Generate fake images
        random_latent_vectors = tf.random.normal((batch_size, self.latent_dim))
        fake_images = self.generator(random_latent_vectors, training=True)

        # Combine real and fake images
        combined_images = tf.concat([real_images, fake_images], axis=0)
        labels = tf.concat([
            tf.ones((batch_size, 1)),  # real = 1
            tf.zeros((batch_size, 1))  # fake = 0
        ], axis=0)

        # Add label noise
        labels += 0.05 * tf.random.uniform(tf.shape(labels))

        # Train discriminator
        with tf.GradientTape() as d_tape:
            predictions = self.discriminator(combined_images, training=True)
            d_loss = self.d_loss(labels, predictions)

        d_grads = d_tape.gradient(d_loss, self.discriminator.trainable_variables)
        self.d_opt.apply_gradients(zip(d_grads, self.discriminator.trainable_variables))

        # Train generator
        misleading_labels = tf.ones((batch_size, 1))  # Want generator to "fool" the disc

        with tf.GradientTape() as g_tape:
            fake_latent_vectors = tf.random.normal((batch_size, self.latent_dim))
            generated_images = self.generator(fake_latent_vectors, training=True)
            predictions = self.discriminator(generated_images, training=False)
            g_loss = self.g_loss(misleading_labels, predictions)

        g_grads = g_tape.gradient(g_loss, self.generator.trainable_variables)
        self.g_opt.apply_gradients(zip(g_grads, self.generator.trainable_variables))

        return {"d_loss": d_loss, "g_loss": g_loss}

gan = ArtGAN(generator, discriminator, latent_dim=128)
gan.compile(
    g_opt=Adam(learning_rate=1e-4),
    d_opt=Adam(learning_rate=1e-5),
    g_loss=BinaryCrossentropy(),
    d_loss=BinaryCrossentropy()
)

class ModelMonitor(Callback):
    def __init__(self, num_img=3, latent_dim=128):
        self.num_img = num_img
        self.latent_dim = latent_dim

    def on_epoch_end(self, epoch, logs=None):
        random_latent_vectors = tf.random.normal((self.num_img, self.latent_dim))
        generated_images = self.model.generator(random_latent_vectors)
        generated_images *= 255
        generated_images.numpy()
        for i in range(self.num_img):
            img = array_to_img(generated_images[i])
            img.save(os.path.join('images', f'generated_img_{epoch}_{i}.png'))

hist = gan.fit(ds, epochs=20, callbacks=[ModelMonitor()])