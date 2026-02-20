# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:11:46 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Open the Excel workbook and access the specific sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Load the Excel workbook
sheet = book.sheet_by_name('Sheet15')  # Access the sheet named 'Sheet15'

# Extract the Total Points (X) and Total Expected Goal Difference (Y) columns
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # Total Points - Reshaped to a 2D array
Y = np.array(sheet.col_values(1))  # Total Expected Goal Difference (xGD)

# Calculate the averages of Total Points (X) and xGD (Y)
X_avg = np.mean(X)  # Average Total Points
Y_avg = np.mean(Y)  # Average Total xGD

# Print the average values to the console for inspection
print(f"Average of X (Average Total Points): {X_avg:.2f}")
print(f"Average of Y (Average Total xGD): {Y_avg:.2f}")

# Reverse the order of the teams for visualization purposes
reversed_indices = np.arange(len(X))[::-2]  # Reverse the indices to create a reverse bar chart
reversed_X = X.flatten()[::-1]  # Reverse the values of Total Points
reversed_Y = Y[::-1]  # Reverse the values of Total Expected Goal Difference

# Create a figure and axis object for the plot, with specific size and background color
fig, ax = plt.subplots(figsize=(14, 11), facecolor='beige')  # Set figure size (14x11) and background color
ax.set_facecolor('beige')  # Set the plot area background color

# Define the list of team names to label the y-axis
team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', 'Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd'
]

# Calculate the highest and lowest values for Total Points and Total xGD
highest_Points = np.max(X)  # Find the maximum Total Points
lowest_Points = np.min(X)   # Find the minimum Total Points
highest_xGD = np.max(Y)  # Find the maximum xGD
lowest_xGD = np.min(Y)   # Find the minimum xGD

# Identify the indices of the teams with the highest and lowest values
highest_Points_team_index = np.argmax(X)  # Index of team with highest Total Points
lowest_Points_team_index = np.argmin(X)  # Index of team with lowest Total Points
highest_xGD_team_index = np.argmax(Y)  # Index of team with highest xGD
lowest_xGD_team_index = np.argmin(Y)  # Index of team with lowest xGD

# Print the highest and lowest values and the corresponding teams
print(f"Highest Total Points: {highest_Points} by {team_names[highest_Points_team_index]}")
print(f"Lowest Total Points: {lowest_Points} by {team_names[lowest_Points_team_index]}")
print(f"Highest Total xGD: {highest_xGD} by {team_names[highest_xGD_team_index]}")
print(f"Lowest Total xGD: {lowest_xGD} by {team_names[lowest_xGD_team_index]}")

# Set the bar height for the horizontal bar chart
bar_height = 0.35  # Height of each bar

# Create an array of indices for the teams, reversed for plotting
indices = np.arange(len(X))  # Create indices for each team
reversed_indices = indices[::-1]  # Reverse the indices

# Plot the horizontal bars for Total Points and Total Expected Goal Difference (xGD)
wins_bars = ax.barh(reversed_indices + bar_height, X.flatten(), bar_height, label='Total Points', color='lightblue')  # Blue bars for Total Points
lose_bars = ax.barh(reversed_indices - bar_height, Y, bar_height, label='Total Expected Goal Difference', color='orange')  # Orange bars for xGD

# Set the labels for the axes and the plot title
ax.set_ylabel('Teams')  # Label for the y-axis (Teams)
ax.set_xlabel('Points and xGD')  # Label for the x-axis (Points and xGD)
ax.set_title('Total Points and Expected Goal Difference for the Teams of the 2023/24 EPL Season')  # Title of the plot

# Set the y-ticks to correspond to the reversed indices and label them with team names
ax.set_yticks(reversed_indices)  # Set y-ticks at the reversed indices
ax.set_yticklabels(team_names)  # Set y-tick labels to the team names

# Display the legend to label the bars (Total Points and Total xGD)
ax.legend()

# Annotate each bar with its respective value (Total Points and Total xGD)
for bar in wins_bars:
    width = bar.get_width()  # Get the width of the bar (Total Points)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')  # Add label to Total Points bars

for bar in lose_bars:
    width = bar.get_width()  # Get the width of the bar (xGD)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')  # Add label to xGD bars

# Add the Premier League logo to the plot (in the top-left corner)
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo image
Logo_img = mpimg.imread(Logo_image_path)  # Read the image from the specified path
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo with zoom factor 0.2

# Position the logo in the top-left corner of the plot area
ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo to the plot

# Add text annotations for the average and extreme values of Total Points and xGD
plt.text(0.00, 1.00, f"Avg Total Points: {X_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.85, 1.00, f"Avg Total xGD: {Y_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Add annotations for the highest and lowest values for Total Points and xGD
plt.text(0.70, 0.14, f"Highest Total Points: {highest_Points} by {team_names[highest_Points_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.11, f"Lowest Total Points: {lowest_Points} by {team_names[lowest_Points_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.08, f"Highest Total xGD: {highest_xGD} by {team_names[highest_xGD_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.05, f"Lowest Total xGD: {lowest_xGD} by {team_names[lowest_xGD_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Adjust the layout to ensure all elements fit within the figure area
plt.tight_layout()

# Show the plot
plt.show()