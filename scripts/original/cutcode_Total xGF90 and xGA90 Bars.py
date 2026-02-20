# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:57:49 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Open the Excel workbook and access the specific sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Load the Excel workbook
sheet = book.sheet_by_name('Sheet17')  # Access the sheet named 'Sheet17'

# Extract the Total Expected Goals For per Match (xGF/90) and Total Expected Goals Against per Match (xGA/90)
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # xGF/90 - Reshaped to a 2D array
Y = np.array(sheet.col_values(1))  # xGA/90

# Calculate the averages of xGF/90 (X) and xGA/90 (Y)
X_avg = np.mean(X)  # Average of xGF/90
Y_avg = np.mean(Y)  # Average of xGA/90

# Print the average values to the console for inspection
print(f"Average of X (Average Total xGF/90): {X_avg:.2f}")
print(f"Average of Y (Average Total xGA/90): {Y_avg:.2f}")

# Reverse the order of the teams for visualization purposes (this allows for the first team to appear at the bottom)
reversed_indices = np.arange(len(X))[::-2]  # Reverse the indices to create a reverse bar chart
reversed_X = X.flatten()[::-1]  # Reverse the values of xGF/90
reversed_Y = Y[::-1]  # Reverse the values of xGA/90

# Create a figure and axis object for the plot with specific size and background color
fig, ax = plt.subplots(figsize=(14, 11), facecolor='beige')  # Set figure size (14x11) and background color
ax.set_facecolor('beige')  # Set the plot area background color to beige

# List of team names for labeling the y-axis
team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', 'Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd'
]

# Calculate the highest and lowest values for xGF/90 and xGA/90
highest_xGF90 = np.max(X)  # Find the maximum xGF/90
lowest_xGF90 = np.min(X)   # Find the minimum xGF/90
highest_xGA90 = np.max(Y)  # Find the maximum xGA/90
lowest_xGA90 = np.min(Y)   # Find the minimum xGA/90

# Identify the indices of the teams with the highest and lowest values
highest_xGF90_team_index = np.argmax(X)  # Index of team with highest xGF/90
lowest_xGF90_team_index = np.argmin(X)  # Index of team with lowest xGF/90
highest_xGA90_team_index = np.argmax(Y)  # Index of team with highest xGA/90
lowest_xGA90_team_index = np.argmin(Y)  # Index of team with lowest xGA/90

# Print the highest and lowest values along with the corresponding teams to the console
print(f"Highest Total xGF/90: {highest_xGF90:.2f} by {team_names[highest_xGF90_team_index]}")
print(f"Lowest Total xGF/90: {lowest_xGF90:.2f} by {team_names[lowest_xGF90_team_index]}")
print(f"Highest Total xGA/90: {highest_xGA90:.2f} by {team_names[highest_xGA90_team_index]}")
print(f"Lowest Total xGA/90: {lowest_xGA90:.2f} by {team_names[lowest_xGA90_team_index]}")

# Set the bar height for the horizontal bar chart
bar_height = 0.45  # Height of each bar

# Create an array of indices for the teams, reversed for plotting
indices = np.arange(len(X))  # Create indices for each team
reversed_indices = indices[::-1]  # Reverse the indices to plot from bottom to top

# Plot the horizontal bars for xGF/90 and xGA/90
xGF90_bars = ax.barh(reversed_indices + bar_height / 2, X.flatten(), bar_height, label='Total Expected Goal For per Match', color='lightblue')  # Blue bars for xGF/90
xGA90_bars = ax.barh(reversed_indices - bar_height / 2, Y, bar_height, label='Total Expected Goal Against per Match', color='orange')  # Orange bars for xGA/90

# Set the labels for the axes and the plot title
ax.set_ylabel('Teams')  # Label for the y-axis (Teams)
ax.set_xlabel('xGF/90 and xGA/90')  # Label for the x-axis (xGF/90 and xGA/90)
ax.set_title('Expected Goals For per Match and Expected Goals Against per Match for the Teams of the 2023/24 EPL Season')  # Title of the plot

# Set the y-ticks to correspond to the reversed indices and label them with team names
ax.set_yticks(reversed_indices)  # Set y-ticks at the reversed indices
ax.set_yticklabels(team_names)  # Set y-tick labels to the team names

# Display the legend to label the bars (xGF/90 and xGA/90)
ax.legend()

# Annotate each bar with its respective value (xGF/90 and xGA/90)
for bar in xGF90_bars:
    width = bar.get_width()  # Get the width of the bar (xGF/90)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')  # Add label to xGF/90 bars

for bar in xGA90_bars:
    width = bar.get_width()  # Get the width of the bar (xGA/90)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')  # Add label to xGA/90 bars

# Add the Premier League logo to the plot (in the top-left corner)
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo image
Logo_img = mpimg.imread(Logo_image_path)  # Read the image from the specified path
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo with zoom factor 0.2

# Position the logo in the top-left corner of the plot area
ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo to the plot

# Add text annotations for the average and extreme values of xGF/90 and xGA/90
plt.text(0.72, 0.45, f"Avg Total xGF/90: {X_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.72, 0.42, f"Avg Total xGD/90: {Y_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Add annotations for the highest and lowest values for xGF/90 and xGA/90
plt.text(0.72, 0.39, f"Highest Total xGF/90: {highest_xGF90:.2f} by {team_names[highest_xGF90_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.72, 0.36, f"Lowest Total xGF/90: {lowest_xGF90:.2f} by {team_names[lowest_xGF90_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.72, 0.33, f"Highest Total xGD/90: {highest_xGA90:.2f} by {team_names[highest_xGA90_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.72, 0.30, f"Lowest Total xGD/90: {lowest_xGA90:.2f} by {team_names[lowest_xGA90_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Adjust the layout to ensure all elements fit within the figure area
plt.tight_layout()

# Show the plot
plt.show()