# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:31:31 2018

@author: Andriy
"""
import wx
from src.views.akInstrumentManagerView import AkInstrumentManagerView
from src.models.akInstrumentManagerModel import AkInstrumentManagerModel
from src.controllers.akWatchListNameController import AkWatchListNameController

class AkInstrumentManagerController:
    def __init__(self):
        self.model = AkInstrumentManagerModel()
        self.view = AkInstrumentManagerView(None)
        
        self.view.Bind(wx.EVT_BUTTON, self.onNewWatchListHandler, self.view.btnNew)
        self.view.Bind(wx.EVT_BUTTON, self.onDeleteWatchListHandler, self.view.btnDelete)
        self.view.Bind(wx.EVT_BUTTON, self.onSearchInstrumentHandler, self.view.btnSearch)
        self.view.Bind(wx.EVT_BUTTON, self.onSelectAllInstrumentsHandler, self.view.btnSelectAll)
        self.view.Bind(wx.EVT_BUTTON, self.onDeselectAllInstrumentsHandler, self.view.btnDeselectAll)
        self.view.Bind(wx.EVT_BUTTON, self.onInsertSelectedToWatchListHandler, self.view.btn_Insert)
        self.view.Bind(wx.EVT_BUTTON, self.onRemoveWatchListItemHandler, self.view.btn_Remove)
        self.view.Bind(wx.EVT_BUTTON, self.onSaveAndApplyHandler, self.view.btnOK)
        self.view.Bind(wx.EVT_BUTTON, self.onCancelHandler, self.view.btnCancel)        
        self.view.Bind(wx.EVT_COMBOBOX, self.onWatchListChangedHandler, self.view.cb_WatchList)

    def onWatchListChangedHandler(self, event):
        index = self.view.cb_WatchList.GetSelection()
        self.view.lst_WatchInstruments.Items = self.model.checkedWatchList[index]
        
    def onNewWatchListHandler(self, event): 
        controller = AkWatchListNameController()        
        with controller.view as listNameview:
            listNameview.ShowModal()
            
            self.view.cb_WatchList.Append(listNameview.text_Name.GetValue())            
            self.model.checkedWatchList.append([])


    def onDeleteWatchListHandler(self, event): 
        selection = self.view.cb_WatchList.GetSelection()
        dlg = wx.MessageDialog(self.view, "Delete " + self.view.cb_WatchList.GetStringSelection() + " watchlist?", "Confirmation", wx.YES_NO | wx.ICON_ASTERISK)
        if (dlg.ShowModal() == wx.ID_YES):
            if (selection == 0):  #"Default" watch list 
                deleteDefault = wx.MessageDialog(self.view, "Default watch list can't be deleted.", "Notification", wx.OK | wx.ICON_ERROR)
                if (deleteDefault.ShowModal() == wx.ID_OK):
                    deleteDefault.Destroy()
                    return
            if (selection != -1):
                self.view.cb_WatchList.Delete(selection)
                self.view.cb_WatchList.SetSelection(0)
                del self.model.checkedWatchList[selection]
                self.onWatchListChangedHandler(event)
            
        dlg.Destroy()

    def onRemoveWatchListItemHandler(self, event):  
        comboIdx = self.view.cb_WatchList.GetSelection()
        listIdx = self.view.lst_WatchInstruments.GetSelection()

        if (listIdx != -1):
            self.view.lst_WatchInstruments.Delete(listIdx)
            del self.model.checkedWatchList[comboIdx][listIdx]
        
            if (listIdx > 0):
                self.view.lst_WatchInstruments.SetSelection(listIdx - 1)

    def onSearchInstrumentHandler(self, event):  
        "Search instrument by 'Name' or by 'Description'"
        
        print("Event handler 'onSearchInstrumentHandler' not implemented!")
        event.Skip()

    def onSelectAllInstrumentsHandler(self, event): 
        "Select all instruments in the lst_CheckedInstrumentList"
        num = self.view.lst_CheckedInstrumentList.GetItemCount()
        for i in range(num):
            self.view.lst_CheckedInstrumentList.CheckItem(i)        

    def onDeselectAllInstrumentsHandler(self, event):  
        num = self.view.lst_CheckedInstrumentList.GetItemCount()
        for i in range(num):
            self.view.lst_CheckedInstrumentList.CheckItem(i, False) 

    def onInsertSelectedToWatchListHandler(self, event):  
        checkedList = []

        num = self.view.lst_CheckedInstrumentList.GetItemCount()
        if (num < 1 ):
            return
        
        for i in range(num):
            if (self.view.lst_CheckedInstrumentList.IsChecked(i)):
                value = self.view.lst_CheckedInstrumentList.GetItemText(i)
                checkedList.append(value + '\n')
             
        self.view.lst_WatchInstruments.Items = checkedList

        index = self.view.cb_WatchList.GetSelection()
        self.model.checkedWatchList.insert(index, checkedList)        

    def onSaveAndApplyHandler(self, event): 
        print("Event handler 'onSaveAndApplyHandler' not implemented!")
        event.Skip()

    def onCancelHandler(self, event): 
        self.view.Close()

