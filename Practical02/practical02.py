import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Define Data
n = int(input("Enter number of data points: "))
x = []
y = []

print("\nEnter x and y values:")

for i in range(n):
    xi = float(input(f"Enter x[{i+1}]: "))
    yi = float(input(f"Enter y[{i+1}]: "))
    x.append(xi)
    y.append(yi)

x = np.array(x)
y = np.array(y)

# Step 2: Least Squares Regression
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x * x)

a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - (sum_x ** 2))
b = (sum_y - a * sum_x) / n

print("\nSlope (a) =", a)
print("Intercept (b) =", b)
print(f"Regression Equation: y = {a:.4f}x + {b:.4f}")

# Step 3: Predicted Values
y_pred = a * x + b

print("\nPredicted Values:")

for i in range(n):
    print(f"x = {x[i]:.2f}, Actual y = {y[i]:.2f}, Predicted y = {y_pred[i]:.4f}")

# Step 4: Evaluation Metrics
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

print("\nEvaluation Metrics")
print("----------------------")
print("MAE =", mae)
print("MSE =", mse)
print("RMSE =", rmse)
print("R2 Score =", r2)

# Step 5: Plot Regression Line
plt.figure(figsize=(8, 6))

plt.scatter(x, y, color='blue', s=80, label='Actual Data')
plt.plot(x, y_pred, color='red', linewidth=2, label='Regression Line')

# Axis labels
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Least Squares Linear Regression")

# Integer ticks
plt.xticks(range(int(min(x))-1, int(max(x))+2))
plt.yticks(range(int(min(y))-1, int(max(y))+2))

# Axes through origin
plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=0, color='black', linewidth=1)

plt.grid(True)
plt.legend()
plt.show()

# Step 6: Plot Evaluation Metrics
metrics = ["MAE", "MSE", "RMSE"]
values = [mae, mse, rmse]

plt.figure(figsize=(6, 4))
plt.bar(metrics, values, color=["green", "orange", "purple"])

plt.title("Evaluation Metrics")
plt.xlabel("Metrics")
plt.ylabel("Value")
plt.grid(axis='y')
plt.show()
