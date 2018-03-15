# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:01:22 2018

@author: Andriy
"""
import wx
from src.models.akConnectionManagerModel import AkConnectionManagerModel
from src.views.akConnectionManagerView import AkConnectionManagerView
from src.views.akConnectionOptionsView import AkConnectionOptionsView

class AkConnectionManagerController:
    def __init__(self):
        self.model = AkConnectionManagerModel()
        self.view = AkConnectionManagerView(None)
        
        self.view.Bind(wx.EVT_BUTTON, self.onAddConnectionHandler, self.view.btn_Add)
        self.view.Bind(wx.EVT_BUTTON, self.onChangeConnectionHandler, self.view.btn_Change)
        self.view.Bind(wx.EVT_BUTTON, self.onRemoveConnectionHandler, self.view.btn_Remove)
        self.view.Bind(wx.EVT_BUTTON, self.onCloseViewHandler, self.view.btn_Close)

    def onAddConnectionHandler(self, event):  # wxGlade: AkConnectionManager.<event_handler>
        connection = AkConnectionOptionsView(None, 'Connection Options', '') #AkTextEntryDialog(None, 'Title', 'Caption')
        connection.CenterOnParent()
        if (connection.ShowModal() == wx.ID_OK):
            if (connection.GetValue() == ""):
                return
            
            self.view.AddConnection(connection.GetValue())
        connection.Destroy()        
        print(wx.GetApp().GetTopWindow().GetMenuBar())

    def onChangeConnectionHandler(self, event):  # wxGlade: AkConnectionManager.<event_handler>
        connection = AkConnectionOptionsView(None, 'Connection Options', self.view.GetSelectedConnection()) #AkTextEntryDialog(None, 'Title', 'Caption')
        connection.CenterOnParent() 
        if (connection.ShowModal() == wx.ID_OK):
                self.view.ChangeConnection(connection.GetValue())
        connection.Destroy()   

    def onRemoveConnectionHandler(self, event):  
        if (self.view.GetSelectedIndex() == -1):
            return
        
        dlg = wx.MessageDialog(self.view, "Delete \'" + self.view.GetSelectedConnection() + "\' connection?", "Confirmation", wx.YES_NO | wx.ICON_ASTERISK)
        if (dlg.ShowModal() == wx.ID_YES):
            self.view.RemoveConnection()
        event.Skip()

    def onCloseViewHandler(self, event):  # wxGlade: AkConnectionManager.<event_handler>
        self.view.Close()
