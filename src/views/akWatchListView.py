# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:24:19 2018

@author: Andriy
"""
import wx

class AkWatchListView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
    
        self._comboboxList = wx.ComboBox(self, wx.ID_ANY, choices=["Default"], style=wx.CB_DROPDOWN)
        self.watchListInstruments = wx.ListBox(self, wx.ID_ANY, choices=[])
        self.btnNew = wx.Button(self, wx.ID_ANY, "New")
        self.btnDelete = wx.Button(self, wx.ID_ANY, "Delete")
        
        self.__set_properties()
        self.__do_layout()
        
    def __set_properties(self):
        self._comboboxList.SetSelection(0)
        self.btnNew.SetMinSize((60, 26))
        self.btnDelete.SetMinSize((60, 26))
        
    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        hBox_Buttons = wx.BoxSizer(wx.HORIZONTAL)
        lblInstuments = wx.StaticText(self, wx.ID_ANY, "Instrument lists:")
        sizer.Add(lblInstuments, 0, wx.TOP, 5)
        sizer.Add(self._comboboxList, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 5)
        sizer.Add(self.watchListInstruments, 1, wx.EXPAND, 0)
        hBox_Buttons.Add(self.btnNew, 0, wx.LEFT | wx.RIGHT, 5)
        hBox_Buttons.Add(self.btnDelete, 0, wx.LEFT | wx.RIGHT, 5)
        sizer.Add(hBox_Buttons, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        
        self.SetSizer(sizer)
        self.Layout()
