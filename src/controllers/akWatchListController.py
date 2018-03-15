# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:47:23 2018

@author: Andriy
"""
from src.views.akWatchListView import AkWatchListView
from src.models.akWatchListModel import AkWatchListModel

class AkWatchListController:
    def __init__(self):
        self.watchListView = AkWatchListView(None)
        self.watchListModel = AkWatchListModel()

        self.view.Bind(wx.EVT_BUTTON, self.onAddWatchList_btnClick_Handler, self.view.btnNew)
        self.view.Bind(wx.EVT_BUTTON, self.onDeleteWatchList_btnClick_Handler, self.view.btnDelete)
        self.view.Bind(wx.EVT_COMBOBOX, self.onWatchList_comboboxChanged_Handler, self.view.GetWatchListObject())

        
    def onWatchList_comboboxChanged_Handler(self, event):
        source = self.model.GetItemsByIndex(self.view.GetSelectedWatchListIndex())
        self.view.watchListInstruments.Items = source
        
        
    def onAddWatchList_btnClick_Handler(self, event): 
        dialog = AkWatchListNameView(self.view, 'Enter the name of new watch list:','Watch list name')
        if (dialog.ShowModal() == wx.ID_OK):                
            self.view.AddWatchList(dialog.GetValue())
            self.model.AddWatchListData([]) # create new empty list of items 
        dialog.Destroy()

    def onDeleteWatchList_btnClick_Handler(self, event): 
        dlg = wx.MessageDialog(self.view, "Delete \'" + self.view.GetSelectedWatchList() + "\' watchlist?", "Confirmation", wx.YES_NO | wx.ICON_ASTERISK)
        if (dlg.ShowModal() == wx.ID_YES):
            self.view.DeleteSelectedWatchList()
            
            idx = self.view.GetSelectedWatchListIndex()
            self.model.DeleteWatchListData(idx)
            
            self.onWatchList_comboboxChanged_Handler(event)
        dlg.Destroy()

    def onDeleteItem_btnClick_Handler(self, event):  
        comboboxIndex = self.view.GetSelectedWatchListIndex()
        listIndex = self.view.watchListInstruments.GetSelection()

        if (listIndex != -1):
            self.view.watchListInstruments.Delete(listIndex)
            del self.model.checkedWatchList[comboboxIndex][listIndex]
        
            if (listIndex > 0):
                self.view.watchListInstruments.SetSelection(listIndex - 1)
        