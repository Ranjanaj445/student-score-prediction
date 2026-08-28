import numpy as np
from sklearn.linear_model import LinearRegression

# Student study hours
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)

# Student scores
y = np.array([35, 40, 50, 55, 65, 70, 80, 90])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

print("Model trained successfully!")

# Predict score for 6 study hours
prediction = model.predict([[6]])

print("Predicted Score:", round(prediction[0], 2))