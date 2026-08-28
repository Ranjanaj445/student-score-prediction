import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([35, 40, 50, 55, 65, 70, 80, 90])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Get input from user
hours = float(input("Enter your study hours: "))

# Predict score
prediction = model.predict([[hours]])

# Display result
print("Predicted Score:", round(prediction[0], 2))