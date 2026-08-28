import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([35, 40, 50, 55, 65, 70, 80, 90])

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Study hours for prediction
study_hours = np.array([[2], [4], [6], [8]])

# Predict student scores
predictions = model.predict(study_hours)

# Display predictions
for hours, score in zip(study_hours, predictions):
    print(f"Study Hours: {hours[0]} -> Predicted Score: {score:.2f}")