# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:56:41 2018

@author: Andriy
"""

import tkinter.filedialog as fileDialog
import src.distribution as distr
import src.loadCSVFile as csv
import matplotlib.pyplot as plt

fileName = ''
csvData = []
distributions = []

def loadCSVFile():
    print('mainGUI_support.loadCSVFiles')
    #sys.stdout.flush()

    global fileName, csvData
    fileName = fileDialog.Open(root, filetypes = [('*.csv files', '.csv')]).show()
    if fileName == '':
        return

    csvData = csv.readDataFromFile(fileName)
    #print(DataFrame(csvData))


def SaveFile(ev):
    fileName = fileDialog.SaveAs(root, filetypes = [('*.csv files', '.csv')]).show()
    if fileName == '':
        return
    if not fileName.endswith(".csv"):
        fileName+=".csv"
    #open(fn, 'wt').write(textbox.get('1.0', 'end'))

def calculate():
    print('mainGUI_support.calculate')

    global csvData
    if len(csvData) == 0:
        return

    distributions = distr.getDistributionList()
    plotDistributions(distributions)

def plotDistributions(distrList):

    #draw in console
    for i in range(len(distrList)):
        plt.figure()
        plt.title(distr.shortNames[i])
        plt.hist(distr.distributions[i], bins=20)


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import mainGUI
    mainGUI.vp_start_gui()

