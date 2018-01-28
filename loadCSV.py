# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:12:12 2018

@author: Andriy
"""
import numpy as np
import csv as csv
import pandas as pd

readdata = csv.reader(open('E:\GoogleDrive\Торгівля\Торгова Система\dimahao\Statistics\^spx_y.csv', 'r'))

#read data from csv to the data object
data = []
for row in readdata:
    data.append(row)

#remove volume column
for row in data:
    del row[5]

# save header for future display
header = data[0]

# from now , data without header
data.pop(0)

# display data as a table
#print(pd.DataFrame(data, columns=header))

