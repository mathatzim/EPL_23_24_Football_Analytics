# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 14:44:01 2025

@author: mathaios
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

import xlrd

book = xlrd.open_workbook("EPL_Home_Away_xG_xGA 23_24.xls")
sheet = book.sheet_by_name('Sheet6')

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

print(f"Average of X (Home Expected Goals For): {X_avg:.2f}")
print(f"Average of Y (Home Expected Goals Against): {Y_avg:.2f}")

fig, ax = plt.subplots(figsize=(12, 6), facecolor='beige')
ax.set_facecolor('beige')
plt.scatter(X, Y, color='red', s=1, label =' Teams')

ax.spines['top'].set_visible(True)  
ax.spines['right'].set_visible(True)

ax.spines['top'].set_color('Green')  
ax.spines['top'].set_linewidth(2)

ax.spines['right'].set_color('Green')  
ax.spines['right'].set_linewidth(2)

ax.spines['top'].set_position(('outward', Y_avg * -6.5))  
ax.spines['right'].set_position(('outward', X_avg * -13.3))

plt.xlabel(' Home Expected Goals For')
plt.ylabel(' Home Expected Goals Against')
plt.title('Comparison of Home Expected Goals For vs Home Expected Goals Against')
for i in range(len(X)):
    img = mpimg.imread(image_paths[i])  
    imagebox = OffsetImage(img, zoom=0.5)  
    ab = AnnotationBbox(imagebox, (X[i], Y[i]), frameon=False, xycoords='data', boxcoords="data")
    plt.gca().add_artist(ab) 

Logo_image_path = 'images/PL_Logo.png'  
Logo_img = mpimg.imread(Logo_image_path)
Logo_imagebox = OffsetImage(Logo_img, zoom=0.2)

ab_Logo = AnnotationBbox(Logo_imagebox, (0.95, 0.83), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab_Logo)

plt.text(0.88, 0.05, 'Good Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.88, 0.02, 'Good Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.35, 0.02, f"Avg xG For: {X_avg:.2f}", fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.02, 0.05, 'Bad Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.02, 0.02, 'Good Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.83, 0.47, f"Avg xG Against: {Y_avg:.2f}",fontsize=10, color='black', ha='left', va='top', transform=plt.gca().transAxes)
plt.text(0.02, 0.53, 'Bad Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.02, 0.50, 'Bad Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.88, 0.53, 'Good Offense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)
plt.text(0.88, 0.50, 'Bad Defense', fontsize=10, color='black', ha='left', va='bottom', transform=plt.gca().transAxes)

plt.legend()

plt.show()

