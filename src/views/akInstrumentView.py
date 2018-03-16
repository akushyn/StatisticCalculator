# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:00:38 2018

@author: Andriy
"""

import wx
from src.views.controls.akCheckedInstrumentListBox import AkCheckedInstrumentListBox
from src.views.akWatchListView import AkWatchListView
from src.views.akCheckedListView import AkCheckedListView
from src.views.akSearchView import AkSearchView

instrumentData = [("EURUSD", "Euro FX"), ("GBPUSD", "British Pound"), ("GC", "COMEX Gold Futures"), ("CL", "Crude Oil Futures"), ("SP500", "S&P 500"), ("AUDUSD", "Australian Dollar"), ("EURJPY", "Euro vs Japanese Yen"), ("USDJPY", "Japanese Yen"), ("BTCUSD", "Bit coin"), ("LTCUSD", "Light coin")]

class AkInstrumentView(wx.Dialog):
    def __init__(self, parent, controller):
        style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        super(AkInstrumentView, self).__init__(parent, style=style)
        self.SetInitialSize((515, 430))
        
        self.controller = controller
        self.controller.Register(self)
        
        self.watchListView = AkWatchListView(self)
        self.searchView = AkSearchView(self)
        self.checkedListView = AkCheckedListView(self)
        
        self.btnOK = wx.Button(self, wx.ID_ANY, "OK")
        self.btnCancel = wx.Button(self, wx.ID_ANY, "Cancel")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onSaveAndApply_btnClick_Handler, self.btnOK)
        self.Bind(wx.EVT_BUTTON, self.onCancel_btnClick_Handler, self.btnCancel)        


    def __set_properties(self):
        self.SetTitle("Instrument Manager")


    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        vBox_Save = wx.BoxSizer(wx.HORIZONTAL)
        hBox_Left = wx.BoxSizer(wx.HORIZONTAL)
        vBox_Instruments = wx.BoxSizer(wx.VERTICAL)

        hBox_Left.Add(self.watchListView, 0, wx.ALL | wx.EXPAND, 10)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        hBox_Left.Add(static_line_1, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 10)

        lblCaption = wx.StaticText(self, wx.ID_ANY, "Available master instruments")
        vBox_Instruments.Add(lblCaption, 0, 0, 0)
        
        vBox_Instruments.Add(self.searchView, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 15)
        vBox_Instruments.Add(self.checkedListView, 1, wx.EXPAND, 0)
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
        self.checkedInstrumentsList = AkCheckedInstrumentListBox(self)
        
        self.checkedInstrumentsList.InsertColumn(0, "Name")
        self.checkedInstrumentsList.InsertColumn(1, "Description")

        for i in range(len(instrumentData)):
            self.checkedInstrumentsList.InsertItem(i, instrumentData[i][0])
            self.checkedInstrumentsList.SetItem(i, 1, instrumentData[i][1])

    def GetWatchListObject(self):
        return self._comboboxList
    
    def AddWatchList(self, name):
        if (name == ""):
            return
    
        if (name == "Default"):
            dlg = wx.MessageDialog(self.view, "Default watch list is already defined", "Notification", wx.OK | wx.ICON_ERROR)
            if (dlg.ShowModal() == wx.ID_OK):
                dlg.Destroy()
                return            
        self._comboboxList.Append(name)

    def DeleteSelectedWatchList(self):
        sel = self.GetSelectedWatchListIndex()
        
        if (sel == 0):  #"Default" watch list 
            delDefault = wx.MessageDialog(self, "Default watch list can't be deleted.", "Notification", wx.OK | wx.ICON_ERROR)
            if (delDefault.ShowModal() == wx.ID_OK):
                delDefault.Destroy()
                return

        if (sel != -1):
            self._comboboxList.Delete(sel)
            self._comboboxList.SetSelection(0)            
            
    def GetSelectedWatchList(self):
        return self._comboboxList.GetStringSelection()

    def GetSelectedWatchListIndex(self):
        return self._comboboxList.GetSelection()
        
    def RemoveItem(self):
        self.watchListInstruments
    
    def onInsertItems_btnClick_Handler(self, event):  
        checkedList = []

        num = self.view.checkedInstrumentsList.GetItemCount()
        if (num < 1 ):
            return
        
        for i in range(num):
            if (self.view.checkedInstrumentsList.IsChecked(i)):
                value = self.view.checkedInstrumentsList.GetItemText(i)
                checkedList.append(value + '\n')
             
        self.view.watchListInstruments.Items = checkedList

        index = self.view.GetSelectedWatchListIndex()
        self.model.InsertWatchListData(index, checkedList)        

    def onSearchInstrument_btnClick_Handler(self, event):  
        "Search instrument by 'Name' or by 'Description'"
        
        print("Event handler 'onSearchInstrument_btnClick_Handler' not implemented!")
        event.Skip()

    def onSelectAllInstruments_btnClick_Handler(self, event): 
        "Select all instruments in the checkedInstrumentsList"
        num = self.view.checkedInstrumentsList.GetItemCount()
        for i in range(num):
            self.view.checkedInstrumentsList.CheckItem(i)        

    def onDeselectAllInstruments_btnClick_Handler(self, event):  
        num = self.view.checkedInstrumentsList.GetItemCount()
        for i in range(num):
            self.view.checkedInstrumentsList.CheckItem(i, False) 


    def onSaveAndApply_btnClick_Handler(self, event): 
        print("Event handler 'onSaveAndApply_btnClick_Handler' not implemented!")
        event.Skip()

    def onCancel_btnClick_Handler(self, event): 
        self.view.Close()

    