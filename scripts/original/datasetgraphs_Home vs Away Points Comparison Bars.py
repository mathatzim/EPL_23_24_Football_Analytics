# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:05:50 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Open the Excel workbook and read data from 'Sheet14'
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Specify the path to the Excel file
sheet = book.sheet_by_name('Sheet14')  # Access the data in the 14th sheet

# Extract the columns: X for Home Points, Y for Away Points
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # First column (X) for home points, reshape to column vector
Y = np.array(sheet.col_values(1))  # Second column (Y) for away points

# Calculate the average home and away points
X_avg = np.mean(X)  # Calculate the average of home points
Y_avg = np.mean(Y)  # Calculate the average of away points

# Print the average values
print(f"Average of X (Average Home Points): {X_avg:.2f}")
print(f"Average of Y (Average Away Points): {Y_avg:.2f}")

# List of team names corresponding to the data
team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', 'Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd'
]

# Calculate highest and lowest points for home and away games
highest_home = np.max(X)  # Highest home points
lowest_home = np.min(X)  # Lowest home points
highest_away = np.max(Y)  # Highest away points
lowest_away = np.min(Y)  # Lowest away points

# Find the indices of the teams with the highest and lowest points
highest_home_team_index = np.argmax(X)  # Index of the team with highest home points
lowest_home_team_index = np.argmin(X)   # Index of the team with lowest home points
highest_away_team_index = np.argmax(Y)  # Index of the team with highest away points
lowest_away_team_index = np.argmin(Y)   # Index of the team with lowest away points

# Print the teams with the highest and lowest home and away points
print(f"Highest Home Points: {highest_home} by {team_names[highest_home_team_index]}")
print(f"Lowest Home Points: {lowest_home} by {team_names[lowest_home_team_index]}")
print(f"Highest Away Points: {highest_away} by {team_names[highest_away_team_index]}")
print(f"Lowest Away Points: {lowest_away} by {team_names[lowest_away_team_index]}") 

# Reversing the order of indices for plotting purposes (for descending team order in the plot)
reversed_indices = np.arange(len(X))[::-1]  # Reversed index array
reversed_X = X.flatten()[::-1]  # Reverse the home points for proper plotting order
reversed_Y = Y[::-1]  # Reverse away points for plotting

# Create a horizontal bar chart with a beige background
fig, ax = plt.subplots(figsize=(14, 8), facecolor='beige')  # Set figure size and background color
ax.set_facecolor('beige')  # Set the background color of the axes

# Bar height for the horizontal bars (adjusting positioning)
bar_height = 0.45 

# Indices of teams (reversed for descending order)
indices = np.arange(len(X))  
reversed_indices = indices[::-1]  # Reverse the order for descending team order in the plot

# Plotting horizontal bars for Home and Away points
home_bars = ax.barh(reversed_indices + bar_height/2, X.flatten(), bar_height, label='Home Points', color='lightblue')  # Light blue for home points
away_bars = ax.barh(reversed_indices - bar_height/2, Y, bar_height, label='Away Points', color='orange')  # Orange for away points

# Set axis labels and title for the plot
ax.set_ylabel('Teams')  # Label for the y-axis (team names)
ax.set_xlabel('Points')  # Label for the x-axis (points)
ax.set_title('Home vs Away Points for the Teams of the 2023/24 EPL Season')  # Plot title

# Set y-ticks to correspond to team names and reverse the order for the descending plot
ax.set_yticks(reversed_indices)  
ax.set_yticklabels(team_names)  # Label each y-tick with the team names

# Add legend to the plot for Home and Away points
ax.legend()

# Add numerical values to the bars
for bar in home_bars:
    width = bar.get_width()  # Get the width of the home points bar
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')  # Display the width of each home bar

for bar in away_bars:
    width = bar.get_width()  # Get the width of the away points bar
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')  # Display the width of each away bar

# Add the Premier League logo in the top-left corner of the plot
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo image
Logo_img = mpimg.imread(Logo_image_path)  # Read the logo image
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo image

# Position the Premier League logo in the top-left corner
ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)

# Display additional text for average home and away points on the plot
plt.text(0.00, 1.00, f"Avg Home Points: {X_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.82, 1.00, f"Avg Away Points: {Y_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Display text for the highest and lowest points for home and away games
plt.text(0.69, 0.18, f"Highest Home Points: {highest_home} by {team_names[highest_home_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.69, 0.15, f"Lowest Home Points: {lowest_home} by {team_names[lowest_home_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.69, 0.12, f"Highest Away Points: {highest_away} by {team_names[highest_away_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.69, 0.09, f"Lowest Away Points: {lowest_away} by {team_names[lowest_away_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Adjust layout to prevent text overlap and ensure everything is visible
plt.tight_layout()

# Display the plot
plt.show()