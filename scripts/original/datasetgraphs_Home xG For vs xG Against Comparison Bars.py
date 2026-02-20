# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:27:08 2025

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
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # Home Expected Goals For (xG For)
Y = np.array(sheet.col_values(1))  # Home Expected Goals Against (xG Against)

# Calculate the average values for Home Expected Goals For (xG For) and Home Expected Goals Against (xG Against)
X_avg = np.mean(X)
Y_avg = np.mean(Y)

# Print the average xG For and xG Against values for reference
print(f"Average of X (Home Expected Goals For): {X_avg:.2f}")
print(f"Average of Y (Home Expected Goals Against): {Y_avg:.2f}")

# Reverse the order of the indices for plotting (for a top-down approach)
reversed_indices = np.arange(len(X))[::-1]  # Reversed indices for bar chart
reversed_X = X.flatten()[::-1]  # Reversed X values for plotting (Home Expected Goals For)
reversed_Y = Y[::-1]  # Reversed Y values for plotting (Home Expected Goals Against)

# Set up the figure and axis for the bar chart
fig, ax = plt.subplots(figsize=(14, 8), facecolor='beige')  # Set figure size and background color
ax.set_facecolor('beige')  # Set the axes background color to beige

# List of team names corresponding to the data
team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', 'Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd'
]

# Calculate the highest and lowest values for both xG For and xG Against
highest_xGFor = np.max(X)  # Maximum value for Home Expected Goals For
lowest_xGFor = np.min(X)  # Minimum value for Home Expected Goals For
highest_xGAgainst = np.max(Y)  # Maximum value for Home Expected Goals Against
lowest_xGAgainst = np.min(Y)  # Minimum value for Home Expected Goals Against

# Find the indices of the teams with the highest and lowest xG For and xG Against
highest_xGFor_team_index = np.argmax(X)  # Index of team with the highest xG For
lowest_xGFor_team_index = np.argmin(X)   # Index of team with the lowest xG For
highest_xGAgainst_team_index = np.argmax(Y)  # Index of team with the highest xG Against
lowest_xGAgainst_team_index = np.argmin(Y)  # Index of team with the lowest xG Against

# Print out the teams with the highest and lowest xG For and xG Against for reference
print(f"Highest Home xGFor: {highest_xGFor} by {team_names[highest_xGFor_team_index]}")
print(f"Lowest Home xGFor: {lowest_xGFor} by {team_names[lowest_xGFor_team_index]}")
print(f"Highest Home xGAgainst: {highest_xGAgainst} by {team_names[highest_xGAgainst_team_index]}")
print(f"Lowest Home xGAgainst: {lowest_xGAgainst} by {team_names[lowest_xGAgainst_team_index]}")

# Define bar height for visualization of both xG For and xG Against
bar_height = 0.45  # Height of each bar to prevent overlap

# Create horizontal bar chart for Home Expected Goals For (xG For) and Home Expected Goals Against (xG Against)
indices = np.arange(len(X))  # Create indices for the teams
reversed_indices = indices[::-1]  # Reverse the indices for top-down plotting

# Bar chart for Home Expected Goals For (xG For)
xGFor_bars = ax.barh(reversed_indices + bar_height/2, X.flatten(), bar_height, label='Home Expected Goals For', color='lightblue')

# Bar chart for Home Expected Goals Against (xG Against)
xGAgainst_bars = ax.barh(reversed_indices - bar_height/2, Y, bar_height, label='Home Expected Goals Against', color='orange')

# Set labels and title for the plot
ax.set_ylabel('Teams')  # y-axis label
ax.set_xlabel('Expected Goals For/Against')  # x-axis label
ax.set_title('Comparison of Home xG For vs Home xG Against')  # plot title

# Set the y-ticks to the reversed indices for proper team labeling
ax.set_yticks(reversed_indices)  
ax.set_yticklabels(team_names)  # Set the team names as labels

# Add a legend to the plot
ax.legend()

# Add text labels for each bar (show the exact values of xG For and xG Against)
for bar in xGFor_bars:
    width = bar.get_width()  # Get the width of the bar (xG For value)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

for bar in xGAgainst_bars:
    width = bar.get_width()  # Get the width of the bar (xG Against value)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

# Load the Premier League logo and add it to the plot
Logo_image_path = 'images/PL_Logo.png'  
Logo_img = mpimg.imread(Logo_image_path)  # Load the image
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo

# Position the logo at a fixed location in the plot (bottom-left corner)
ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo to the plot

# Add text annotations showing key statistics (averages, highest and lowest xG values)
plt.text(0.68, 0.27, f"Avg Home xG For: {X_avg:.2f}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.68, 0.24, f"Avg Home xG Against: {Y_avg:.2f}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Add text for teams with the highest and lowest xG values
plt.text(0.68, 0.21, f"Highest Home xGFor: {highest_xGFor} by {team_names[highest_xGFor_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.68, 0.18, f"Lowest Home xGFor: {lowest_xGFor} by {team_names[lowest_xGFor_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.68, 0.15, f"Highest Home xGAgainst: {highest_xGAgainst} by {team_names[highest_xGAgainst_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.68, 0.12, f"Lowest Home xGAgainst: {lowest_xGAgainst} by {team_names[lowest_xGAgainst_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Adjust layout to ensure everything fits within the plot
plt.tight_layout()

# Display the plot
plt.show()