# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:55:05 2024

@author: mathaios
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")
sheet = book.sheet_by_name('Sheet3')
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
plt.figure(figsize=(12, 6), facecolor='beige')
plt.gca().set_facecolor('beige')
plt.scatter(X, Y, color='red',label=' Teams', s=10)

correlation_matrix = np.corrcoef(X.flatten(), Y)  
correlation_coefficient = correlation_matrix[0, 1]

print(f"Correlation coefficient: {correlation_coefficient:.4f}")

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

plt.plot(X, model.predict(X), color='Green', label='Regression line')

equation = f"Y = {intercept:.2f} + {slope:.2f} * X"

plt.xlabel(' Total Goal Difference')
plt.ylabel(' Total Points')
plt.title('Relantionship Between Points and Goal Difference')
for i in range(len(X)):
    img = mpimg.imread(image_paths[i])  
    imagebox = OffsetImage(img, zoom=0.5)  
    ab = AnnotationBbox(imagebox, (X[i], Y[i]), frameon=False, xycoords='data', boxcoords="data")
    plt.gca().add_artist(ab) 

Logo_image_path = 'images/PL_Logo.png'  
Logo_img = mpimg.imread(Logo_image_path)
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)

ab_Logo = AnnotationBbox(Logo_imagebox, (0.05, 0.77), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)

plt.text(0.95, 0.05, equation, fontsize=12, color='black', ha='right', va='bottom', transform=plt.gca().transAxes)
plt.legend()

plt.show()

xNew = np.array([[20]])

yNew_manual = model.intercept_ + model.coef_[0] * xNew

yPred = model.predict(xNew)

print(f"Prediction (Manual calculation): {yNew_manual[0][0]:.2f}")
print(f"Prediction (Using model.predict): {yPred[0]:.2f}")