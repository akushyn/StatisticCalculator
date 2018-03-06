# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:40:57 2018

@author: Andriy
"""
import wx
from datetime import datetime
from src.models.akJournalModel import AkJournalModel, AkJournalNoteItemModel

class AkJournalController:
    def __init__(self, view):
        self.model = AkJournalModel()
        self.view = view
        
        self.view.btn_Ok.Bind(wx.EVT_BUTTON, self.onAddNoteHandler, self.view.btn_Ok)       
        self.view.btn_Clear.Bind(wx.EVT_BUTTON, self.onClearHandler, self.view.btn_Clear)
       
        self.view.lst_Notes.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.onNotesItemRightClickHandler)
        self.view.lst_Notes.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onDoubleClickHandler)    

    def onAddNoteHandler(self, event): 
        "Add new note to the lst_Notes widget"
        noteString = self.view.text_Note.GetValue()
        if (noteString == ""):
            return
        
        dtObject =  datetime.fromtimestamp(self.view.calendar_Note.GetDate().GetTicks())         
        dateString = ' '.join([str(dtObject)[:10], str(datetime.now().time().replace(second=0, microsecond=0))])
        
        item = AkJournalNoteItemModel(dateString, noteString)
        self.model.AddNoteItem(item)

           
        count = self.view.lst_Notes.GetItemCount()        
        self.view.lst_Notes.InsertItem(count, item.GetDate())
        self.view.lst_Notes.SetItem(count, 1, item.GetNote())
        
        for i in range(self.model.GetCount()):
            print(self.model.GetItem(i).ToString())
        
    def onClearHandler(self, event): 
        self.view.text_Note.Clear()

    def onNotesItemRightClickHandler(self, event):  # wxGlade: AkNotebookMain.<event_handler>
        print("Event handler 'onNotesItemRightClickHandler' not implemented!")
        event.Skip()
    
    def onDoubleClickHandler(self, event):
        print("Event handler 'onDoubleClickHandler' not implemented!")
        event.Skip()
    