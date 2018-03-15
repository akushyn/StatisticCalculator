# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 19:27:27 2018

@author: Andriy
"""

import wx
import csv as csv
import wx.lib.pubsub.setupkwargs
from wx.lib.pubsub import pub
from src.controllers.akPubEvents import AkPubEvents

class AkImportView(wx.Panel):
    def __init__(self, parent, controller):
        super(AkImportView, self).__init__(parent)
        
        self.controller = controller
        
        self.cb_Format = wx.ComboBox(self, wx.ID_ANY, choices=["Trade Workstation", "Metatrader 4"], style=wx.CB_DROPDOWN)
        self.cb_TimeZone = wx.ComboBox(self, wx.ID_ANY, choices=["UTC"], style=wx.CB_DROPDOWN)
        self.btn_Import = wx.Button(self, wx.ID_ANY, "Start Import")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onImportCSV_btnClick_Handler, self.btn_Import)  

    def __set_properties(self):
        self.cb_Format.SetSelection(0)
        self.cb_TimeZone.SetSelection(0)

    
    def __do_layout(self):
        
        vBox_Labels = wx.BoxSizer(wx.VERTICAL)
        lblInpurFormat = wx.StaticText(self, wx.ID_ANY, "Data Input Format")
        vBox_Labels.Add(lblInpurFormat, 0, wx.ALL, 20)
        lblTimeZone = wx.StaticText(self, wx.ID_ANY, "Time zone of imported data:")
        vBox_Labels.Add(lblTimeZone, 0, wx.ALL, 20)
        
        vBox_Inputs = wx.BoxSizer(wx.VERTICAL)
        vBox_Inputs.Add(self.cb_Format, 0, wx.ALL | wx.EXPAND, 15)
        vBox_Inputs.Add(self.cb_TimeZone, 0, wx.ALL | wx.EXPAND, 15)
        vBox_Inputs.Add(self.btn_Import, 0, wx.ALL, 15)
        
        sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizer.Add(vBox_Labels, 1, wx.EXPAND, 0)
        sizer.Add(vBox_Inputs, 2, wx.EXPAND, 0)
        
        self.SetSizer(sizer)
        self.Layout()        
        
    def onImportCSV_btnClick_Handler(self, event):
        print("Event handler 'onImportCSVHandler' not implemented!")

        #csvData = []
        fileDialog = wx.FileDialog(self, "Open XYZ file", wildcard="CSV files (*.csv)|*.csv", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return     

        pathname = fileDialog.GetPath()
        try:
            with open(pathname, 'r') as file:
                csvData = csv.reader(file)    
                
                data = []
                for row in csvData:
                    data.append(row)
                    
                # send message to controller to change model data
                pub.sendMessage(AkPubEvents.IMPORTED_DATA_CHANGING, name=fileDialog.GetFilename(), data=data, headers=data.pop(0))
                
        except IOError:
            print("Error!")
        fileDialog.Destroy()