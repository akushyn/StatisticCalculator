# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:01:22 2018

@author: Andriy
"""
import wx
from src.models.akConnectionManagerModel import AkConnectionManagerModel
from src.views.akConnectionManagerView import AkConnectionManagerView
from src.controllers.akConnectionOptionsController import AkConnectionOptionsController

class AkConnectionManagerController:
    def __init__(self):
        self.model = AkConnectionManagerModel()
        self.view = AkConnectionManagerView(None)
        
        self.view.Bind(wx.EVT_BUTTON, self.onAddHandler, self.view.btn_Add)
        self.view.Bind(wx.EVT_BUTTON, self.onChangeHandler, self.view.btn_Change)
        self.view.Bind(wx.EVT_BUTTON, self.onRemoveHandler, self.view.btn_Remove)
        self.view.Bind(wx.EVT_BUTTON, self.onCloseHandler, self.view.btn_Close)

    def onAddHandler(self, event):  # wxGlade: AkConnectionManager.<event_handler>
        print("Event handler 'onAddHandler' called!")
        controller = AkConnectionOptionsController()
        with controller.view as connectionView:
            connectionView.ShowModal()

    def onChangeHandler(self, event):  # wxGlade: AkConnectionManager.<event_handler>
        print("Event handler 'onChangeHandler' not implemented!")
        event.Skip()

    def onRemoveHandler(self, event):  # wxGlade: AkConnectionManager.<event_handler>
        print("Event handler 'onRemoveHandler' not implemented!")
        event.Skip()

    def onCloseHandler(self, event):  # wxGlade: AkConnectionManager.<event_handler>
        self.view.Close()
