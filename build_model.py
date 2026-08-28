import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([35, 40, 50, 55, 65, 70, 80, 90])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Display model details
print("Model trained successfully!")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Prediction
hours = np.array([[6]])
prediction = model.predict(hours)

print("Predicted marks for 6 hours:", prediction[0])