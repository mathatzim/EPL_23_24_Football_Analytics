import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

import xlrd

book = xlrd.open_workbook("EPL Home Away xG xGA 23_24.xls")
sheet = book.sheet_by_name('Sheet2')

X = np.array(sheet.col_values(0)).reshape(-1,1)
Y = np.array(sheet.col_values(1))
                                   
plt.scatter(X, Y, color='blue', label='Data points')                                                                                                                                                                                                                                                                                  ', label='Data points')

model = LinearRegression()

model.fit(X, Y)

Rsquare = model.score(X, Y)
print('Coefficient of determination (R²):', Rsquare)

print('Intercept (𝑏₀):', model.intercept_)
print('Slope (𝑏₁):', model.coef_)

print(f"Equation of the line: Y = {model.intercept_} + {model.coef_[0]} * X")

intercept = model.intercept_
slope = model.coef_[0]

print(f'Intercept (𝑏₀): {intercept:.2f}')
print(f'Slope (𝑏₁): {slope:.2f}')                                         

print(f"Equation of the line: Y = {intercept:.2f} + {slope:.2f} * X")

plt.plot(X, model.predict(X), color='red', label='Regression line')

equation = f"Y = {intercept:.2f} + {slope:.2f} * X"

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Linear Regression Line')

plt.text(0.95, 0.05, equation, fontsize=12, color='black', ha='right', va='bottom', transform=plt.gca().transAxes)

plt.legend()

plt.show()

xNew = np.array([[20]])

yNew_manual = model.intercept_ + model.coef_[0] * xNew

yPred = model.predict(xNew)

print(f"Prediction (Manual calculation): {yNew_manual[0][0]:.2f}")
print(f"Prediction (Using model.predict): {yPred[0]:.2f}")