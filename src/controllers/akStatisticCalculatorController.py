# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 12:45:51 2018

@author: Andriy
"""
import wx
from src.views.akStatisticCalculatorView import AkStatisticCalculatorView
from src.models.akStatisticCalculatorModel import AkStatisticCalculatorModel
from src.controllers.akInstrumentManagerController import AkInstrumentManagerController
from src.controllers.akConnectionManagerController import AkConnectionManagerController
from src.controllers.akHistoricalDataManagerController import AkHistoricalDataManagerController
from src.controllers.akAboutController import AkAboutController
from src.controllers.akAuiNotebookController import AkAuiNotebookController

class AkStatisticCalculatorController():
    def __init__(self):
        self.model = AkStatisticCalculatorModel()
        self.view = AkStatisticCalculatorView(None, wx.ID_ANY, "")
        
        self.view.Bind(wx.EVT_MENU, self.onConnectHandler, id=self.view.connectMenuItem.GetId())   
        self.view.Bind(wx.EVT_MENU, self.onDisconnectHandler, id=self.view.disconnectMenuItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onExitHandler, id=self.view.exitMenuItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onInstrumentHandler, id=self.view.itstrumentMngrMenuItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onHistoryDataManagerHandler, id=self.view.historyDataMngrMenuItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onConnectionManagerHandler, id=self.view.connectionMngrMenuItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onOptionsHandler, id=self.view.optionsMenuItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onHelpHandler, id=self.view.helpMenuItem.GetId()) 
        self.view.Bind(wx.EVT_MENU, self.onAboutHandler, id=self.view.aboutMenuItem.GetId())
        
        self.notebookController = AkAuiNotebookController(self.view.notebook)

    def onInstrumentHandler(self, event): 
        print("Event handler 'onInstrumentHandler' called!")
        
        controller = AkInstrumentManagerController()       
        with controller.view as view:
            view.ShowModal()

    def onConnectionManagerHandler(self, event): 
        print("Event handler 'onConnectionManagerHandler' called!")
        
        controller = AkConnectionManagerController()
        with controller.view as view:
            view.ShowModal()

    def onHistoryDataManagerHandler(self, event):  
        print("Event handler 'onHistoryDataManagerHandler' called!")
        controller = AkHistoricalDataManagerController()
        with controller.view as view:
            view.ShowModal()

    def onOptionsHandler(self, event):
        print("Event handler 'onOptionsHandler' not implemented!")
        event.Skip()

    def onHelpHandler(self, event):  
        print("Event handler 'onHelpHandler' called!")
        #with AkHelpDialog(self) as dlg:
        #    dlg.ShowModal()
        
        
    def onAboutHandler(self, event):  
        print("Event handler 'onAboutHandler' called!")
        controller = AkAboutController()
        with controller.view as view:
            view.ShowModal()
    
    def onConnectHandler(self, event):
        print("Event handler 'onConnectHandler' not implemented!")
        event.Skip()
        
    def onDisconnectHandler(self, event):
        print("Event handler 'onDisconnectHandler' not implemented!")
        event.Skip()

    def onExitHandler(self, event):
        answer = wx.MessageBox("Do you really want to quit?", "Confirm", wx.YES_NO, self.view)
        
        if (answer == wx.YES):
            self.view.Close()
