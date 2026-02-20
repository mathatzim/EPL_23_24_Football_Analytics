# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:45:19 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
import xlrd

# Load the Excel file and access the relevant sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Open the Excel file
sheet = book.sheet_by_name('Sheet13')  # Access the sheet named 'Sheet13' containing the data

# Extract data columns for Away Wins (X), Away Draws (S), and Away Loses (Y)
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # Extract Away Wins (first column) and reshape it as a column vector
S = np.array(sheet.col_values(1))  # Extract Away Draws (second column)
Y = np.array(sheet.col_values(2))  # Extract Away Loses (third column)

# Calculate the total values for Away Wins, Away Draws, and Away Loses
total_wins = np.sum(X)  # Sum of Away Wins (total number of wins across all teams)
total_draws = np.sum(S)  # Sum of Away Draws (total number of draws across all teams)
total_losses = np.sum(Y)  # Sum of Away Loses (total number of losses across all teams)

# Create a list of the total results for pie chart plotting
results = [total_wins, total_draws, total_losses]  # The values to plot (Away Wins, Away Draws, Away Loses)
labels = ['Away Wins', 'Away Draws', 'Away Losses']  # Labels for each segment of the pie chart
colors = ['lightblue', 'yellow', 'orange']  # Colors to represent the different segments
explode = (0, 0, 0.1)  # Slightly "explode" the Away Losses segment (highlight it)

# Create a subplot for the pie chart (positioned on the first row of the figure)
ax_pie = plt.subplot(211)  # Create a subplot in a 2-row grid at position 1 (top row)

# Plot the pie chart with the specified data and formatting
ax_pie.pie(
    results,  # Data to plot (Away Wins, Away Draws, Away Loses)
    labels=labels,  # Labels for each segment
    autopct='%1.1f%%',  # Format the percentage labels on the pie chart
    colors=colors,  # Set colors for each segment
    startangle=90,  # Start the pie chart from the 90-degree angle
    explode=explode,  # Highlight the Away Losses segment (exploding it out slightly)
    shadow=True  # Add shadow effect to the pie chart for visual appeal
)

# Set the title for the pie chart
ax_pie.set_title('Distribution of Away Results')  # Title of the pie chart

# Display the plot
plt.show()  # Show the generated pie chart