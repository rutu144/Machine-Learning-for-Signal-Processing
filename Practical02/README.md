# Practical 02: Least Squares Linear Regression

## Aim

To implement Least Squares Linear Regression and evaluate the model using
MAE, MSE, RMSE, and R² score.

## Tools Used

- Python
- NumPy
- Matplotlib
- Scikit-learn

## Theory

Least Squares Linear Regression is a supervised machine learning technique
used to find the best-fit straight line between input and output data.

The regression equation is:

y = ax + b

where:
- a is the slope of the regression line
- b is the intercept
- x is the input value
- y is the predicted output

The least squares method determines the values of slope and intercept by
minimizing the difference between actual and predicted values.

## Algorithm

1. Enter the number of data points.
2. Enter the X and Y values.
3. Calculate the required summations.
4. Calculate the slope and intercept using the Least Squares method.
5. Generate predicted Y values.
6. Calculate MAE, MSE, RMSE, and R² score.
7. Plot the actual data points and regression line.
8. Plot the evaluation metrics.
9. Display the results.

## Methodology

The input X and Y data points are provided by the user. The Least Squares
method is then used to calculate the slope and intercept of the regression
line. Using these values, predicted Y values are calculated.

The model performance is evaluated using Mean Absolute Error (MAE),
Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² score.

Finally, the actual data points and regression line are plotted, followed
by a graph of the evaluation metrics.

## Evaluation Metrics

- MAE – Mean Absolute Error
- MSE – Mean Squared Error
- RMSE – Root Mean Squared Error
- R² Score – Coefficient of Determination

## Files

- `practical02.py` – Python implementation
- `requirements.txt` – Required Python libraries
- `output.png` – Output of the practical
- `README.md` – Practical documentation

## Output

The output displays the calculated slope, intercept, regression equation,
predicted values, evaluation metrics, regression plot, and evaluation
metrics plot.

![Output](output.png)

## Conclusion

Least Squares Linear Regression was successfully implemented. The regression
line was obtained from the given data and the model was evaluated using
MAE, MSE, RMSE, and R² score.
