# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:44:48 2025

@author: mathaios
"""

import numpy as np
from sklearn.linear_model import LinearRegression  
import matplotlib.pyplot as plt  
from matplotlib.offsetbox import OffsetImage, AnnotationBbox  
import matplotlib.image as mpimg  
import xlrd  

# Open the Excel workbook and read the data from the specified sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Specify your file path
sheet = book.sheet_by_name('Sheet18')  # Accessing data from 'Sheet18'
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # Extract first column (e.g., Total Goal Difference)
Y = np.array(sheet.col_values(1))  # Extract second column (e.g., Total Points)

# Define the paths for the images of each team
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

# Ensure that the number of teams matches the number of data points
if len(X) != len(image_paths):
    raise ValueError(f"Length mismatch: len(X)={len(X)} and len(image_paths)={len(image_paths)}")

# Create a plot with beige background
plt.figure(figsize=(12, 5.5), facecolor='beige')
plt.gca().set_facecolor('beige')

# Scatter plot to display the relationship between the goal difference (X) and points (Y)
plt.scatter(X, Y, color='red', label=' Teams', s=10)

# Calculate the correlation coefficient to understand the relationship between X and Y
correlation_matrix = np.corrcoef(X.flatten(), Y)  # Calculate correlation matrix
correlation_coefficient = correlation_matrix[0, 1]  # Extract the correlation coefficient

# Print the correlation coefficient to check how strongly the variables are related
print(f"Correlation coefficient: {correlation_coefficient:.4f}")

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, Y)  # Fit the model to the data

# Print the coefficient of determination (R²) to evaluate the model fit
Rsquare = model.score(X, Y)
print('Coefficient of determination (R²):', Rsquare)

# Print the model's intercept and slope (equation of the regression line)
print('Intercept (𝑏₀):', model.intercept_)
print('Slope (𝑏₁):', model.coef_)

# Print the equation of the line
print(f"Equation of the line: Y = {model.intercept_} + {model.coef_[0]} * X")

# Extract intercept and slope for later use
intercept = model.intercept_
slope = model.coef_[0]

# Display the final equation in a more readable format
print(f'Intercept (𝑏₀): {intercept:.2f}')
print(f'Slope (𝑏₁): {slope:.2f}')                                         

# Display the regression line on the plot
plt.plot(X, model.predict(X), color='Green', label='Regression line')

# Add the regression equation to the plot as text
equation = f"Y = {intercept:.2f} + {slope:.2f} * X"
plt.text(0.95, 0.05, equation, fontsize=12, color='black', ha='right', va='bottom', transform=plt.gca().transAxes)

# Label the axes and add a title
plt.xlabel(' Total Expected Goal Difference')
plt.ylabel(' Total Goal Difference')
plt.title('Relationship Between Expected Goal Difference and Goal Difference')

# Loop through each data point and add the corresponding team logo at the position of each point
for i in range(len(X)):
    img = mpimg.imread(image_paths[i])  # Read the team logo image
    imagebox = OffsetImage(img, zoom=0.5)  # Resize the image to fit the plot
    ab = AnnotationBbox(imagebox, (X[i], Y[i]), frameon=False, xycoords='data', boxcoords="data")  # Position the image
    plt.gca().add_artist(ab)  # Add the image to the plot

# Add the Premier League logo in the top-left corner of the plot
Logo_image_path = 'images/PL_Logo.png'  # Path to the logo image
Logo_img = mpimg.imread(Logo_image_path)  # Read the logo image
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo image

# Position the Premier League logo
ab_Logo = AnnotationBbox(Logo_imagebox, (0.05, 0.77), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)

# Display the regression equation as a label on the plot
plt.text(0.95, 0.05, equation, fontsize=12, color='black', ha='right', va='bottom', transform=plt.gca().transAxes)

# Add the legend to the plot
plt.legend()

# Show the plot
plt.show()

# Example prediction: predicting Total Points (Y) when Total Goal Difference (X) is 20
xNew = np.array([[20]])

# Manual prediction using the regression formula
yNew_manual = model.intercept_ + model.coef_[0] * xNew

# Prediction using the model's predict method
yPred = model.predict(xNew)

# Print both predictions for comparison
print(f"Prediction (Manual calculation): {yNew_manual[0][0]:.2f}")
print(f"Prediction (Using model.predict): {yPred[0]:.2f}")