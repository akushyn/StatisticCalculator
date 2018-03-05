# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:00:38 2018

@author: Andriy
"""

import wx
from src.views.controls.akCheckedInstrumentListBox import AkCheckedInstrumentListBox

instrumentData = [("EURUSD", "Euro FX"), ("GBPUSD", "British Pound"), ("GC", "COMEX Gold Futures"), ("CL", "Crude Oil Futures"), ("SP500", "S&P 500"), ("AUDUSD", "Australian Dollar"), ("EURJPY", "Euro vs Japanese Yen"), ("USDJPY", "Japanese Yen"), ("BTCUSD", "Bit coin"), ("LTCUSD", "Light coin")]
packages = [('abiword', '5.8M', 'base'), ('adie', '145k', 'base'),
    ('airsnort', '71k', 'base'), ('ara', '717k', 'base'), ('arc', '139k', 'base'),
    ('asc', '5.8M', 'base'), ('ascii', '74k', 'base'), ('ash', '74k', 'base')]


class AkInstrumentManagerView(wx.Dialog):
    def __init__(self, *args, **kwds):
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((515, 430))
        self.cb_WatchList = wx.ComboBox(self, wx.ID_ANY, choices=["Default"], style=wx.CB_DROPDOWN)
        self.lst_WatchInstruments = wx.ListBox(self, wx.ID_ANY, choices=[])
        self.btnNew = wx.Button(self, wx.ID_ANY, "New")
        self.btnDelete = wx.Button(self, wx.ID_ANY, "Delete")
        self.text_Name = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_Description = wx.TextCtrl(self, wx.ID_ANY, "")
        self.btnSearch = wx.Button(self, wx.ID_ANY, "Search")
        self.btnSelectAll = wx.Button(self, wx.ID_ANY, "Select All")
        self.btnDeselectAll = wx.Button(self, wx.ID_ANY, "Deselect All")
        self.btn_Insert = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/icons/add.ico", wx.BITMAP_TYPE_ANY))
        self.btn_Remove = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/icons/delete.ico", wx.BITMAP_TYPE_ANY))        
        self.initCheckInstrumentListBox()
        self.btnOK = wx.Button(self, wx.ID_ANY, "OK")
        self.btnCancel = wx.Button(self, wx.ID_ANY, "Cancel")

        self.__set_properties()
        self.__do_layout()

        #self.checkedWatchList = []

    def __set_properties(self):
        self.SetTitle("Instrument Manager")
        self.cb_WatchList.SetSelection(0)
        self.btnNew.SetMinSize((60, 26))
        self.btnDelete.SetMinSize((60, 26))
        self.text_Name.SetMinSize((70, 23))
        self.text_Description.SetMinSize((120, 23))
        self.btnSearch.SetMinSize((80, 23))
        self.btnSelectAll.SetMinSize((70, 26))
        self.btnDeselectAll.SetMinSize((70, 26))
        self.btn_Insert.SetMinSize((25, 25))
        self.btn_Remove.SetMinSize((25, 25))

    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        vBox_Save = wx.BoxSizer(wx.HORIZONTAL)
        hBox_Left = wx.BoxSizer(wx.HORIZONTAL)
        vBox_Instruments = wx.BoxSizer(wx.VERTICAL)
        hBox_Instruments = wx.BoxSizer(wx.HORIZONTAL)
        vBox_Buttons = wx.BoxSizer(wx.VERTICAL)
        hBox_Search = wx.BoxSizer(wx.HORIZONTAL)
        grid_Inputs = wx.FlexGridSizer(2, 3, 0, 0)
        vBox_WatchList = wx.BoxSizer(wx.VERTICAL)
        hBox_ListButtons = wx.BoxSizer(wx.HORIZONTAL)
        lblInstuments = wx.StaticText(self, wx.ID_ANY, "Instrument lists:")
        vBox_WatchList.Add(lblInstuments, 0, wx.TOP, 5)
        vBox_WatchList.Add(self.cb_WatchList, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 5)
        vBox_WatchList.Add(self.lst_WatchInstruments, 1, wx.EXPAND, 0)
        hBox_ListButtons.Add(self.btnNew, 0, wx.LEFT | wx.RIGHT, 5)
        hBox_ListButtons.Add(self.btnDelete, 0, wx.LEFT | wx.RIGHT, 5)
        vBox_WatchList.Add(hBox_ListButtons, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        hBox_Left.Add(vBox_WatchList, 0, wx.ALL | wx.EXPAND, 10)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        hBox_Left.Add(static_line_1, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 10)
        lblCaption = wx.StaticText(self, wx.ID_ANY, "Available master instruments")
        vBox_Instruments.Add(lblCaption, 0, 0, 0)
        lblName = wx.StaticText(self, wx.ID_ANY, "Name")
        grid_Inputs.Add(lblName, 0, 0, 0)
        lblDescription = wx.StaticText(self, wx.ID_ANY, "Description")
        grid_Inputs.Add(lblDescription, 0, wx.LEFT, 10)
        grid_Inputs.Add((0, 0), 0, 0, 0)
        grid_Inputs.Add(self.text_Name, 0, 0, 0)
        grid_Inputs.Add(self.text_Description, 0, wx.LEFT, 10)
        grid_Inputs.Add(self.btnSearch, 0, wx.LEFT, 20)
        hBox_Search.Add(grid_Inputs, 0, wx.EXPAND, 0)
        vBox_Instruments.Add(hBox_Search, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 15)
        vBox_Buttons.Add(self.btnSelectAll, 0, wx.ALIGN_CENTER | wx.BOTTOM, 5)
        vBox_Buttons.Add(self.btnDeselectAll, 0, wx.ALIGN_CENTER, 0)
        vBox_Buttons.Add((20, 20), 1, wx.EXPAND, 0)
        vBox_Buttons.Add(self.btn_Insert, 0, 0, 0)
        vBox_Buttons.Add(self.btn_Remove, 0, 0, 0)
        hBox_Instruments.Add(vBox_Buttons, 0, wx.EXPAND | wx.RIGHT, 10)
        hBox_Instruments.Add(self.lst_CheckedInstrumentList, 1, wx.EXPAND, 0)
        vBox_Instruments.Add(hBox_Instruments, 1, wx.EXPAND, 0)
        hBox_Left.Add(vBox_Instruments, 4, wx.ALL | wx.EXPAND, 10)
        sizer.Add(hBox_Left, 1, wx.EXPAND, 0)
        static_line_2 = wx.StaticLine(self, wx.ID_ANY)
        sizer.Add(static_line_2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        vBox_Save.Add(self.btnOK, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 40)
        vBox_Save.Add(self.btnCancel, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 40)
        sizer.Add(vBox_Save, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.TOP, 15)
        self.SetSizer(sizer)
        self.Layout()

    def initCheckInstrumentListBox(self):
        self.lst_CheckedInstrumentList = AkCheckedInstrumentListBox(self)
        
        self.lst_CheckedInstrumentList.InsertColumn(0, "Name")
        self.lst_CheckedInstrumentList.InsertColumn(1, "Description")

        for i in range(len(instrumentData)):
            self.lst_CheckedInstrumentList.InsertItem(i, instrumentData[i][0])
            self.lst_CheckedInstrumentList.SetItem(i, 1, instrumentData[i][1])



