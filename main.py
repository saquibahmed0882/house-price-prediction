import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score



data = pd.read_csv("dataset/kc_house_data.csv")



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



y = data['price']



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



model = RandomForestRegressor(
    n_estimators=50,
    random_state=42,
    n_jobs=-1
)


model.fit(X_train, y_train)



prediction = model.predict(X_test)



print("Mean Absolute Error:", mean_absolute_error(y_test, prediction))
print("R2 Score:", r2_score(y_test, prediction))



import joblib

joblib.dump(model, "house_price_model.pkl", compress=3)

print("Model saved successfully!")