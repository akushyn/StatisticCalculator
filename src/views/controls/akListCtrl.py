# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 16:50:19 2018

@author: Andriy
"""
import wx
from wx.lib.pubsub import pub
from src.controllers.akPubEvents import AkHistoricalDataEvents

class AkListCtrl(wx.ListCtrl):
    '''
    Custom List control.
    '''
    def __init__(self, *args, **kwargs):
        super(AkListCtrl, self).__init__(*args, **kwargs)
        self.__set_properties()
        
        pub.subscribe(self.ShowData, AkHistoricalDataEvents.LIST_DATA_CONTROL_CHANGING)
         
    def __set_properties(self):
        self.AppendColumn("Date", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.AppendColumn("Open", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.AppendColumn("High", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.AppendColumn("Low", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.AppendColumn("Close", format=wx.LIST_FORMAT_LEFT, width=-1)

    def ShowData(self, data):
        print("Pub handler 'OnListDataChanging' called!")
        # [Date, Open, High, Low, Close]
        if (data):
            self.DeleteAllItems()
            for i in range(len(data)):
                self.InsertItem(i, data[i][0])
                self.SetItem(i, 1, data[i][1])
                self.SetItem(i, 2, data[i][2])            
                self.SetItem(i, 3, data[i][3])
                self.SetItem(i, 4, data[i][4])
