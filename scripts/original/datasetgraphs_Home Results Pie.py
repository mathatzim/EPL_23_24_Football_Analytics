# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:43:27 2025

@author: mathaios
"""
import numpy as np
import matplotlib.pyplot as plt
import xlrd

# Load the Excel file and access the relevant sheet
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")  # Open the Excel workbook
sheet = book.sheet_by_name('Sheet12')  # Access the data sheet (Sheet12)

# Extract the data columns for Home Wins (X), Home Draws (S), and Home Loses (Y)
X = np.array(sheet.col_values(0)).reshape(-1, 1)  # Home Wins data from the first column
S = np.array(sheet.col_values(1))  # Home Draws data from the second column
Y = np.array(sheet.col_values(2))  # Home Loses data from the third column

# Calculate the total values for Home Wins, Draws, and Loses across all teams
total_wins = np.sum(X)  # Sum of all Home Wins
total_draws = np.sum(S)  # Sum of all Home Draws
total_losses = np.sum(Y)  # Sum of all Home Loses

# Group the results into a list for the pie chart
results = [total_wins, total_draws, total_losses]  # Total Wins, Draws, and Losses
labels = ['Home Wins', 'Home Draws', 'Home Losses']  # Labels for the pie chart
colors = ['lightblue', 'yellow', 'orange']  # Colors for the different sections of the pie chart
explode = (0.1, 0, 0)  # "Explode" the first slice (Home Wins) for emphasis

# Create a subplot for the pie chart
ax_pie = plt.subplot(211)  # Create a subplot (top part of the figure)

# Create the pie chart
ax_pie.pie(results, 
           labels=labels,  # Labels for each section
           autopct='%1.1f%%',  # Display percentage on each slice
           colors=colors,  # Color scheme for the pie chart
           startangle=90,  # Start angle for the pie chart (rotates the chart)
           explode=explode,  # Make the Home Wins section stand out
           shadow=True)  # Add shadow effect for the pie chart

# Set the title for the pie chart
ax_pie.set_title('Distribution of Home Results')  # Title for the pie chart

# Display the plot
plt.show()  # Show the pie chart to the user