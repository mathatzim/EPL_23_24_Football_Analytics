# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 14:44:01 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Load the Excel file containing the data
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls") # Path to the Excel file
sheet = book.sheet_by_name('Sheet6')  # Read data from the specified sheet

# Extract the Home Expected Goals For (xG For) and Home Expected Goals Against (xG Against) values
X = np.array(sheet.col_values(0)).reshape(-1,1)  # Home Expected Goals For (xG For)
Y = np.array(sheet.col_values(1))  # Home Expected Goals Against (xG Against)

# List of team logo paths
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
    'images/Sheffield Utd.png'
]

# Print X and Y arrays for verification
print(X)
print(Y)

# Check if the number of teams matches the number of logos
if len(X) != len(image_paths):
    raise ValueError(f"Length mismatch: len(X)={len(X)} and len(image_paths)={len(image_paths)}")

# Calculate the average xG For and xG Against values
X_avg = np.mean(X)
Y_avg = np.mean(Y)

# Print the average values for reference
print(f"Average of X (Home Expected Goals For): {X_avg:.2f}")
print(f"Average of Y (Home Expected Goals Against): {Y_avg:.2f}")

# Set up the figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 6), facecolor='beige')  # Set the figure size and background color
ax.set_facecolor('beige')  # Set the axes background color

# Scatter plot of Home Expected Goals For vs Home Expected Goals Against
plt.scatter(X, Y, color='red', s=1, label='Teams')

# Customize the axes spines (edges)
ax.spines['top'].set_visible(True)  # Show the top spine
ax.spines['right'].set_visible(True)  # Show the right spine

# Set color and thickness of the spines
ax.spines['top'].set_color('Green')  
ax.spines['top'].set_linewidth(2)

ax.spines['right'].set_color('Green')  
ax.spines['right'].set_linewidth(2)

# Adjust the positions of the spines based on average values
ax.spines['top'].set_position(('outward', Y_avg * -6.5))  
ax.spines['right'].set_position(('outward', X_avg * -13.3))

# Set labels and title for the plot
plt.xlabel('Home Expected Goals For')  # x-axis label
plt.ylabel('Home Expected Goals Against')  # y-axis label
plt.title('Comparison of Home Expected Goals For vs Home Expected Goals Against')  # plot title

# Loop through each team to add their logos to the plot
for i in range(len(X)):
    img = mpimg.imread(image_paths[i])  # Read the logo image
    imagebox = OffsetImage(img, zoom=0.5)  # Create an image box with zoom
    ab = AnnotationBbox(imagebox, (X[i], Y[i]), frameon=False, xycoords='data', boxcoords="data")  # Place logo at (X[i], Y[i])
    plt.gca().add_artist(ab)  # Add the logo to the plot

# Add Premier League logo to the top-right corner
Logo_image_path = 'images/PL_Logo.png'  
Logo_img = mpimg.imread(Logo_image_path)  # Load the Premier League logo
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo

# Place the Premier League logo at a fixed position (top-right corner)
ab_Logo = AnnotationBbox(Logo_imagebox, (0.95, 0.83), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)

# Add text annotations to indicate performance areas and averages
plt.text(0.88, 0.05, 'Good Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.88, 0.02, 'Good Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.35, 0.02, f"Avg xG For: {X_avg:.2f}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.02, 0.05, 'Bad Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.02, 0.02, 'Good Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.83, 0.47, f"Avg xG Against: {Y_avg:.2f}", fontsize=10, color='black', ha='left', va='top', transform=plt.gca().transAxes)
plt.text(0.02, 0.53, 'Bad Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.02, 0.50, 'Bad Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.88, 0.53, 'Good Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.88, 0.50, 'Bad Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Add a legend (in case we have labels or different markers)
plt.legend()

# Display the plot
plt.show()

