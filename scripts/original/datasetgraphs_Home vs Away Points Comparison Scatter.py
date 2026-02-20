# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:13:41 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Open the Excel workbook and access the sheet by name
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Path to the Excel file
sheet = book.sheet_by_name('Sheet14')  # Access the specific sheet containing the data

# Extract the data from the sheet: Home points (X) and Away points (Y)
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # Home points (X), reshaped into a column vector
Y = np.array(sheet.col_values(1))  # Away points (Y)

# List of image paths for each team in the dataset
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

# Print X and Y arrays for verification
print(X)
print(Y)
    
# Check if the number of teams and the number of images match
if len(X) != len(image_paths):
    raise ValueError(f"Length mismatch: len(X)={len(X)} and len(image_paths)={len(image_paths)}")

# Calculate the average of Home and Away points
X_avg = np.mean(X)  # Average of Home points
Y_avg = np.mean(Y)  # Average of Away points

# Print the average points to the console
print(f"Average of X (Home Points): {X_avg:.2f}")
print(f"Average of Y (Away Points): {Y_avg:.2f}")

# Create a figure for plotting and set the background color to beige
fig, ax = plt.subplots(figsize=(12, 6), facecolor='Beige')
ax.set_facecolor('beige')  # Set the background color for the axes

# Create a scatter plot with Home points on the x-axis and Away points on the y-axis
plt.scatter(X, Y, color='red', s=1, label='Teams')  # Red dots for each team's data

# Customize the appearance of the plot's spines (edges)
ax.spines['top'].set_visible(True)  # Make the top spine visible
ax.spines['right'].set_visible(True)  # Make the right spine visible
ax.spines['top'].set_color('Green')  # Set the color of the top spine to green
ax.spines['top'].set_linewidth(2)  # Set the line width of the top spine
ax.spines['right'].set_color('Green')  # Set the color of the right spine to green
ax.spines['right'].set_linewidth(2)  # Set the line width of the right spine

# Adjust the position of the spines based on the average points
ax.spines['top'].set_position(('outward', Y_avg * -8.2))  # Move the top spine outward relative to the average Away points
ax.spines['right'].set_position(('outward', X_avg * -10.4))  # Move the right spine outward relative to the average Home points

# Add labels and a title to the plot
plt.xlabel('Home Points')  # Label for the x-axis
plt.ylabel('Away Points')  # Label for the y-axis
plt.title('Comparison of Home Points vs Away Points')  # Title of the plot

# Add team logos to the plot as images at the corresponding (X, Y) positions
for i in range(len(X)):  # Loop over each team
    img = mpimg.imread(image_paths[i])  # Read the image for the current team
    imagebox = OffsetImage(img, zoom=0.5)  # Resize the image to fit
    ab = AnnotationBbox(imagebox, (X[i], Y[i]), frameon=False, xycoords='data', boxcoords="data")  # Add the image at the (X, Y) point
    plt.gca().add_artist(ab)  # Add the image to the plot

# Add the Premier League logo to the plot
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo
Logo_img = mpimg.imread(Logo_image_path)  # Read the logo image
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo

# Place the Premier League logo in the top-left corner of the plot
ab_Logo = AnnotationBbox(Logo_imagebox, (0.05, 0.83), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo to the plot

# Add some explanatory text to the plot using relative positioning
plt.text(0.89, 0.05, 'Good atHome', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text annotation for teams good at home
plt.text(0.89, 0.02, 'Bad Away', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text annotation for teams bad away
plt.text(0.54, 0.02, f"Avg Home PT: {X_avg:.2f}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Average Home Points text
plt.text(0.43, 0.05, 'Bad atHome', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text annotation for teams bad at home
plt.text(0.43, 0.02, 'Bad Away', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text annotation for teams bad away
plt.text(0.01, 0.41, f"Avg Away PT: {Y_avg:.2f}", fontsize=10, color='black', ha='left', va='top', transform=plt.gca().transAxes)  # Average Away Points text
plt.text(0.01, 0.48, 'Bad atHome', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text annotation for bad at home teams
plt.text(0.01, 0.45, 'Good Away', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text annotation for good away teams
plt.text(0.89, 0.48, 'Good atHome', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text annotation for good at home teams
plt.text(0.89, 0.45, 'Good Away', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text annotation for good away teams

# Add a legend to the plot
plt.legend()

# Display the plot
plt.show()