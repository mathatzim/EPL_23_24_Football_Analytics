# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 19:18:33 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

import xlrd

book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")
sheet = book.sheet_by_name('Sheet11')

X = np.array(sheet.col_values(0)).reshape(-1,1)
Y = np.array(sheet.col_values(1))

image_paths = [
    'images/Manchester City.png',
    'images/Arsenal.png',
    'images/Liverpool.png',
    'images/Aston Villa.png',
    'images/Tottenham.png',
    'images/Chelsea.png',
    'images/Newcastle Utd.png',
    'images/Manchester Utd.png',
    'images/West Ham.png',
    'images/Crystal Palace.png',
    'images/Bournemouth.png',
    'images/Brighton.png',
    'images/Everton.png',
    'images/Fulham.png',
    'images/Wolves.png',
    'images/Brentford.png',
    'images/Nottingham Forest.png',
    'images/Luton Town.png',
    'images/Burnley.png',
    'images/Sheffield Utd.png']
    

print(X)
print(Y)

if len(X) != len(image_paths):
    raise ValueError(f"Length mismatch: len(X)={len(X)} and len(image_paths)={len(image_paths)}")

X_avg = np.mean(X)
Y_avg = np.mean(Y)

print(f"Average of X (Home Goals Difference): {X_avg:.2f}")
print(f"Average of Y (Away Goals Difference): {Y_avg:.2f}")

fig, ax = plt.subplots(figsize=(12, 6), facecolor='beige')
ax.set_facecolor('beige')
ax.scatter(X, Y, color='red', s=1, label =' Teams')

ax.spines['top'].set_visible(True)  # Show the top spine
ax.spines['bottom'].set_visible(True)  # Show the bottom spine
ax.spines['left'].set_visible(True)  # Show the left spine
ax.spines['right'].set_visible(True)

ax.spines['top'].set_color('Green')  # Set the color of the top spine
ax.spines['top'].set_linewidth(2)

ax.spines['right'].set_color('Green')  # Set the color of the top spine
ax.spines['right'].set_linewidth(2)

ax.spines['top'].set_position(('outward',  Y_avg * 31.3))  # Show the bottom spine
ax.spines['right'].set_position(('outward', X_avg * -44.5))


plt.xlabel(' Home Goals Difference')
plt.ylabel(' Away Goals Difference')
plt.title('Comparison of Home Goals Difference vs Away Goals Difference')
for i in range(len(X)):
    img = mpimg.imread(image_paths[i])  
    imagebox = OffsetImage(img, zoom=0.5)  
    ab = AnnotationBbox(imagebox, (X[i], Y[i]), frameon=False, xycoords='data', boxcoords="data")
    plt.gca().add_artist(ab) 

plt.text(0.89, 0.05, 'Good atHome', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.89, 0.02, 'Bad Away', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.60, 0.02, 'Avg Home GD: 6.10', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.49, 0.05, 'Bad atHome', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.49, 0.02, 'Bad Away', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.01, 0.40, 'Avg Away GD: -6.10', fontsize=10, color='black', ha='left', va='top', transform=plt.gca().transAxes)
plt.text(0.01, 0.46, 'Bad atHome', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.01, 0.43, 'Good Away', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.89, 0.46, 'Good atHome', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.89, 0.43, 'Good Away', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

plt.legend()

plt.show()

reversed_indices = np.arange(len(X))[::-1]  
reversed_X = X.flatten()[::-1]  
reversed_Y = Y[::-1]

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 8), facecolor='beige')
ax.set_facecolor('beige')

team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', 'Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd']

highest_home_GD = np.max(X)
lowest_home_GD = np.min(X)
highest_away_GD = np.max(Y)
lowest_away_GD = np.min(Y)

highest_home_GD_team_index = np.argmax(X)  
lowest_home_GD_team_index = np.argmin(X)   
highest_away_GD_team_index = np.argmax(Y)  
lowest_away_GD_team_index = np.argmin(Y) 

print(f"Highest Home GD: {highest_home_GD} by {team_names[highest_home_GD_team_index]}")
print(f"Lowest Home GD: {lowest_home_GD} by {team_names[lowest_home_GD_team_index]}")
print(f"Highest Away GD: {highest_away_GD} by {team_names[highest_away_GD_team_index]}")
print(f"Lowest Away GD: {lowest_away_GD} by {team_names[lowest_away_GD_team_index]}")

bar_height = 0.45 
indices = np.arange(len(X))  
reversed_indices = indices[::-1]

home_bars = ax.barh(reversed_indices + bar_height/2, X.flatten(), bar_height, label='Home Goal Difference', color='lightblue')
away_bars = ax.barh(reversed_indices - bar_height/2, Y, bar_height, label='Away Goal Difference', color='orange')

ax.set_ylabel(' Home Goal Difference')
ax.set_xlabel('Away Goal Difference')
ax.set_title('Comparison of Home Goal Difference vs Away Goal Difference')

ax.set_yticks(reversed_indices)  
ax.set_yticklabels(team_names)

ax.legend()

for bar in home_bars:
    width = bar.get_width()  
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

for bar in away_bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

plt.text(0.71, 0.17, 'Avg Home Goal Dif: 6.10', fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.71, 0.14, 'Avg Away Goal Dif: -6.10', fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

plt.text(0.71, 0.11, f"Highest Home GD: {highest_home_GD} by {team_names[highest_home_GD_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.71, 0.08, f"Lowest Home GD: {lowest_home_GD} by {team_names[lowest_home_GD_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.71, 0.05, f"Highest Away GD: {highest_away_GD} by {team_names[highest_away_GD_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.71, 0.02, f"Lowest Away GD: {lowest_away_GD} by {team_names[lowest_away_GD_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

plt.tight_layout()
plt.show()