import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("dataset.csv")

X = data.drop("label", axis=1)
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

def predict_crop(temp, humidity, ph, rainfall, N, P, K):
    input_data = [[N, P, K, temp, humidity, ph, rainfall]]
    return model.predict(input_data)[0]
