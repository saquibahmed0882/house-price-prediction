import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# Load dataset
data = pd.read_csv("dataset/kc_house_data.csv")


# Features
X = data[['bedrooms',
          'bathrooms',
          'sqft_living',
          'sqft_lot',
          'floors',
          'waterfront',
          'view',
          'condition',
          'grade',
          'sqft_above',
          'sqft_basement',
          'yr_built',
          'yr_renovated']]


# Target
y = data['price']


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Create Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# Train Model  ✅ ye line yahi hai
model.fit(X_train, y_train)


# Prediction
prediction = model.predict(X_test)


# Accuracy
print("Mean Absolute Error:", mean_absolute_error(y_test, prediction))
print("R2 Score:", r2_score(y_test, prediction))


# Save Model
with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")