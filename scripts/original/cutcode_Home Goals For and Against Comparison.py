# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:04:16 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import xlrd

book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")
sheet = book.sheet_by_name('Sheet8')

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

print(f"Average of X (Home Goals For): {X_avg:.2f}")
print(f"Average of Y (Home Goals Against): {Y_avg:.2f}")

fig, ax = plt.subplots(figsize=(12, 6), facecolor='Beige')
ax.set_facecolor('beige')
plt.scatter(X, Y, color='red', s=1, label =' Teams')

ax.spines['top'].set_visible(True)  
ax.spines['right'].set_visible(True)

ax.spines['top'].set_color('Green')  
ax.spines['top'].set_linewidth(2)

ax.spines['right'].set_color('Green')  
ax.spines['right'].set_linewidth(2)

ax.spines['top'].set_position(('outward', Y_avg * -8.0))  
ax.spines['right'].set_position(('outward', X_avg * -10.3))

plt.xlabel(' Home Goals For')
plt.ylabel(' Home Goals Against')
plt.title('Comparison of Home Goals For vs Home Goals Against')
for i in range(len(X)):
    img = mpimg.imread(image_paths[i])  
    imagebox = OffsetImage(img, zoom=0.5)  
    ab = AnnotationBbox(imagebox, (X[i], Y[i]), frameon=False, xycoords='data', boxcoords="data")
    plt.gca().add_artist(ab) 

# Add Premier League logo to the top-right corner
Logo_image_path = 'images/PL_Logo.png'  
Logo_img = mpimg.imread(Logo_image_path)  # Load the Premier League logo
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo

# Place the Premier League logo at a fixed position (top-right corner)
ab_Logo = AnnotationBbox(Logo_imagebox, (0.95, 0.83), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)

plt.text(0.89, 0.27, 'Good Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.89, 0.24, 'Good Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.48, 0.02, f"Avg Goals For: {X_avg:.2f}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.01, 0.05, 'Bad Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.01, 0.02, 'Good Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.01, 0.30, f"Avg Goals Against: {Y_avg:.2f}",fontsize=10, color='black', ha='left', va='top', transform=plt.gca().transAxes)
plt.text(0.01, 0.36, 'Bad Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.01, 0.33, 'Bad Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.89, 0.36, 'Good Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.89, 0.33, 'Bad Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

plt.legend()

plt.show()

reversed_indices = np.arange(len(X))[::-1]  
reversed_X = X.flatten()[::-1]  
reversed_Y = Y[::-1]

fig, ax = plt.subplots(figsize=(14, 8), facecolor='beige')
ax.set_facecolor('beige')

team_names = [
    'Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 
    'Newcastle Utd', 'Manchester Utd', 'West Ham', 'Crystal Palace', 'Bournemouth', 
    'Brighton', 'Everton', 'Fulham', 'Wolves', 'Brentford', 'Nottingham Forest', 
    'Luton Town', 'Burnley', 'Sheffield Utd']

highest_GFor = np.max(X)
lowest_GFor = np.min(X)
highest_GAgainst = np.max(Y)
lowest_GAgainst = np.min(Y)

highest_GFor_team_index = np.argmax(X)  
lowest_GFor_team_index = np.argmin(X)   
highest_GAgainst_team_index = np.argmax(Y)  
lowest_GAgainst_team_index = np.argmin(Y) 

print(f"Highest Home Goals For: {highest_GFor} by {team_names[highest_GFor_team_index]}")
print(f"Lowest Home Goals For: {lowest_GFor} by {team_names[lowest_GFor_team_index]}")
print(f"Highest Home Goals Against: {highest_GAgainst} by {team_names[highest_GAgainst_team_index]}")
print(f"Lowest Home Goals Against: {lowest_GAgainst} by {team_names[lowest_GAgainst_team_index]}") 

bar_height = 0.45 
indices = np.arange(len(X))  
reversed_indices = indices[::-1]

GFor_bars = ax.barh(reversed_indices + bar_height/2, X.flatten(), bar_height, label='Home Goals For', color='lightblue')
GAgainst_bars = ax.barh(reversed_indices - bar_height/2, Y, bar_height, label='Home Goals Against', color='orange')

ax.set_ylabel(' Teams')
ax.set_xlabel(' Goals For/Against')
ax.set_title('Comparison of Home Goals For vs Home Goals Against')

ax.set_yticks(reversed_indices)  
ax.set_yticklabels(team_names)

ax.legend()

for bar in GFor_bars:
    width = bar.get_width()  
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

for bar in GAgainst_bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=11, color='black')

# Load the Premier League logo and add it to the plot
Logo_image_path = 'images/PL_Logo.png'  
Logo_img = mpimg.imread(Logo_image_path)  # Load the image
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)  # Resize the logo

# Position the logo at a fixed location in the plot (bottom-left corner)
ab_Logo = AnnotationBbox(Logo_imagebox, (-0.10, -0.01), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)  # Add the logo to the plot

plt.text(0.65, 0.40, f"Avg Home Goals For: {X_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.65, 0.37, f"Avg Home Goals Against: {Y_avg:.2f}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

plt.text(0.65, 0.34, f"Highest Home Goals For: {highest_GFor} by {team_names[highest_GFor_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.65, 0.31, f"Lowest Home Goals For: {lowest_GFor} by {team_names[lowest_GFor_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.65, 0.28, f"Highest Home Goals Against: {highest_GAgainst} by {team_names[highest_GAgainst_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.65, 0.25, f"Lowest Home Goals Against: {lowest_GAgainst} by {team_names[lowest_GAgainst_team_index]}", fontsize=11, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

plt.tight_layout()
plt.show()