import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.DataFrame({
    'N': [90, 40, 60, 30],
    'P': [42, 50, 35, 20],
    'K': [43, 60, 40, 25],
    'temperature': [20, 30, 25, 35],
    'humidity': [80, 60, 70, 50],
    'ph': [6.5, 7.0, 6.8, 5.5],
    'rainfall': [200, 150, 180, 100],
    'crop': ['rice', 'wheat', 'maize', 'millet']
})

X = data.drop('crop', axis=1)
y = data['crop']

model = RandomForestClassifier()
model.fit(X, y)

def predict_crop(features):
    return model.predict([features])[0]