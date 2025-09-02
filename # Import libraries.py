# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

# 1. Load dataset
df = pd.read_csv('weatherHistory.csv')

# 2. Check the head and shape
print("Initial Shape:", df.shape)
print(df.head())

# 3. Preprocess
# Drop rows with nulls (if any)
df = df.dropna()

# Define features and target
X = df[['Humidity', 'Wind Speed (km/h)', 'Wind Bearing (degrees)', 'Visibility (km)', 'Pressure (millibars)']]
y = df['Apparent Temperature (C)']

# Optional: normalize features (helpful for SVR)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 5. Train models
models = {
    'Linear Regression': LinearRegression(),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'SVM': SVR()
}

rmse_scores = {}
predictions = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    predictions[name] = y_pred
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    rmse_scores[name] = rmse
    print(f"{name} RMSE: {rmse:.4f}")

# 6. Plot actual vs predicted
plt.figure(figsize=(20, 12))
for i, (name, y_pred) in enumerate(predictions.items(), 1):
    plt.subplot(2, 2, i)
    sns.scatterplot(x=y_test, y=y_pred, alpha=0.4)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel('Actual Temperature (C)')
    plt.ylabel('Predicted Temperature (C)')
    plt.title(f'{name} - Actual vs Predicted')

plt.tight_layout()
plt.show()

# 7. Print summary
print("\n--- RMSE Summary ---")
for name, rmse in rmse_scores.items():
    print(f"{name}: {rmse:.4f}")
