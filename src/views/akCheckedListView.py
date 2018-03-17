# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:56:31 2018

@author: Andriy
"""
import wx
from src.views.controls.akCheckedInstrumentListBox import AkCheckedInstrumentListBox

instrumentData = [("EURUSD", "Euro FX"), ("GBPUSD", "British Pound"), ("GC", "COMEX Gold Futures"), ("CL", "Crude Oil Futures"), ("SP500", "S&P 500"), ("AUDUSD", "Australian Dollar"), ("EURJPY", "Euro vs Japanese Yen"), ("USDJPY", "Japanese Yen"), ("BTCUSD", "Bit coin"), ("LTCUSD", "Light coin")]

class AkCheckedListView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        self.btnSelectAll = wx.Button(self, wx.ID_ANY, "Select All")
        self.btnDeselectAll = wx.Button(self, wx.ID_ANY, "Deselect All")
        self.btn_Insert = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("icons/add.ico", wx.BITMAP_TYPE_ANY))
        self.btn_Remove = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("icons/delete.ico", wx.BITMAP_TYPE_ANY))        
        
        self.checkedInstrumentsList = AkCheckedInstrumentListBox(self)
        
        self.checkedInstrumentsList.InsertColumn(0, "Name")
        self.checkedInstrumentsList.InsertColumn(1, "Description")

        for i in range(len(instrumentData)):
            self.checkedInstrumentsList.InsertItem(i, instrumentData[i][0])
            self.checkedInstrumentsList.SetItem(i, 1, instrumentData[i][1])
        
        self.__set_properties()
        self.__do_layout()
        
    def __set_properties(self):
        self.btnSelectAll.SetMinSize((70, 26))
        self.btnDeselectAll.SetMinSize((70, 26))
        self.btn_Insert.SetMinSize((25, 25))
        self.btn_Remove.SetMinSize((25, 25))
        
    def __do_layout(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        vBox_Buttons = wx.BoxSizer(wx.VERTICAL)
        vBox_Buttons.Add(self.btnSelectAll, 0, wx.ALIGN_CENTER | wx.BOTTOM, 5)
        vBox_Buttons.Add(self.btnDeselectAll, 0, wx.ALIGN_CENTER, 0)
        vBox_Buttons.Add((20, 20), 1, wx.EXPAND, 0)
        vBox_Buttons.Add(self.btn_Insert, 0, 0, 0)
        vBox_Buttons.Add(self.btn_Remove, 0, 0, 0)
        
        sizer.Add(vBox_Buttons, 0, wx.EXPAND | wx.RIGHT, 10)
        sizer.Add(self.checkedInstrumentsList, 1, wx.EXPAND, 0)

        self.SetSizer(sizer)
        self.Layout()
        
        