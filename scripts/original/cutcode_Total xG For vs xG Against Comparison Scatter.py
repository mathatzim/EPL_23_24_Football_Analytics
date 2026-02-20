# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:18:39 2024

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Open the Excel file and read the relevant sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Open the Excel file
sheet = book.sheet_by_name('Sheet5')  # Access the sheet named 'Sheet5'

# Extract the data for 'Total Expected Goals For' (X) and 'Total Expected Goals Against' (Y)
X = np.array(sheet.col_values(0)).reshape(-1,1)  # Reshape the 'Total Expected Goals For' column into a column vector
Y = np.array(sheet.col_values(1))  # Extract 'Total Expected Goals Against' from the second column

# Define the image paths for team logos
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

# Ensure the number of team logos matches the number of teams in the data
if len(X) != len(image_paths):
    raise ValueError(f"Length mismatch: len(X)={len(X)} and len(image_paths)={len(image_paths)}")

# Calculate the average of Total Expected Goals For (X) and Total Expected Goals Against (Y)
X_avg = np.mean(X)
Y_avg = np.mean(Y)

# Print out the averages for inspection
print(f"Average of X (Total Expected Goals For): {X_avg:.2f}")
print(f"Average of Y (Total Expected Goals Against): {Y_avg:.2f}")

# Create the plot with specified figure size and background color
fig, ax = plt.subplots(figsize=(12, 6), facecolor='beige')  # Create a figure with size (12, 6)
ax.set_facecolor('beige')  # Set the background color of the plot

# Plot the scatter plot of Total Expected Goals For (X) vs Total Expected Goals Against (Y)
plt.scatter(X, Y, color='red', s=1, label='Teams')  # Red points for each team, size of points = 1

# Customize the appearance of the plot axes (spines)
ax.spines['top'].set_visible(True)  # Make the top spine visible
ax.spines['right'].set_visible(True)  # Make the right spine visible

# Set the color and width for the top and right spines
ax.spines['top'].set_color('Green')
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_color('Green')
ax.spines['right'].set_linewidth(2)

# Set the position of the top and right spines to be offset from the average values of X and Y
ax.spines['top'].set_position(('outward',  Y_avg * -2.2))  # Move the top spine downward
ax.spines['right'].set_position(('outward', X_avg * -6.5))  # Move the right spine to the left

# Set the x and y axis labels and title
plt.xlabel('Total Expected Goals For')  # Label for the x-axis
plt.ylabel('Total Expected Goals Against')  # Label for the y-axis
plt.title('Comparison of Expected Goals For vs Expected Goals Against')  # Title of the plot

# Add team logo images for each data point (representing each team)
for i in range(len(X)):  # Loop through each team
    img = mpimg.imread(image_paths[i])  # Read the image for the team
    imagebox = OffsetImage(img, zoom=0.5)  # Create an OffsetImage instance with zoom factor 0.5
    ab = AnnotationBbox(imagebox, (X[i], Y[i]), frameon=False, xycoords='data', boxcoords="data")  # Place the image at the (X, Y) position
    plt.gca().add_artist(ab)  # Add the image to the plot

# Add the Premier League logo at the top-right corner of the plot
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo image
Logo_img = mpimg.imread(Logo_image_path)  # Read the image
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Create an OffsetImage with a zoom factor of 0.2

# Position the logo within the axes using the axes fraction coordinates
ab_Logo = AnnotationBbox(Logo_imagebox, (0.95, 0.83), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo to the plot

# Add textual annotations on the plot to indicate average xG and descriptive categories
plt.text(0.88, 0.05, 'Good Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text for 'Good Offense'
plt.text(0.88, 0.02, 'Good Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text for 'Good Defense'
plt.text(0.44, 0.02, f"Avg xG For: {X_avg:.2f}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Average xG For
plt.text(0.02, 0.05, 'Bad Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text for 'Bad Offense'
plt.text(0.02, 0.02, 'Good Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text for 'Good Defense'
plt.text(0.01, 0.58, f"Avg xG Against: {Y_avg:.2f}", fontsize=10, color='black', ha='left', va='top', transform=plt.gca().transAxes)  # Average xG Against
plt.text(0.02, 0.65, 'Bad Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text for 'Bad Offense'
plt.text(0.02, 0.62, 'Bad Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text for 'Bad Defense'
plt.text(0.88, 0.65, 'Good Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text for 'Good Offense'
plt.text(0.88, 0.62, 'Bad Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Text for 'Bad Defense'

# Show the legend to describe the scatter plot
plt.legend()

# Display the plot
plt.show()  # Render the plot
