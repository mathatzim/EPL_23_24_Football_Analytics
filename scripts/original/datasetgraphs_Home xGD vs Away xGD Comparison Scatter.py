# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 18:55:36 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Load the Excel file and access the relevant sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Open the Excel file
sheet = book.sheet_by_name('Sheet10')  # Access the sheet that contains the Home and Away data

# Extracting Home Expected Goal Difference (X) and Away Expected Goal Difference (Y)
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # Home Expected Goal Difference (xGD)
Y = np.array(sheet.col_values(1))  # Away Expected Goal Difference (xGD)

# List of paths to the team logos for embedding them in the plot
image_paths = [
    'images/Manchester City.png', 'images/Arsenal.png', 'images/Liverpool.png', 'images/Aston Villa.png',
    'images/Tottenham.png', 'images/Chelsea.png', 'images/Newcastle Utd.png', 'images/Manchester Utd.png',
    'images/West Ham.png', 'images/Crystal Palace.png', 'images/Bournemouth.png', 'images/Brighton.png',
    'images/Everton.png', 'images/Fulham.png', 'images/Wolves.png', 'images/Brentford.png',
    'images/Nottingham Forest.png', 'images/Luton Town.png', 'images/Burnley.png', 'images/Sheffield Utd.png'
]

# Print X and Y arrays for verification
print(X)
print(Y)

# Ensure that the length of X matches the number of logos
if len(X) != len(image_paths):
    raise ValueError(f"Length mismatch: len(X)={len(X)} and len(image_paths)={len(image_paths)}")

# Calculate the averages for Home and Away Expected Goal Difference (xGD)
X_avg = np.mean(X)  # Average of Home Expected Goal Difference
Y_avg = np.mean(Y)  # Average of Away Expected Goal Difference

# Print out the average values for Home xGD and Away xGD
print(f"Average of X (Home Expected Goal Difference): {X_avg:.2f}")
print(f"Average of Y (Away Expected Goal Difference): {Y_avg:.2f}")

# Create the figure and axis for plotting
fig, ax = plt.subplots(figsize=(12, 6), facecolor='beige')  # Set plot size and background color
ax.set_facecolor('beige')  # Set axes background color

# Scatter plot for Home Expected Goal Difference vs. Away Expected Goal Difference
plt.scatter(X, Y, color='red', s=1, label='Teams')  # Scatter plot of the data

# Customize axis spines (the lines around the plot)
ax.spines['top'].set_visible(True)  # Show the top spine
ax.spines['right'].set_visible(True)  # Show the right spine

# Set the color and thickness of the top and right spines
ax.spines['top'].set_color('Green')
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_color('Green')
ax.spines['right'].set_linewidth(2)

# Position the top and right spines outward based on the averages
ax.spines['top'].set_position(('outward', Y_avg * 22.5))
ax.spines['right'].set_position(('outward', X_avg * -51.2))

# Labeling the axes and adding a title
plt.xlabel('Home Expected Goal Difference')  # x-axis label
plt.ylabel('Away Expected Goal Difference')  # y-axis label
plt.title('Comparison of Home Expected Goal Difference vs Away Expected Goal Difference')  # Plot title

# Loop to add team logos at the corresponding coordinates
for i in range(len(X)):
    img = mpimg.imread(image_paths[i])  # Load the team logo
    imagebox = OffsetImage(img, zoom=0.5)  # Resize the image
    ab = AnnotationBbox(imagebox, (X[i], Y[i]), frameon=False, xycoords='data', boxcoords="data")  # Add image to the plot at the team's position
    plt.gca().add_artist(ab)  # Add the logo to the plot

# Load the Premier League logo and place it in the top-left corner
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo
Logo_img = mpimg.imread(Logo_image_path)  # Load the logo image
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo image

# Position the Premier League logo in the top-left corner of the plot
ab_Logo = AnnotationBbox(Logo_imagebox, (0.05, 0.95), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo as an annotation on the plot

# Add text annotations for categorizing different areas in the plot
# The text annotations explain the four quadrants in terms of good/bad at home and away performance
plt.text(0.88, 0.05, 'Good at Home', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.88, 0.02, 'Bad Away', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.43, 0.02, 'Avg Home xGD: 7.58', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.01, 0.05, 'Bad at Home', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.01, 0.02, 'Bad Away', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.01, 0.46, 'Avg Away xGD: -7.61', fontsize=10, color='black', ha='left', va='top', transform=plt.gca().transAxes)
plt.text(0.01, 0.53, 'Bad at Home', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.01, 0.50, 'Good Away', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.88, 0.53, 'Good at Home', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.88, 0.50, 'Good Away', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Adding the legend to the plot
plt.legend()

# Show the plot
plt.show()  # Display the plot in the window
