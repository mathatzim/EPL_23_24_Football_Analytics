# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 02:08:27 2024

@author: mathaios
"""
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

import xlrd

book = xlrd.open_workbook("EPL Home Away xG xGA 23_24.xls")
sheet = book.sheet_by_name('Sheet4')

X = np.array(sheet.col_values(0)).reshape(-1,1)
Y = np.array(sheet.col_values(1))

print(X)
print(Y)

plt.scatter(X, Y, color='blue', label='Data points')