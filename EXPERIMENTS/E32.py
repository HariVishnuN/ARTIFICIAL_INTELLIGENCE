import numpy as np
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
x_mean = np.mean(X)
y_mean = np.mean(y)
numerator = np.sum((X - x_mean) * (y - y_mean))
denominator = np.sum((X - x_mean) ** 2)
m = numerator / denominator
c = y_mean - (m * x_mean)
print(f"Learned Equation: y = {m:.2f}x + {c:.2f}")
new_x = 6
prediction = m * new_x + c
print(f"Prediction for x={new_x}: {prediction:.2f}")