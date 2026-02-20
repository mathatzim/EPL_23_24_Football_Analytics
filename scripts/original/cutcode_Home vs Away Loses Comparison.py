# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 20:48:11 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
import xlrd

# Reading the data from the Excel file
book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")
sheet = book.sheet_by_name('Sheet12')

X = np.array(sheet.col_values(0)).reshape(-1, 1)  
Y = np.array(sheet.col_values(2))  
S = np.array(sheet.col_values(1))  

X_avg = np.mean(X)
S_avg = np.mean(S)
Y_avg = np.mean(Y)

print(f"Average of X (Average Away Wins): {X_avg:.2f}")
print(f"Average of Y (Average Away Draws): {S_avg:.2f}")
print(f"Average of Y (Average Away Loses): {Y_avg:.2f}")


reversed_indices = np.arange(len(X))[::-2]  
reversed_X = X.flatten()[::-1]  
reversed_Y = Y[::-1]

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 11), facecolor='beige')
ax.set_facecolor('beige')

bar_height = 0.35 
indices = np.arange(len(X))  
reversed_indices = indices[::-1]

wins_bars = ax.barh(reversed_indices + bar_height, X.flatten(), bar_height, label='Away Wins', color='lightblue')
draws_bars = ax.barh(reversed_indices, S, bar_height, label='Away Draws', color='yellow')
lose_bars = ax.barh(reversed_indices - bar_height, Y, bar_height, label='Away Loses', color='orange')

ax.set_ylabel(' Teams')
ax.set_xlabel('Results')
ax.set_title('Away Results for the Teams of the 2023/24 EPL Season')

ax.set_yticks(reversed_indices)  
ax.set_yticklabels([
    'Manchester City', ' Arsenal', 'Liverpool', 'Aston Villa', ' Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', ' Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd'])

ax.legend()

for bar in wins_bars:
    width = bar.get_width()  
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=10, color='black')
    
for bar in draws_bars:
    width = bar.get_width()  
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=10, color='black')

for bar in lose_bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=10, color='black')

plt.text(0.01, 1.00, 'Avg Away Wins: 8.75', fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.15, 1.00, 'Avg Away Draws: 4.10', fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.85, 1.00, 'Avg Away Loses: 6.15', fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

plt.tight_layout()
plt.show()

total_wins = np.sum(X)
total_draws = np.sum(S)
total_losses = np.sum(Y)

# Pie chart data
results = [total_wins, total_draws, total_losses]
labels = ['Home Wins', 'Home Draws', 'Home Losses']
colors = ['lightblue', 'yellow', 'orange']
explode = (0.1, 0, 0)  # Slightly "explode" the wins slice for better visibility

# Plotting the Pie Chart
ax_pie = plt.subplot(211)  # Create a new subplot below the bar chart
ax_pie.pie(results, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, explode=explode, shadow=True)
ax_pie.set_title('Distribution of Away Results')


plt.show()
