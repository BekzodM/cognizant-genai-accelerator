import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

#Reading a dataset downloaded from https://www.kaggle.com/datasets/thedevastator/weather-prediction/data
df = pd.read_csv('weather_prediction_dataset.csv')

#Creating a weather class to determine whether it is sunny or cloudy based on cloud cover in Ljublana, Slovenia
df['Weather_Class'] = df['LJUBLJANA_cloud_cover'].apply(lambda x: 1 if x >= 4 else 0)
print(df['Weather_Class'].value_counts())

#features used to train and test our ML model
features = ['LJUBLJANA_humidity', 'LJUBLJANA_pressure', 'LJUBLJANA_wind_speed',
            'LJUBLJANA_global_radiation', 'LJUBLJANA_precipitation',
            'LJUBLJANA_temp_mean', 'LJUBLJANA_temp_min', 'LJUBLJANA_temp_max']

target = 'Weather_Class'

X = df[features]
y = df[target]

#if we are missing any data
df.fillna(df.mean(numeric_only=True), inplace=True)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#Setting train test split of 80/20
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=17, stratify=y)


# Train Decision Tree Regressor
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#Printing accuracy and report
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))


