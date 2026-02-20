# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 20:48:11 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

# Load the Excel file and access the relevant sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Open the Excel workbook
sheet = book.sheet_by_name('Sheet13')  # Access the data sheet (Sheet13)

# Extract the data columns for Away Wins (X), Away Draws (S), and Away Loses (Y)
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # Away Wins data from the first column
S = np.array(sheet.col_values(1))  # Away Draws data from the second column
Y = np.array(sheet.col_values(2))  # Away Loses data from the third column

# Calculate the average values for Away Wins, Draws, and Loses across all teams
X_avg = np.mean(X)  # Average of Away Wins
S_avg = np.mean(S)  # Average of Away Draws
Y_avg = np.mean(Y)  # Average of Away Loses

# Print the averages for user reference
print(f"Average of X (Average Away Wins): {X_avg:.2f}")
print(f"Average of Y (Average Away Draws): {S_avg:.2f}")
print(f"Average of Y (Average Away Loses): {Y_avg:.2f}")

# Reverse the indices for plotting purposes
reversed_indices = np.arange(len(X))[::-2]  # Reverse the indices for plotting
reversed_X = X.flatten()[::-1]  # Flatten and reverse the Away Wins data
reversed_Y = Y[::-1]  # Reverse the Away Loses data

# Set up the plot figure and axis
fig, ax = plt.subplots(figsize=(14, 11), facecolor='beige')  # Create a plot with a beige background
ax.set_facecolor('beige')  # Set the background color of the plot

# Team names for the Premier League teams
team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', ' Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', ' Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd']

# Find the highest and lowest values for Away Wins, Draws, and Loses
highest_Wins = np.max(X)  # Maximum value for Away Wins
lowest_Wins = np.min(X)  # Minimum value for Away Wins
highest_Draws = np.max(S)  # Maximum value for Away Draws
lowest_Draws = np.min(S)  # Minimum value for Away Draws
highest_Loses = np.max(Y)  # Maximum value for Away Loses
lowest_Loses = np.min(Y)  # Minimum value for Away Loses

# Find the team indices corresponding to the highest and lowest values
highest_Wins_team_index = np.argmax(X)  # Index of team with highest Away Wins
lowest_Wins_team_index = np.argmin(X)  # Index of team with lowest Away Wins
highest_Draws_team_index = np.argmax(S)  # Index of team with highest Away Draws
lowest_Draws_team_index = np.argmin(S)  # Index of team with lowest Away Draws
highest_Loses_team_index = np.argmax(Y)  # Index of team with highest Away Loses
lowest_Loses_team_index = np.argmin(Y)  # Index of team with lowest Away Loses

# Print the highest and lowest values along with the corresponding teams
print(f"Highest Away Wins: {highest_Wins} by {team_names[highest_Wins_team_index]}")
print(f"Lowest Away Wins: {lowest_Wins} by {team_names[lowest_Wins_team_index]}")
print(f"Highest Away Draws: {highest_Draws} by {team_names[highest_Draws_team_index]}")
print(f"Lowest Away Draws: {lowest_Draws} by {team_names[lowest_Draws_team_index]}")
print(f"Highest Away Loses: {highest_Loses} by {team_names[highest_Loses_team_index]}")
print(f"Lowest Away Loses: {lowest_Loses} by {team_names[lowest_Loses_team_index]}")

# Set bar height for the bar charts
bar_height = 0.35  # Height of the bars in the bar chart
indices = np.arange(len(X))  # Indices for the teams
reversed_indices = indices[::-1]  # Reverse the indices to flip the order of teams for better visualization

# Create horizontal bar charts for Away Wins, Draws, and Loses
wins_bars = ax.barh(reversed_indices + bar_height, X.flatten(), bar_height, label='Away Wins', color='lightblue')
draws_bars = ax.barh(reversed_indices, S, bar_height, label='Away Draws', color='yellow')
lose_bars = ax.barh(reversed_indices - bar_height, Y, bar_height, label='Away Loses', color='orange')

# Set labels for the axes and title
ax.set_ylabel(' Teams')  # Y-axis label
ax.set_xlabel('Results')  # X-axis label
ax.set_title('Away Results for the Teams of the 2023/24 EPL Season')  # Title of the plot

# Set the tick marks and labels for the Y-axis
ax.set_yticks(reversed_indices)  # Set Y-axis ticks based on reversed indices
ax.set_yticklabels(team_names)  # Set the team names as the labels on the Y-axis

# Add a legend to the plot
ax.legend()  # Show legend for Away Wins, Away Draws, and Away Loses

# Add the values of each bar to the bars (to show the numerical value)
for bar in wins_bars:
    width = bar.get_width()  # Get the width of each bar (Away Wins value)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

for bar in draws_bars:
    width = bar.get_width()  # Get the width of each bar (Away Draws value)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

for bar in lose_bars:
    width = bar.get_width()  # Get the width of each bar (Away Loses value)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

# Load and add the Premier League logo to the plot
Logo_image_path = 'images/PL_Logo.png'  # Path to the Premier League logo image
Logo_img = mpimg.imread(Logo_image_path)  # Read the logo image
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo image

# Position the logo on the plot using AnnotationBbox
ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo to the plot

# Add text annotations with the averages and highest/lowest results
plt.text(0.00, 1.00, f"Avg Away Wins: {X_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.15, 1.00, f"Avg Away Draws: {S_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.85, 1.00, f"Avg Away Loses: {Y_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Add text annotations with the highest/lowest results for Away Wins, Draws, and Loses
plt.text(0.70, 0.44, f"Highest Away Wins: {highest_Wins} by {team_names[highest_Wins_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.41, f"Lowest Away Wins: {lowest_Wins} by {team_names[lowest_Wins_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.38, f"Highest Away Draws: {highest_Draws} by {team_names[highest_Draws_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.35, f"Lowest Away Draws: {lowest_Draws} by {team_names[lowest_Draws_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.32, f"Highest Away Loses: {highest_Loses} by {team_names[highest_Loses_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.29, f"Lowest Away Loses: {lowest_Loses} by {team_names[lowest_Loses_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

# Make sure everything fits in the layout
plt.tight_layout()

# Display the plot
plt.show()

