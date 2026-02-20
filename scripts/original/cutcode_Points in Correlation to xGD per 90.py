# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:02:34 2024

@author: mathaios
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

import xlrd

book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")
sheet = book.sheet_by_name('Sheet4')

X = np.array(sheet.col_values(0)).reshape(-1,1)
Y = np.array(sheet.col_values(1))

image_paths = [
    'images/Manchester City.png',
    'images/Arsenal.png',
    'images/Liverpool.png',
    'images/Aston Villa.png',
    'images/Tottenham.png',
    'images/Chelsea.png',
    'images/Newcastle Utd.png',
    'images/Manchester Utd.png',
    'images/West Ham.png',
    'images/Crystal Palace.png',
    'images/Bournemouth.png',
    'images/Brighton.png',
    'images/Everton.png',
    'images/Fulham.png',
    'images/Wolves.png',
    'images/Brentford.png',
    'images/Nottingham Forest.png',
    'images/Luton Town.png',
    'images/Burnley.png',
    'images/Sheffield Utd.png']
    

print(X)
print(Y)

if len(X) != len(image_paths):
    raise ValueError(f"Length mismatch: len(X)={len(X)} and len(image_paths)={len(image_paths)}")
plt.figure(figsize=(12, 9), facecolor='lightgray')
plt.gca().set_facecolor('beige')
plt.scatter(X, Y, color='red',label=' Teams', s=50)


model = LinearRegression()

model.fit(X, Y)

Rsquare = model.score(X, Y)
print('Coefficient of determination (R²):', Rsquare)

#Y_pred = model.predict(X)
#residuals = Y - Y_pred
#plt.scatter(X, residuals, color='blue')
#plt.axhline(0, color='black', linestyle='--') 
#plt.xlabel('Expected Goal Difference')
#plt.ylabel('Residuals')
#plt.title('Residuals Plot')
#plt.show()
#mean_residual = np.mean(residuals)
#print("Mean of Residuals:", mean_residual)
#mse = np.mean(residuals**2)
#print("Mean Squared Error (MSE):", mse)

print('Intercept (𝑏₀):', model.intercept_)
print('Slope (𝑏₁):', model.coef_)

print(f"Equation of the line: Y = {model.intercept_} + {model.coef_[0]} * X")

intercept = model.intercept_
slope = model.coef_[0]

print(f'Intercept (𝑏₀): {intercept:.2f}')
print(f'Slope (𝑏₁): {slope:.2f}')                                         

print(f"Equation of the line: Y = {intercept:.2f} + {slope:.2f} * X")

plt.plot(X, model.predict(X), color='Green', label='Regression line')

equation = f"Y = {intercept:.2f} + {slope:.2f} * X"

plt.xlabel(' Total Points')
plt.ylabel(' Expected Goals Difference per 90')
plt.title('Scatter Plot with Linear Regression Line')

for i in range(len(X)):
    img = mpimg.imread(image_paths[i])  
    imagebox = OffsetImage(img, zoom=0.8)  
    ab = AnnotationBbox(imagebox, (X[i], Y[i]), frameon=False, xycoords='data', boxcoords="data")
    plt.gca().add_artist(ab) 

plt.legend()

plt.show()

xNew = np.array([[20]])

yNew_manual = model.intercept_ + model.coef_[0] * xNew

yPred = model.predict(xNew)

print(f"Prediction (Manual calculation): {yNew_manual[0][0]:.2f}")
print(f"Prediction (Using model.predict): {yPred[0]:.2f}")