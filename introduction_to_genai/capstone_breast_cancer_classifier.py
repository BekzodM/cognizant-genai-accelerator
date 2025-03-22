import tensorflow as tf
import numpy as np

from matplotlib import pyplot as plt

gpus = tf.config.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.set_logical_device_configuration(
    gpu,
    [tf.config.LogicalDeviceConfiguration(memory_limit=1024)]  # Limit to 1024MB (1GB)
    )

#Create directory data, and import training data from kaggle https://www.kaggle.com/datasets/gauravduttakiit/mammography-breast-cancer-detection/data
data = tf.keras.utils.image_dataset_from_directory('data', image_size=(256, 256), batch_size=32)
data = data.map(lambda x, y: (x/255.0, y))  # Normalize pixel values

data = data.cache().shuffle(1000).prefetch(tf.data.AUTOTUNE)

""" # Show images from index 2 to 6
for idx, img in enumerate(batch[0][2:6]):
    ax[idx].imshow(img)
    
    # Use `idx+2` to get the correct label from batch[1]
    ax[idx].title.set_text(f"Label: {batch[1][idx+2]}")

plt.show() """
data_size = data.cardinality().numpy()
train_size = int(data_size*0.7)
val_size = int(data_size*0.2)
test_size = int(data_size*0.1)

train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size+val_size).take(test_size)
print(len(test))

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout

model = Sequential()

model.add(Conv2D(16, (3,3), 1, activation='relu', input_shape=(256,256,3)))
model.add(MaxPooling2D())

model.add(Conv2D(32, (3,3), 1, activation='relu'))
model.add(MaxPooling2D())

model.add(Conv2D(16, (3,3), 1, activation='relu'))
model.add(MaxPooling2D())

model.add(Flatten())

model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss=tf.losses.BinaryCrossentropy(),
    metrics=['accuracy']
)
print(model.summary())

logdir = 'logs'
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)
hist = model.fit(train, epochs=20, validation_data=val, callbacks=[tensorboard_callback])

from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
pre = Precision()
re = Recall()
acc = BinaryAccuracy()

for batch in test.as_numpy_iterator():
    X, y = batch
    yhat = model.predict(X)
    pre.update_state(y, yhat)
    re.update_state(y, yhat)
    acc.update_state(y, yhat)
print(f'Precision:{pre.result().numpy()}, Recall:{re.result().numpy()}, Accuracy:{acc.result().numpy()}')

import cv2

#img = cv2.imread('13475_50358702.png') # M
#resize = tf.image.resize(img, (256,256))


#yhat = model.predict(np.expand_dims(resize/255.0, axis=0))
#print(yhat)