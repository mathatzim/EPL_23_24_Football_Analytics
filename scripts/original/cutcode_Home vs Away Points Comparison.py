# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:05:50 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")
sheet = book.sheet_by_name('Sheet14')

X = np.array(sheet.col_values(0)).reshape(-1, 1)  
Y = np.array(sheet.col_values(1))  

X_avg = np.mean(X)
Y_avg = np.mean(Y)

print(f"Average of X (Average Home Points): {X_avg:.2f}")
print(f"Average of Y (Average Away Points): {Y_avg:.2f}")

team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', 'Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd'
]
highest_home = np.max(X)
lowest_home = np.min(X)
highest_away = np.max(Y)
lowest_away = np.min(Y)

highest_home_team_index = np.argmax(X) 
lowest_home_team_index = np.argmin(X)   
highest_away_team_index = np.argmax(Y)  
lowest_away_team_index = np.argmin(Y) 

print(f"Highest Home Points: {highest_home} by {team_names[highest_home_team_index]}")
print(f"Lowest Home Points: {lowest_home} by {team_names[lowest_home_team_index]}")
print(f"Highest Away Points: {highest_away} by {team_names[highest_away_team_index]}")
print(f"Lowest Away Points: {lowest_away} by {team_names[lowest_away_team_index]}") 

reversed_indices = np.arange(len(X))[::-1]  
reversed_X = X.flatten()[::-1]  
reversed_Y = Y[::-1]

fig, ax = plt.subplots(figsize=(14, 8), facecolor='beige')
ax.set_facecolor('beige')

bar_height = 0.45 
indices = np.arange(len(X))  
reversed_indices = indices[::-1]

home_bars = ax.barh(reversed_indices + bar_height/2, X.flatten(), bar_height, label='Home Points', color='lightblue')
away_bars = ax.barh(reversed_indices - bar_height/2, Y, bar_height, label='Away Points', color='orange')

ax.set_ylabel(' Teams')
ax.set_xlabel(' Points')
ax.set_title('Home vs Away Points for the Teams of the 2023/24 EPL Season')

ax.set_yticks(reversed_indices)  
ax.set_yticklabels(team_names)

ax.legend()

for bar in home_bars:
    width = bar.get_width()  
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

for bar in away_bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

Logo_image_path = 'images/PL_Logo.png'  
Logo_img = mpimg.imread(Logo_image_path)
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)

ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)

plt.text(0.00, 1.00, f"Avg Home Points: {X_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.82, 1.00, f"Avg Away Points: {Y_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

plt.text(0.69, 0.18, f"Highest Home Points: {highest_home} by {team_names[highest_home_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.69, 0.15, f"Lowest Home Points: {lowest_home} by {team_names[lowest_home_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.69, 0.12, f"Highest Away Points: {highest_away} by {team_names[highest_away_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.69, 0.09, f"Lowest Away Points: {lowest_away} by {team_names[lowest_away_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

plt.tight_layout()
plt.show()