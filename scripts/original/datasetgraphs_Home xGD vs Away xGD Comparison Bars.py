# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:40:03 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Load the Excel file containing the data and access the relevant sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Open the Excel workbook
sheet = book.sheet_by_name('Sheet10')  # Access the sheet with the data

# Extract Home Expected Goal Difference (X) and Away Expected Goal Difference (Y) values
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # Home Expected Goal Difference
Y = np.array(sheet.col_values(1))  # Away Expected Goal Difference

# Reversing the order of the indices for later use in bar positioning
reversed_indices = np.arange(len(X))[::-1]  # Reverse the indices to plot the bars in reverse order
reversed_X = X.flatten()[::-1]  # Reverse the Home Expected Goal Difference values
reversed_Y = Y[::-1]  # Reverse the Away Expected Goal Difference values

# Calculate the average values of Home and Away Expected Goal Difference
X_avg = np.mean(X)  # Average of Home Expected Goal Difference
Y_avg = np.mean(Y)  # Average of Away Expected Goal Difference

# Print out the average values for Home and Away Expected Goal Difference
print(f"Average of X (Home Expected Goal Difference): {X_avg:.2f}")
print(f"Average of Y (Away Expected Goal Difference): {Y_avg:.2f}")

# Create the plot with customized size and background color
fig, ax = plt.subplots(figsize=(14, 8), facecolor='beige')  # Set figure size and background color
ax.set_facecolor('beige')  # Set the background color of the axes

# List of team names for the labels on the y-axis
team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', 'Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd']

# Identify the highest and lowest values for both Home and Away Expected Goal Differences
highest_home_xGD = np.max(X)  # Highest Home Expected Goal Difference
lowest_home_xGD = np.min(X)  # Lowest Home Expected Goal Difference
highest_away_xGD = np.max(Y)  # Highest Away Expected Goal Difference
lowest_away_xGD = np.min(Y)  # Lowest Away Expected Goal Difference

# Find the teams with the highest and lowest values for Home and Away Expected Goal Differences
highest_home_xGD_team_index = np.argmax(X)  # Index of team with highest Home xGD
lowest_home_xGD_team_index = np.argmin(X)   # Index of team with lowest Home xGD
highest_away_xGD_team_index = np.argmax(Y)  # Index of team with highest Away xGD
lowest_away_xGD_team_index = np.argmin(Y)   # Index of team with lowest Away xGD

# Print out which teams have the highest and lowest values for Home and Away Expected Goal Differences
print(f"Highest Home xGD: {highest_home_xGD} by {team_names[highest_home_xGD_team_index]}")
print(f"Lowest Home xGD: {lowest_home_xGD} by {team_names[lowest_home_xGD_team_index]}")
print(f"Highest Away xGD: {highest_away_xGD} by {team_names[highest_away_xGD_team_index]}")
print(f"Lowest Away xGD: {lowest_away_xGD} by {team_names[lowest_away_xGD_team_index]}")

# Set bar height for horizontal bars
bar_height = 0.45 
indices = np.arange(len(X))  # Generate indices for the bars
reversed_indices = indices[::-1]  # Reverse the order of the indices to plot bars from top to bottom

# Create horizontal bars for Home Expected Goal Difference and Away Expected Goal Difference
home_bars = ax.barh(reversed_indices + bar_height / 2, X.flatten(), bar_height, label='Home Expected Goal Difference', color='lightblue')
away_bars = ax.barh(reversed_indices - bar_height / 2, Y, bar_height, label='Away Expected Goal Difference', color='orange')

# Customize the axes labels and the plot title
ax.set_ylabel('Teams')  # Set y-axis label
ax.set_xlabel('Home/Away Expected Goal Difference')  # Set x-axis label
ax.set_title('Comparison of Home xG Difference vs Away xG Difference')  # Set the plot title

# Set y-ticks to match the reversed indices and label the teams
ax.set_yticks(reversed_indices)  
ax.set_yticklabels(team_names)  # Set the team names as the y-tick labels

# Add the legend to the plot
ax.legend()

# Add data labels to each bar (display the numerical value of each bar)
for bar in home_bars:
    width = bar.get_width()  # Get the width of each bar (the xGD value)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

for bar in away_bars:
    width = bar.get_width()  # Get the width of each bar (the xGD value)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

# Add the Premier League logo in the bottom-left corner of the plot
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo image
Logo_img = mpimg.imread(Logo_image_path)  # Read the image file
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo

# Place the logo in the bottom-left corner using axes fraction coordinates
ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo to the plot

# Add text annotations with the average, highest, and lowest values for Home and Away xGD
plt.text(0.71, 0.17, f'Avg Home xG Dif: {X_avg:.2f}', fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.71, 0.14, f'Avg Away xG Dif: {Y_avg:.2f}', fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Add the highest and lowest Home and Away xGD values
plt.text(0.71, 0.11, f"Highest Home xGD: {highest_home_xGD} by {team_names[highest_home_xGD_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.71, 0.08, f"Lowest Home xGD: {lowest_home_xGD} by {team_names[lowest_home_xGD_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.71, 0.05, f"Highest Away xGD: {highest_away_xGD} by {team_names[highest_away_xGD_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.71, 0.02, f"Lowest Away xGD: {lowest_away_xGD} by {team_names[lowest_away_xGD_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Adjust the layout to ensure that everything fits well
plt.tight_layout()

# Display the plot
plt.show()