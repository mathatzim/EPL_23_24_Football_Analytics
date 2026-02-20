# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:55:05 2024

@author: mathaios
"""

import numpy as np
from sklearn.linear_model import LinearRegression  # For linear regression model
import matplotlib.pyplot as plt  # For plotting graphs
from matplotlib.offsetbox import OffsetImage, AnnotationBbox  # For adding images to the plot
import matplotlib.image as mpimg  # For reading image files
import xlrd  # For reading Excel files
import statsmodels.api as sm  # For statistical models

# Open the Excel workbook and read the data from the specified sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Specify your file path
sheet = book.sheet_by_name('Sheet3')  # Accessing data from 'Sheet3'
X = np.array(sheet.col_values(0))  # Extract first column (e.g., Total Goal Difference)
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

# Add a constant (intercept) to the X data for statsmodels
X_with_intercept = sm.add_constant(X)

# Create and fit a linear regression model using statsmodels
model_stats = sm.OLS(Y, X_with_intercept)  # Ordinary Least Squares regression model
results = model_stats.fit()

# Print the regression results summary from statsmodels
print(results.summary())

# Now that we have the p-values, we can extract them for interpretation
p_value = results.pvalues[1]  # Extract p-value for the slope (X coefficient)

# If the p-value is less than 0.05, we can reject the null hypothesis that the slope is 0 (no relationship).
if p_value < 0.05:
    print(f"The relationship between X (Total Goal Difference) and Y (Total Points) is statistically significant (p-value = {p_value:.4f}).")
else:
    print(f"The relationship between X (Total Goal Difference) and Y (Total Points) is not statistically significant (p-value = {p_value:.4f}).")

# Create and train the linear regression model using sklearn
model_sklearn = LinearRegression()
model_sklearn.fit(X.reshape(-1, 1), Y)  # Fit the model to the data

# Calculate the correlation coefficient to understand the relationship between X and Y
correlation_matrix = np.corrcoef(X.flatten(), Y)  # Calculate the correlation matrix
correlation_coefficient = correlation_matrix[0, 1]  # Extract the correlation coefficient

# Print the correlation coefficient
print(f"Correlation coefficient: {correlation_coefficient:.4f}")

# Calculate and print the coefficient of determination (R²) to evaluate the model fit
Rsquare = model_sklearn.score(X.reshape(-1, 1), Y)
print('Coefficient of determination (R²):', Rsquare)

# Print the model's intercept and slope (equation of the regression line)
print('Intercept (𝑏₀):', model_sklearn.intercept_)
print('Slope (𝑏₁):', model_sklearn.coef_)

# Print the equation of the line
print(f"Equation of the line: Y = {model_sklearn.intercept_} + {model_sklearn.coef_[0]} * X")

# Extract intercept and slope for later use
intercept = model_sklearn.intercept_
slope = model_sklearn.coef_[0]                                     

# Create a plot with beige background
plt.figure(figsize=(12, 6), facecolor='beige')
plt.gca().set_facecolor('beige')

# Scatter plot to display the relationship between the goal difference (X) and points (Y)
plt.scatter(X, Y, color='red', label=' Teams', s=10)

# Display the regression line on the plot
plt.plot(X, model_sklearn.predict(X.reshape(-1, 1)), color='Green', label='Regression line')

# Add the regression equation to the plot as text
equation = f"Y = {intercept:.2f} + {slope:.2f} * X"
plt.text(0.95, 0.05, equation, fontsize=12, color='black', ha='right', va='bottom', transform=plt.gca().transAxes)

# Label the axes and add a title
plt.xlabel(' Total Goal Difference')
plt.ylabel(' Total Points')
plt.title('Relationship Between Points and Goal Difference')

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
yNew_manual = model_sklearn.intercept_ + model_sklearn.coef_[0] * xNew

# Prediction using the model's predict method
yPred = model_sklearn.predict(xNew)

# Print both predictions for comparison
print(f"Prediction (Manual calculation): {yNew_manual[0][0]:.2f}")
print(f"Prediction (Using model.predict): {yPred[0]:.2f}")