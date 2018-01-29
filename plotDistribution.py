# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:27:27 2018

@author: Andriy
"""
import src.calc.distribution as distr
import matplotlib.pyplot as plt

# cycle on distributions and plot 
for i in range(len(distr.distributions)):
    plt.figure()
    plt.title(distr.titles[i])
    plt.hist(distr.distributions[i], bins=20)

# add code here to configure histogramm