# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:47:46 2025

@author: mathaios
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Open the Excel workbook and select the appropriate sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Load the Excel workbook
sheet = book.sheet_by_name('Sheet5')  # Access the sheet named 'Sheet5'

# Extract the Total Expected Goals For (X) and Total Expected Goals Against (Y) columns
X = np.array(sheet.col_values(0)).reshape(-1,1)  # Convert the 'Expected Goals For' data to a NumPy array and reshape it
Y = np.array(sheet.col_values(1))  # Extract the 'Expected Goals Against' data into a NumPy array

# Calculate the averages of both X (xG For) and Y (xG Against)
X_avg = np.mean(X)  # Calculate the average of Expected Goals For
Y_avg = np.mean(Y)  # Calculate the average of Expected Goals Against

# Print the averages for inspection
print(f"Average of X (Total Expected Goals For): {X_avg:.2f}")
print(f"Average of Y (Total Expected Goals Against): {Y_avg:.2f}")

# Reverse the order of indices and the X, Y values for a reversed vertical bar chart
reversed_indices = np.arange(len(X))[::-1]  # Reverse the indices for plotting in reverse order
reversed_X = X.flatten()[::-1]  # Reverse the values of X (Total xG For)
reversed_Y = Y[::-1]  # Reverse the values of Y (Total xG Against)

# Create a figure and axes object for the plot
fig, ax = plt.subplots(figsize=(14, 8), facecolor='beige')  # Set the size of the plot (14x8) and background color
ax.set_facecolor('beige')  # Set the background color of the plot area

# Define team names for labeling the y-axis
team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', 'Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd'
]

# Find the teams with the highest and lowest xG values for 'xG For' and 'xG Against'
highest_xGFor = np.max(X)  # Highest value for Total Expected Goals For
lowest_xGFor = np.min(X)   # Lowest value for Total Expected Goals For
highest_xGAgainst = np.max(Y)  # Highest value for Total Expected Goals Against
lowest_xGAgainst = np.min(Y)   # Lowest value for Total Expected Goals Against

# Identify the indices of the teams with the highest and lowest xG values
highest_xGFor_team_index = np.argmax(X)  # Index of the team with the highest Total xG For
lowest_xGFor_team_index = np.argmin(X)  # Index of the team with the lowest Total xG For
highest_xGAgainst_team_index = np.argmax(Y)  # Index of the team with the highest Total xG Against
lowest_xGAgainst_team_index = np.argmin(Y)  # Index of the team with the lowest Total xG Against

# Print out the results of the highest and lowest values for inspection
print(f"Highest Total xGFor: {highest_xGFor} by {team_names[highest_xGFor_team_index]}")
print(f"Lowest Total xGFor: {lowest_xGFor} by {team_names[lowest_xGFor_team_index]}")
print(f"Highest Total xGAgainst: {highest_xGAgainst} by {team_names[highest_xGAgainst_team_index]}")
print(f"Lowest Total xGAgainst: {lowest_xGAgainst} by {team_names[lowest_xGAgainst_team_index]}")

# Set the height of the bars in the bar chart
bar_height = 0.45  # The height of each bar in the bar chart

# Generate the indices for the teams in reverse order (for horizontal bars)
indices = np.arange(len(X))  # Create indices for each team
reversed_indices = indices[::-1]  # Reverse the indices for plotting in reverse order

# Plot horizontal bars for Total Expected Goals For and Total Expected Goals Against
xGFor_bars = ax.barh(reversed_indices + bar_height/2, X.flatten(), bar_height, label='Home Expected Goals For', color='lightblue')  # xG For bars in light blue
xGAgainst_bars = ax.barh(reversed_indices - bar_height/2, Y, bar_height, label='Home Expected Goals Against', color='orange')  # xG Against bars in orange

# Set axis labels and title for the plot
ax.set_ylabel('Teams')  # Label for the y-axis
ax.set_xlabel('Expected Goals (xG)')  # Label for the x-axis
ax.set_title('Comparison of Total xG For vs Total xG Against')  # Title for the plot

# Set the y-ticks to the reversed indices and label them with team names
ax.set_yticks(reversed_indices)  
ax.set_yticklabels(team_names)

# Display the legend to explain the bar colors
ax.legend()

# Annotate the bars with the actual xG values
for bar in xGFor_bars:
    width = bar.get_width()  # Get the width (value) of each bar
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')  # Add text label for xG For bars

for bar in xGAgainst_bars:
    width = bar.get_width()  # Get the width (value) of each bar
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')  # Add text label for xG Against bars

# Add the Premier League logo to the plot in the top-left corner
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo image
Logo_img = mpimg.imread(Logo_image_path)  # Read the image file
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo with zoom factor of 0.2

# Place the logo in the specified position (top-left corner)
ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo to the plot

# Add text annotations for the average and extreme values of xG For and xG Against
plt.text(0.00, 1.00, f"Avg Total xG For: {X_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.80, 1.00, f"Avg Total xG Against: {Y_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Display additional annotations for the highest and lowest xG values and their corresponding teams
plt.text(0.70, 0.44, f"Highest Total xGFor: {highest_xGFor} by {team_names[highest_xGFor_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.41, f"Lowest Total xGFor: {lowest_xGFor} by {team_names[lowest_xGFor_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.38, f"Highest Total xGAgainst: {highest_xGAgainst} by {team_names[highest_xGAgainst_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.35, f"Lowest Total xGAgainst: {lowest_xGAgainst} by {team_names[lowest_xGAgainst_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Adjust layout to make sure everything fits
plt.tight_layout()

# Display the final plot
plt.show()