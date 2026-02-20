# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:31:01 2025

@author: mathaios
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Load the Excel file and access the relevant sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Open the Excel file
sheet = book.sheet_by_name('Sheet7')  # Access the sheet that contains the away data

# Extracting Away Expected Goals For (X) and Away Expected Goals Against (Y)
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # Expected Goals For (Away)
Y = np.array(sheet.col_values(1))  # Expected Goals Against (Away)

# Calculate the averages for Away xG For (X) and Away xG Against (Y)
X_avg = np.mean(X)  # Average of Away Expected Goals For
Y_avg = np.mean(Y)  # Average of Away Expected Goals Against

# Print out the average values for Away xG For and Away xG Against
print(f"Average of X (Away Expected Goals For): {X_avg:.2f}")
print(f"Average of Y (Away Expected Goals Against): {Y_avg:.2f}")

# Reverse the order of the data for visualization purposes (teams are plotted from bottom to top)
reversed_indices = np.arange(len(X))[::-1]  # Reverse indices for the teams
reversed_X = X.flatten()[::-1]  # Reverse the X values (xG For)
reversed_Y = Y[::-1]  # Reverse the Y values (xG Against)

# Create the figure and axis for plotting
fig, ax = plt.subplots(figsize=(14, 8), facecolor='beige')  # Set plot size and background color
ax.set_facecolor('beige')  # Set axes background color

# List of team names for labeling on the y-axis
team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', 'Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd'
]

# Identify the highest and lowest values for both xG For and xG Against
highest_xGFor = np.max(X)  # Maximum xG For (Away)
lowest_xGFor = np.min(X)  # Minimum xG For (Away)
highest_xGAgainst = np.max(Y)  # Maximum xG Against (Away)
lowest_xGAgainst = np.min(Y)  # Minimum xG Against (Away)

# Identify which teams have the highest and lowest xG For and xG Against
highest_xGFor_team_index = np.argmax(X)  # Index of the team with the highest xG For
lowest_xGFor_team_index = np.argmin(X)  # Index of the team with the lowest xG For
highest_xGAgainst_team_index = np.argmax(Y)  # Index of the team with the highest xG Against
lowest_xGAgainst_team_index = np.argmin(Y)  # Index of the team with the lowest xG Against

# Print out the teams with the highest and lowest xG For and xG Against
print(f"Highest Away xGFor: {highest_xGFor} by {team_names[highest_xGFor_team_index]}")
print(f"Lowest Away xGFor: {lowest_xGFor} by {team_names[lowest_xGFor_team_index]}")
print(f"Highest Away xGAgainst: {highest_xGAgainst} by {team_names[highest_xGAgainst_team_index]}")
print(f"Lowest Away xGAgainst: {lowest_xGAgainst} by {team_names[lowest_xGAgainst_team_index]}")

# Set the bar height for the horizontal bars and create an array of team indices for plotting
bar_height = 0.45  # Bar height for the horizontal bars
indices = np.arange(len(X))  # Indices of the teams
reversed_indices = indices[::-1]  # Reverse indices for proper order in the plot

# Create horizontal bars for both xG For and xG Against
xGFor_bars = ax.barh(reversed_indices + bar_height / 2, X.flatten(), bar_height, label='Away Expected Goals For', color='lightblue')  # xG For bars
xGAgainst_bars = ax.barh(reversed_indices - bar_height / 2, Y, bar_height, label='Away Expected Goals Against', color='orange')  # xG Against bars

# Set the axis labels and title for the plot
ax.set_ylabel('Teams')  # y-axis label
ax.set_xlabel('Expected Goals For/Against')  # x-axis label
ax.set_title('Comparison of Away xG For vs Away xG Against')  # Plot title

# Set the y-axis ticks and labels to display the team names
ax.set_yticks(reversed_indices)  # Set the y-ticks to the reversed team indices
ax.set_yticklabels(team_names)  # Set the y-tick labels to the team names

# Add the plot legend
ax.legend()

# Add text annotations to show the exact values on top of the bars for better clarity
for bar in xGFor_bars:  # Loop over the xG For bars
    width = bar.get_width()  # Get the width (value) of the bar
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')  # Display the value next to the bar

for bar in xGAgainst_bars:  # Loop over the xG Against bars
    width = bar.get_width()  # Get the width (value) of the bar
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')  # Display the value next to the bar

# Load the Premier League logo image and add it to the plot
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo image
Logo_img = mpimg.imread(Logo_image_path)  # Load the logo image
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo image

# Position the Premier League logo in the bottom-left corner of the axes
ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo as an annotation on the plot

# Add text annotations to display the average and extreme values for Away xG For and Away xG Against
plt.text(0.00, 1.00, f"Avg Away xG For: {X_avg:.2f}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Avg xG For text
plt.text(0.82, 1.00, f"Avg Away xG Against: {Y_avg:.2f}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)  # Avg xG Against text

# Display details for the highest and lowest values
plt.text(0.72, 0.90, f"Highest Away xGFor: {highest_xGFor} by {team_names[highest_xGFor_team_index]}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.72, 0.87, f"Lowest Away xGFor: {lowest_xGFor} by {team_names[lowest_xGFor_team_index]}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.72, 0.84, f"Highest Away xGAgainst: {highest_xGAgainst} by {team_names[highest_xGAgainst_team_index]}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.72, 0.81, f"Lowest Away xGAgainst: {lowest_xGAgainst} by {team_names[lowest_xGAgainst_team_index]}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Adjust layout to make sure everything fits without overlap
plt.tight_layout()

# Display the plot
plt.show()  # Show the plot in the window