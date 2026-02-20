# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 20:27:49 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Load the Excel file and access the relevant sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Open the Excel workbook
sheet = book.sheet_by_name('Sheet12')  # Access the data sheet (Sheet12)

# Extract the data columns for Home Wins (X), Home Draws (S), and Home Loses (Y)
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # Home Wins
S = np.array(sheet.col_values(1))  # Home Draws
Y = np.array(sheet.col_values(2))  # Home Loses

# Calculate the average values for Home Wins, Draws, and Loses
X_avg = np.mean(X)  # Average of Home Wins
S_avg = np.mean(S)  # Average of Home Draws
Y_avg = np.mean(Y)  # Average of Home Loses

# Print the average values for Home Wins, Draws, and Loses
print(f"Average of X (Average Home Wins): {X_avg:.2f}")
print(f"Average of Y (Average Home Draws): {S_avg:.2f}")
print(f"Average of Y (Average Home Loses): {Y_avg:.2f}")

# Reverse the order of the indices for plotting the teams from top to bottom
reversed_indices = np.arange(len(X))[::-2]  # Reverse the indices, step 2 for spacing
reversed_X = X.flatten()[::-1]  # Reverse the Home Wins values
reversed_Y = Y[::-1]  # Reverse the Home Loses values

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(14, 11), facecolor='beige')  # Set the figure size and background color
ax.set_facecolor('beige')  # Set the background color of the axes

# List of team names for the y-axis labels
team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', 'Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd']

# Identify the highest and lowest values for Home Wins, Draws, and Loses
highest_Wins = np.max(X)  # Highest Home Wins
lowest_Wins = np.min(X)  # Lowest Home Wins
highest_Draws = np.max(S)  # Highest Home Draws
lowest_Draws = np.min(S)  # Lowest Home Draws
highest_Loses = np.max(Y)  # Highest Home Loses
lowest_Loses = np.min(Y)  # Lowest Home Loses

# Find the indices of the teams with the highest and lowest values for Home Wins, Draws, and Loses
highest_Wins_team_index = np.argmax(X)  # Team with the highest Home Wins
lowest_Wins_team_index = np.argmin(X)  # Team with the lowest Home Wins
highest_Draws_team_index = np.argmax(S)  # Team with the highest Home Draws
lowest_Draws_team_index = np.argmin(S)  # Team with the lowest Home Draws
highest_Loses_team_index = np.argmax(Y)  # Team with the highest Home Loses
lowest_Loses_team_index = np.argmin(Y)  # Team with the lowest Home Loses

# Print the highest and lowest values for Home Wins, Draws, and Loses along with the teams
print(f"Highest Home Wins: {highest_Wins} by {team_names[highest_Wins_team_index]}")
print(f"Lowest Home Wins: {lowest_Wins} by {team_names[lowest_Wins_team_index]}")
print(f"Highest Home Draws: {highest_Draws} by {team_names[highest_Draws_team_index]}")
print(f"Lowest Home Draws: {lowest_Draws} by {team_names[lowest_Draws_team_index]}")
print(f"Highest Home Loses: {highest_Loses} by {team_names[highest_Loses_team_index]}")
print(f"Lowest Home Loses: {lowest_Loses} by {team_names[lowest_Loses_team_index]}")

# Set the bar height for horizontal bars
bar_height = 0.35  
indices = np.arange(len(X))  # Create an array of indices for the bars
reversed_indices = indices[::-1]  # Reverse the indices to plot bars from top to bottom

# Create horizontal bars for Home Wins, Draws, and Loses
wins_bars = ax.barh(reversed_indices + bar_height, X.flatten(), bar_height, label='Home Wins', color='lightblue')
draws_bars = ax.barh(reversed_indices, S, bar_height, label='Home Draws', color='yellow')
lose_bars = ax.barh(reversed_indices - bar_height, Y, bar_height, label='Home Loses', color='orange')

# Set labels and title for the plot
ax.set_ylabel('Teams')  # Label for the y-axis
ax.set_xlabel('Results')  # Label for the x-axis
ax.set_title('Home Results for the Teams of the 2023/24 EPL Season')  # Title for the plot

# Set the y-ticks to match the reversed indices and label the teams
ax.set_yticks(reversed_indices)  
ax.set_yticklabels(team_names)  # Display team names on the y-axis

# Add a legend to differentiate between Home Wins, Draws, and Loses
ax.legend()

# Add data labels to each bar (display the value next to the bar)
for bar in wins_bars:
    width = bar.get_width()  # Get the width (value) of the Home Wins bar
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')
    
for bar in draws_bars:
    width = bar.get_width()  # Get the width (value) of the Home Draws bar
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

for bar in lose_bars:
    width = bar.get_width()  # Get the width (value) of the Home Loses bar
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

# Add the Premier League logo to the plot
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo image
Logo_img = mpimg.imread(Logo_image_path)  # Read the logo image
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo

# Place the logo in the bottom-left corner using axes fraction coordinates
ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo to the plot

# Add text annotations for average, highest, and lowest values
plt.text(0.00, 1.00, f"Avg Home Wins: {X_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.15, 1.00, f"Avg Home Draws: {S_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.85, 1.00, f"Avg Home Loses: {Y_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Add detailed text annotations about the highest and lowest values for Home Wins, Draws, and Loses
plt.text(0.70, 0.44, f"Highest Home Wins: {highest_Wins} by {team_names[highest_Wins_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.41, f"Lowest Home Wins: {lowest_Wins} by {team_names[lowest_Wins_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.38, f"Highest Home Draws: {highest_Draws} by {team_names[highest_Draws_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.35, f"Lowest Home Draws: {lowest_Draws} by {team_names[lowest_Draws_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.32, f"Highest Home Loses: {highest_Loses} by {team_names[highest_Loses_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.29, f"Lowest Home Loses: {lowest_Loses} by {team_names[lowest_Loses_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Adjust the layout to ensure everything fits properly
plt.tight_layout()

# Display the plot
plt.show()
