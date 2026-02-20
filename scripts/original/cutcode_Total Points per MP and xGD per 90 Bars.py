# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 12:55:06 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Open the Excel workbook and access the specific sheet with the required data
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Load the Excel file
sheet = book.sheet_by_name('Sheet16')  # Access the data from the sheet named 'Sheet16'

# Extract the values for the total points per match (X) and total expected goal difference per match (Y)
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # X represents Points per Match (reshaped to a 2D array)
Y = np.array(sheet.col_values(1))  # Y represents Expected Goal Difference per Match (xGD/90)

# Calculate the average values for X (Points per Match) and Y (xGD/90)
X_avg = np.mean(X)  # Calculate the average points per match
Y_avg = np.mean(Y)  # Calculate the average expected goal difference per match

# Print the average values to the console
print(f"Average of X (Average Total Points/MP): {X_avg:.2f}")
print(f"Average of Y (Average Total xGD/90): {Y_avg:.2f}")

# Reverse the order of the teams for plotting purposes (so the first team appears at the bottom)
reversed_indices = np.arange(len(X))[::-2]  # Reverse the indices to display in reverse order
reversed_X = X.flatten()[::-1]  # Reverse the points per match data for proper order
reversed_Y = Y[::-1]  # Reverse the xGD/90 data for proper order

# Create the plot with a specific size and background color
fig, ax = plt.subplots(figsize=(14, 11), facecolor='beige')  # Set the plot's size and background color
ax.set_facecolor('beige')  # Set the background color of the plot area to beige

# List of team names to be used as labels on the y-axis
team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', 'Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd'
]

# Calculate the highest and lowest values for Points per Match (X) and Expected Goal Difference per Match (xGD/90)
highest_PointsMP = np.max(X)  # Maximum points per match (X)
lowest_PointsMP = np.min(X)   # Minimum points per match (X)
highest_xGD90 = np.max(Y)  # Maximum xGD/90 (Y)
lowest_xGD90 = np.min(Y)   # Minimum xGD/90 (Y)

# Find the indices of the teams with the highest and lowest values for Points per Match and xGD/90
highest_PointsMP_team_index = np.argmax(X)  # Index of the team with highest points per match
lowest_PointsMP_team_index = np.argmin(X)  # Index of the team with lowest points per match
highest_xGD90_team_index = np.argmax(Y)  # Index of the team with highest xGD/90
lowest_xGD90_team_index = np.argmin(Y)  # Index of the team with lowest xGD/90

# Print the teams with the highest and lowest values for points per match and xGD/90
print(f"Highest Total Points/MP: {highest_PointsMP:.2f} by {team_names[highest_PointsMP_team_index]}")
print(f"Lowest Total Points/MP: {lowest_PointsMP:.2f} by {team_names[lowest_PointsMP_team_index]}")
print(f"Highest Total xGD/90: {highest_xGD90:.2f} by {team_names[highest_xGD90_team_index]}")
print(f"Lowest Total xGD/90: {lowest_xGD90:.2f} by {team_names[lowest_xGD90_team_index]}")

# Define the bar height for the horizontal bar chart
bar_height = 0.45  # Set the height of each bar

# Create an array of indices for the teams (to be used for the positions of the bars)
indices = np.arange(len(X))  # Indices for each team (from 0 to len(X))
reversed_indices = indices[::-1]  # Reverse the order of the indices to have the first team at the bottom

# Create horizontal bar plots for Points per Match (X) and Expected Goal Difference per Match (Y)
PointsMP_bars = ax.barh(reversed_indices + bar_height / 2, X.flatten(), bar_height, label='Total Points per Matches Played', color='lightblue')  # Light blue bars for Points per Match
xGD90_bars = ax.barh(reversed_indices - bar_height / 2, Y, bar_height, label='Total Expected Goal Difference per Match', color='orange')  # Orange bars for xGD/90

# Set the labels for the y-axis (team names) and x-axis (Points per Match and xGD/90)
ax.set_ylabel('Teams')  # Label for the y-axis
ax.set_xlabel('Points/MP and xGD/90')  # Label for the x-axis
ax.set_title('Total Points per Matches Played and Expected Goal Difference per Match for the Teams of the 2023/24 EPL Season')  # Title of the plot

# Set the y-ticks to correspond to the reversed indices and label them with the team names
ax.set_yticks(reversed_indices)  # Set the y-ticks at the reversed indices
ax.set_yticklabels(team_names)  # Set the team names as labels for the y-axis

# Display the legend to differentiate between the two types of bars (Points per Match and xGD/90)
ax.legend()

# Annotate each bar with the respective value (Points/MP and xGD/90) for better readability
for bar in PointsMP_bars:
    width = bar.get_width()  # Get the width of the bar (represents Points/MP)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')  # Add value annotation to Points/MP bars

for bar in xGD90_bars:
    width = bar.get_width()  # Get the width of the bar (represents xGD/90)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')  # Add value annotation to xGD/90 bars

# Add the Premier League logo to the plot in the top-left corner
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo image
Logo_img = mpimg.imread(Logo_image_path)  # Read the logo image from the file
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo with zoom factor of 0.2

# Position the logo in the top-left corner of the plot
ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo to the plot

# Add textual annotations on the plot to display the averages and extremes of Points/MP and xGD/90
plt.text(0.67, 0.17, f"Avg Total Points/MP: {X_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.67, 0.14, f"Avg Total xGD/90: {Y_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Display the highest and lowest values for Points per Match and xGD/90 along with the corresponding teams
plt.text(0.67, 0.11, f"Highest Total Points/MP: {highest_PointsMP:.2f} by {team_names[highest_PointsMP_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.67, 0.08, f"Lowest Total Points/MP: {lowest_PointsMP:.2f} by {team_names[lowest_PointsMP_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.67, 0.05, f"Highest Total xGD/90: {highest_xGD90:.2f} by {team_names[highest_xGD90_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.67, 0.02, f"Lowest Total xGD/90: {lowest_xGD90:.2f} by {team_names[lowest_xGD90_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Adjust the layout to ensure all elements fit within the figure and are not clipped
plt.tight_layout()

# Display the plot
plt.show()