# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:06:22 2018

@author: Andriy
"""
import wx
import csv as csv
from src.views.akHistoricalDataManagerView import AkHistoricalDataManagerView
from src.models.akHistoricalDataManagerModel import AkHistoricalDataManagerModel

class AkHistoricalDataManagerController:
    def __init__(self):
        self.model = AkHistoricalDataManagerModel()
        self.view = AkHistoricalDataManagerView(None)
        
        self.view.Bind(wx.EVT_BUTTON, self.onImportCSVHandler, self.view.btn_Import)  

    def onImportCSVHandler(self, event):
        print("Event handler 'onImportCSVHandler' not implemented!")
        csvData = []
        with wx.FileDialog(self.view, "Open XYZ file", wildcard="CSV files (*.csv)|*.csv", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            pathname = fileDialog.GetPath()
            #fileName = fileDialog.GetFilename()
            try:
                with open(pathname, 'r') as file:
                    data = csv.reader(file)
                    
                    for row in data:
                        csvData.append(row)
                        print(row)
            except IOError:
                print("Error!")
