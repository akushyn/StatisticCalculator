# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:31:31 2018

@author: Andriy
"""
import wx
from src.views.akInstrumentManagerView import AkInstrumentManagerView
from src.models.akInstrumentManagerModel import AkInstrumentManagerModel

class AkInstrumentManagerController:
    def __init__(self):
        self.model = AkInstrumentManagerModel()
        self.view = AkInstrumentManagerView(None)
        
        self.view.Bind(wx.EVT_BUTTON, self.onSaveAndApply_btnClick_Handler, self.view.btnOK)
        self.view.Bind(wx.EVT_BUTTON, self.onCancel_btnClick_Handler, self.view.btnCancel)        


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

