import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('weather_prediction_dataset.csv')

cities = set(col.split('_')[0] for col in df.columns if '_' in col)
first_city = cities[0]
print(cities)