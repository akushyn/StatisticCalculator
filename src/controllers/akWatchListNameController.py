# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 14:02:33 2018

@author: Andriy
"""
import wx
from src.views.akWatchListNameView import AkWatchListNameView
from src.models.akWatchListNameModel import AkWatchListNameModel

class AkWatchListNameController:
    def __init__(self):
        self.model = AkWatchListNameModel()
        self.view = AkWatchListNameView(None)
        
        self.view.Bind(wx.EVT_BUTTON, self.onOkHandler, self.view.btnOK)
        self.view.Bind(wx.EVT_BUTTON, self.onCancelHandler, self.view.btnCancel)

    def onOkHandler(self, event): 
        
        if (self.view.text_Name.GetValue() == ""):
            return
        
        if (self.view.text_Name.GetValue() == "Default"):
            dlg = wx.MessageDialog(self.view, "Default watch list is already defined", "Notification", wx.OK | wx.ICON_ERROR)
        if (dlg.ShowModal() == wx.ID_OK):
            dlg.Destroy()
            return
        
        #TODO: send value to listener
        
        self.view.Destroy()
        
    def onCancelHandler(self, event): 
        self.view.Destroy()
