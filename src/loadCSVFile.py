# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:12:12 2018

@author: Andriy
"""
import csv as csv

# all data from file [Date, Open, High, Low, Close]
csvData = []

def readDataFromFile(fileName):
    readData = csv.reader(open(fileName, 'r'))
    #read data from csv to the data object
    global csvData, data, header
    
    for row in readData:
        csvData.append(row)
    
    #remove volume column
    for row in csvData:
        del row[5]
    
    return csvData
