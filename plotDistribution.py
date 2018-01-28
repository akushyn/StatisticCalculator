# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:27:27 2018

@author: Andriy
"""
import distribution as distr
import matplotlib.pyplot as plt

'''
plt.figure()
plt.title(distr.header[0])
plt.hist(distr.highLow, bins=20)

plt.figure()
plt.title(distr.header[1])
plt.hist(distr.openHigh, bins='auto')

plt.figure()
plt.title(distr.header[2])
plt.hist(distr.openLow, bins='auto')

plt.figure()
plt.title(distr.header[3])
plt.hist(distr.highClose, bins='auto')

plt.figure()
plt.title(distr.header[4])
plt.hist(distr.lowClose, bins='auto')

'''

# cycle on distributions and plot 
for i in range(len(distr.distributions)):
    plt.figure()
    plt.title(distr.header[i])
    plt.hist(distr.distributions[i], bins=20)
