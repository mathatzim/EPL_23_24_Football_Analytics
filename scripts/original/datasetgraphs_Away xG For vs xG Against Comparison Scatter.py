# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:29:19 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Load the Excel file and access the relevant sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls") # Path to the Excel file
sheet = book.sheet_by_name('Sheet7')  # Sheet name for away data

# Extract the data for Away Expected Goals For (xG For) and Away Expected Goals Against (xG Against)
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # xG For (Expected Goals For) for away teams
Y = np.array(sheet.col_values(1))  # xG Against (Expected Goals Against) for away teams

# List of image paths for the teams
image_paths = [
    'images/Manchester City.png', 'images/Arsenal.png', 'images/Liverpool.png', 
    'images/Aston Villa.png', 'images/Tottenham.png', 'images/Chelsea.png', 
    'images/Newcastle Utd.png', 'images/Manchester Utd.png', 'images/West Ham.png', 
    'images/Crystal Palace.png', 'images/Bournemouth.png', 'images/Brighton.png', 
    'images/Everton.png', 'images/Fulham.png', 'images/Wolves.png', 'images/Brentford.png', 
    'images/Nottingham Forest.png', 'images/Luton Town.png', 'images/Burnley.png', 
    'images/Sheffield Utd.png'
]

# Print X and Y arrays for verification
print(X)
print(Y)

# Check if the lengths of X and image_paths match
if len(X) != len(image_paths):
    raise ValueError(f"Length mismatch: len(X)={len(X)} and len(image_paths)={len(image_paths)}")

# Calculate the averages for Away xG For (X) and Away xG Against (Y)
X_avg = np.mean(X)  # Average of Away Expected Goals For
Y_avg = np.mean(Y)  # Average of Away Expected Goals Against

# Print out the average values of xG For and xG Against
print(f"Average of X (Away Expected Goals For): {X_avg:.2f}")
print(f"Average of Y (Away Expected Goals Against): {Y_avg:.2f}")

# Set up the figure and axis for the scatter plot
fig, ax = plt.subplots(figsize=(12, 6), facecolor='beige')  # Create figure and axis, set background color
ax.set_facecolor('beige')  # Set axes background color

# Scatter plot of the teams' Away Expected Goals For vs Away Expected Goals Against
plt.scatter(X, Y, color='red', s=1, label='Teams')  # Plot xG For vs xG Against

# Customize the plot's spine (axes)
ax.spines['top'].set_visible(True)  # Make the top spine visible
ax.spines['right'].set_visible(True)  # Make the right spine visible

# Change the color and line width for the top and right spines for better visualization
ax.spines['top'].set_color('Green')
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_color('Green')
ax.spines['right'].set_linewidth(2)

# Adjust the position of the spines relative to the data
ax.spines['top'].set_position(('outward', Y_avg * -4.3))  # Move the top spine outward based on avg y value
ax.spines['right'].set_position(('outward', X_avg * -14.4))  # Move the right spine outward based on avg x value

# Add labels and title for the plot
plt.xlabel('Away Expected Goals For')  # x-axis label
plt.ylabel('Away Expected Goals Against')  # y-axis label
plt.title('Comparison of Away Expected Goals For vs Away Expected Goals Against')  # plot title

# Loop through the teams and add their logos to the scatter plot
for i in range(len(X)):
    img = mpimg.imread(image_paths[i])  # Load the team logo image
    imagebox = OffsetImage(img, zoom=0.5)  # Resize the image for better fitting
    ab = AnnotationBbox(imagebox, (X[i], Y[i]), frameon=False, xycoords='data', boxcoords="data")  # Position the image
    plt.gca().add_artist(ab)  # Add the logo image as an annotation on the plot

# Load the Premier League logo and add it to the plot
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo image
Logo_img = mpimg.imread(Logo_image_path)  # Load the logo image
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo

# Position the Premier League logo in the top-right corner of the axes
ab_Logo = AnnotationBbox(Logo_imagebox, (0.95, 0.83), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo to the plot

# Add text annotations to describe different performance categories for xG (Good/Bad Offense/Defense)
plt.text(0.88, 0.05, 'Good Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.88, 0.02, 'Good Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.46, 0.02, f"Avg xG For: {X_avg:.2f}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.02, 0.05, 'Bad Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.02, 0.02, 'Good Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.01, 0.54, f"Avg xG Against: {Y_avg:.2f}", fontsize=10, color='black', ha='left', va='top', transform=plt.gca().transAxes)
plt.text(0.02, 0.61, 'Bad Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.02, 0.58, 'Bad Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.88, 0.61, 'Good Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.88, 0.58, 'Bad Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Add a legend to the plot for clarity
plt.legend()

# Display the plot
plt.show()  # This command actually renders the plot and shows it on the screen
