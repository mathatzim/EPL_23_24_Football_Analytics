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

book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")
sheet = book.sheet_by_name('Sheet12')

X = np.array(sheet.col_values(0)).reshape(-1, 1)  
Y = np.array(sheet.col_values(2))  
S = np.array(sheet.col_values(1))  

X_avg = np.mean(X)
S_avg = np.mean(S)
Y_avg = np.mean(Y)

print(f"Average of X (Average Home Wins): {X_avg:.2f}")
print(f"Average of Y (Average Home Draws): {S_avg:.2f}")
print(f"Average of Y (Average Home Loses): {Y_avg:.2f}")


reversed_indices = np.arange(len(X))[::-2]  
reversed_X = X.flatten()[::-1]  
reversed_Y = Y[::-1]

fig, ax = plt.subplots(figsize=(14, 11), facecolor='beige')
ax.set_facecolor('beige')

team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', ' Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', ' Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd']

highest_Wins = np.max(X)
lowest_Wins = np.min(X)
highest_Draws = np.max(S)
lowest_Draws = np.min(S)
highest_Loses = np.max(Y)
lowest_Loses = np.min(Y)

highest_Wins_team_index = np.argmax(X)  
lowest_Wins_team_index = np.argmin(X)
highest_Draws_team_index = np.argmax(S)  
lowest_Draws_team_index = np.argmin(S)   
highest_Loses_team_index = np.argmax(Y)  
lowest_Loses_team_index = np.argmin(Y) 

print(f"Highest Home Wins: {highest_Wins} by {team_names[highest_Wins_team_index]}")
print(f"Lowest Home Wins: {lowest_Wins} by {team_names[lowest_Wins_team_index]}")
print(f"Highest Home Draws: {highest_Draws} by {team_names[highest_Draws_team_index]}")
print(f"Lowest Home Draws: {lowest_Draws} by {team_names[lowest_Draws_team_index]}")
print(f"Highest Home Loses: {highest_Loses} by {team_names[highest_Loses_team_index]}")
print(f"Lowest Home Loses: {lowest_Loses} by {team_names[lowest_Loses_team_index]}")

bar_height = 0.35 
indices = np.arange(len(X))  
reversed_indices = indices[::-1]

wins_bars = ax.barh(reversed_indices + bar_height, X.flatten(), bar_height, label='Home Wins', color='lightblue')
draws_bars = ax.barh(reversed_indices, S, bar_height, label='Home Draws', color='yellow')
lose_bars = ax.barh(reversed_indices - bar_height, Y, bar_height, label='Home Loses', color='orange')

ax.set_ylabel(' Teams')
ax.set_xlabel('Results')
ax.set_title('Home Results for the Teams of the 2023/24 EPL Season')

ax.set_yticks(reversed_indices)  
ax.set_yticklabels(team_names)

ax.legend()

for bar in wins_bars:
    width = bar.get_width()  
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')
    
for bar in draws_bars:
    width = bar.get_width()  
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

for bar in lose_bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

Logo_image_path = 'images/PL_Logo.png'  
Logo_img = mpimg.imread(Logo_image_path)
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)

ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)

plt.text(0.00, 1.00, f"Avg Home Wins: {X_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.15, 1.00, f"Avg Home Draws: {S_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.85, 1.00, f"Avg Home Loses: {Y_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

plt.text(0.70, 0.44, f"Highest Home Wins: {highest_Wins} by {team_names[highest_Wins_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.41, f"Lowest Home Wins: {lowest_Wins} by {team_names[lowest_Wins_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.38, f"Highest Home Draws: {highest_Draws} by {team_names[highest_Draws_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.35, f"Lowest Home Draws: {lowest_Draws} by {team_names[lowest_Draws_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.32, f"Highest Home Loses: {highest_Loses} by {team_names[highest_Loses_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.70, 0.29, f"Lowest Home Loses: {lowest_Loses} by {team_names[lowest_Loses_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

plt.tight_layout()
plt.show()
