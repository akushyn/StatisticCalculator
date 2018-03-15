# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 12:45:51 2018

@author: Andriy
"""
import wx
import wx.lib.pubsub.setupkwargs
from wx.lib.pubsub import pub
from src.controllers.akPubEvents import AkPubEvents
#from functools import partial
from src.views.akCalculatorView import AkCalculatorView
from src.models.akCalculatorModel import AkCalculatorModel
from src.controllers.akInstrumentManagerController import AkInstrumentManagerController
from src.controllers.akConnectionManagerController import AkConnectionManagerController
from src.controllers.akHistoricalDataController import AkHistoricalDataController
from src.views.akHistoricalDataView import AkHistoricalDataView
from src.controllers.akAuiNotebookController import AkAuiNotebookController
from src.controllers.akController import AkController

class AkCalculatorController():
    def __init__(self):
        AkController.__init__(self)
        self.model = AkCalculatorModel()
        self.view = AkCalculatorView(None, wx.ID_ANY, "")
        
        self.view.Bind(wx.EVT_MENU, self.onConnectHandler, id=self.view.mainMenu.connectMenuItem.GetId())   
        self.view.Bind(wx.EVT_MENU, self.onDisconnectHandler, id=self.view.mainMenu.disconnectMenuItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onExitHandler, id=self.view.mainMenu.exitMenuItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onInstrumentHandler, id=self.view.mainMenu.itstrumentMngrMenuItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onHistoryDataManagerHandler, id=self.view.mainMenu.historyDataMngrMenuItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onConnectionManagerHandler, id=self.view.mainMenu.connectionMngrMenuItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onOptionsHandler, id=self.view.mainMenu.optionsMenuItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onHelpHandler, id=self.view.mainMenu.helpMenuItem.GetId()) 
        self.view.Bind(wx.EVT_MENU, self.onAboutHandler, id=self.view.mainMenu.aboutMenuItem.GetId())
                
        self.view.Bind(wx.EVT_MENU, self.onCheckViewPanel, id=self.view.mainMenu.summaryCheckItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onCheckViewPanel, id=self.view.mainMenu.graphsCheckItem.GetId())
        self.view.Bind(wx.EVT_MENU, self.onCheckViewPanel, id=self.view.mainMenu.journalCheckItem.GetId())
        
        self.notebookController = AkAuiNotebookController(self.view.aui_notebook.notebook)
        
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
        controller = AkHistoricalDataController()

        historicalDataView = AkHistoricalDataView(self.view, controller)        
        historicalDataView.ShowModal()
        historicalDataView.Close()
        
#        data = controller.model.GetImported().GetItems()
                    

    def onOptionsHandler(self, event):
        print("Event handler 'onOptionsHandler' not implemented!")
        event.Skip()

    def onHelpHandler(self, event):  
        print("Event handler 'onHelpHandler' called!")
        #with AkHelpDialog(self) as dlg:
        #    dlg.ShowModal()
        
        
    def onAboutHandler(self, event):  
        aboutInfo = wx.adv.AboutDialogInfo()
        aboutInfo.SetIcon(wx.Icon('icons/setup.ico', wx.BITMAP_TYPE_ICO))
        aboutInfo.SetName("Statistic Calculator")
        aboutInfo.SetVersion("version 1.0")
        aboutInfo.SetDescription("GUI application based on wxPython framework.")
        aboutInfo.SetCopyright("(C) 2018")
        #aboutInfo.SetWebSite("http:#myapp.org")
        aboutInfo.AddDeveloper("Andriy Kushynskyy")

        wx.adv.AboutBox(aboutInfo)

        #print("Event handler 'onAboutHandler' called!")
        #controller = AkAboutController()
        #with controller.view as view:
        #    view.ShowModal()
    
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
            
    def onCheckViewPanel(self, event):
        item = self.view.GetMenuBar().FindItemById(event.GetId())
        print(item.GetText())
        
       
        
        
