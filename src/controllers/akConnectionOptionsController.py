# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:55:14 2018

@author: Andriy
"""
import wx
from src.views.akConnectionOptionsView import AkConnectionOptionsView
from src.models.akConnectionOptionsModel import AkConnectionOptionsModel

class AkConnectionOptionsController:
    def __init__(self):
        self.model = AkConnectionOptionsModel()
        self.view = AkConnectionOptionsView(None)
        
        self.view.Bind(wx.EVT_CHECKBOX, self.onConnectOnStartupHandler, self.view.chb_Startup)
        self.view.Bind(wx.EVT_BUTTON, self.onSaveConnectionOptionsHandler, self.view.btn_Save)
        self.view.Bind(wx.EVT_BUTTON, self.onCancelConnectionOptionsHandler, self.view.btn_Cancel)

    def onConnectOnStartupHandler(self, event):
        print("Event handler 'onConnectOnStartupHandler' not implemented!")
        event.Skip()

    def onSaveConnectionOptionsHandler(self, event):
        print("Event handler 'onSaveConnectionOptionsHandler' not implemented!")
        
        event.Skip()

    def onCancelConnectionOptionsHandler(self, event):
        self.Close()
        event.Skip()
