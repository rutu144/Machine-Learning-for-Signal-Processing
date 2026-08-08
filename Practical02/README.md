# Practical 02: Least Squares Linear Regression

## Aim

To implement Least Squares Linear Regression for modeling the relationship between input and output data, predict values using the obtained regression equation, and evaluate the performance of the model using different evaluation metrics.

---

## Theory

### Least Squares Linear Regression

Linear Regression is a supervised machine learning technique used to model the relationship between an independent variable (X) and a dependent variable (Y).

In simple linear regression, the relationship between X and Y is represented by:

y = ax + b

where:

- `x` = input or independent variable
- `y` = predicted output or dependent variable
- `a` = slope of the regression line
- `b` = intercept of the regression line

The Least Squares method determines the best-fitting straight line by minimizing the sum of squared differences between the actual values and predicted values.

The slope is calculated as:

a = [nΣxy - (Σx)(Σy)] / [nΣx² - (Σx)²]

The intercept is calculated as:

b = [Σy - aΣx] / n

The final regression equation is:

y = ax + b

The obtained regression equation can then be used to predict the output for given input values.

---

## Objective

The objectives of this practical are:

1. To understand the concept of Least Squares Linear Regression.
2. To accept input X and Y values from the user.
3. To calculate the slope and intercept.
4. To obtain the regression equation.
5. To calculate predicted values.
6. To visualize the actual data and regression line.
7. To calculate model evaluation metrics.
8. To understand the performance of the regression model.

---

## Tools and Technologies Used

- Python 3
- NumPy
- Matplotlib
- Scikit-learn
- VS Code / IDLE / Python IDE
- GitHub

---

## Requirements

The Python libraries required for this practical are listed in `requirements.txt`.

Install them using:

```bash
pip install -r requirements.txt
