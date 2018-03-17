# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:00:38 2018

@author: Andriy
"""

import wx
import wx.html
import wx.aui

from src.controllers.akNotebookViewController import AkNotebookViewController
from src.controllers.akInstrumentViewController import AkInstrumentViewController
from src.controllers.akConnectionManagerController import AkConnectionManagerController
from src.controllers.akHistoricalViewController import AkHistoricalViewController

from src.views.akInstrumentView import AkInstrumentView
from src.views.akHistoricalView import AkHistoricalView
from src.views.akMainMenuView import AkMainMenuView
from src.views.akNotebookView import AkNotebookView

class AkCalculatorView(wx.Frame):
    def __init__(self, *args, **kwds):
        #style = wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER
        super(AkCalculatorView, self).__init__(*args, **kwds)
        self.__initControllers()
                
        self.SetSize((900, 600))
        
        self._mainMenu = AkMainMenuView()
        self.SetMenuBar(self._mainMenu)
        

        self._btn_Calculate = wx.Button(self, wx.ID_ANY, "Calculate")
        self._notebookView = AkNotebookView(self, self._notebookController)
        
        self.__set_properties()
        self.__do_layout()
        self.__set_bindings()
  
#------------------------------------------------------------------------------
# Private methods
#------------------------------------------------------------------------------
        
    def __initControllers(self):
        self._notebookController = AkNotebookViewController()
        self._instrumentViewController = AkInstrumentViewController()       
        self._historicalViewController = AkHistoricalViewController()

    def __set_bindings(self):
        self.Bind(wx.EVT_MENU, self.OnConnectView_Handler, id=self.GetMenuBar().connectMenuItem.GetId())   
        self.Bind(wx.EVT_MENU, self.OnDisconnectView_Handler, id=self.GetMenuBar().disconnectMenuItem.GetId())
        self.Bind(wx.EVT_MENU, self.OnExitApp_Handler, id=self.GetMenuBar().exitMenuItem.GetId())
        self.Bind(wx.EVT_MENU, self.OnInstrumentView_Handler, id=self.GetMenuBar().itstrumentMngrMenuItem.GetId())
        self.Bind(wx.EVT_MENU, self.OnHistoryView_Handler, id=self.GetMenuBar().historyDataMngrMenuItem.GetId())
        self.Bind(wx.EVT_MENU, self.OnConnectionOptionsView_Handler, id=self.GetMenuBar().connectionMngrMenuItem.GetId())
        self.Bind(wx.EVT_MENU, self.OnAppOptionsView_Handler, id=self.GetMenuBar().optionsMenuItem.GetId())
        self.Bind(wx.EVT_MENU, self.OnHelpView_Handler, id=self.GetMenuBar().helpMenuItem.GetId()) 
        self.Bind(wx.EVT_MENU, self.OnAboutView_Handler, id=self.GetMenuBar().aboutMenuItem.GetId())
                
        self.Bind(wx.EVT_MENU, self.OnDisplayActiveTab_Handler, id=self.GetMenuBar().summaryCheckItem.GetId())
        self.Bind(wx.EVT_MENU, self.OnDisplayActiveTab_Handler, id=self.GetMenuBar().graphsCheckItem.GetId())
        self.Bind(wx.EVT_MENU, self.OnDisplayActiveTab_Handler, id=self.GetMenuBar().journalCheckItem.GetId())
        
        self.Bind(wx.EVT_BUTTON, self.OnCalculate_Handler, self._btn_Calculate)
    def __set_properties(self):
        self.SetTitle("Statistic Calculator")

    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        hBox_Calculate = wx.BoxSizer(wx.HORIZONTAL)
        hBox_Calculate.Add(self._btn_Calculate, 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        sizer.Add(hBox_Calculate, 0, wx.ALL | wx.EXPAND, 10)
        
        sizer.Add(self._notebookView, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer)
        wx.CallAfter(self._notebookView.SendSizeEvent)
        self.Layout()
        
#------------------------------------------------------------------------------        
# Get/Set methods
#------------------------------------------------------------------------------
    def GetMenuBar(self):
        return self._mainMenu
    
    def GetNotebookView(self):
        return self._notebookView

    def GetHistoricalViewController(self):
        return self._historicalViewControllers
#------------------------------------------------------------------------------
# Event Handlers
#------------------------------------------------------------------------------
    def OnInstrumentView_Handler(self, event): 
        instrumentView = AkInstrumentView(self, self._instrumentViewController)
        instrumentView.ShowModal()
        instrumentView.Close()
        
    def OnConnectionOptionsView_Handler(self, event): 
        print("Event handler 'OnConnectionOptionsView_Handler' called!")
        
        controller = AkConnectionManagerController()
        with controller.view as view:
            view.ShowModal()

    def OnHistoryView_Handler(self, event):
        historicalView = AkHistoricalView(self, self._historicalViewController)   
        historicalView.ShowModal()
        historicalView.Close()
        
#        data = controller.model.GetImported().GetItems()
                    

    def OnAppOptionsView_Handler(self, event):
        print("Event handler 'OnAppOptionsView_Handler' not implemented!")
        event.Skip()

    def OnHelpView_Handler(self, event):  
        print("Event handler 'OnHelpView_Handler' called!")
        #with AkHelpDialog(self) as dlg:
        #    dlg.ShowModal()
        
        
    def OnAboutView_Handler(self, event):  
        aboutInfo = wx.adv.AboutDialogInfo()
        aboutInfo.SetIcon(wx.Icon('icons/setup.ico', wx.BITMAP_TYPE_ICO))
        aboutInfo.SetName("Statistic Calculator")
        aboutInfo.SetVersion("version 1.0")
        aboutInfo.SetDescription("GUI application based on wxPython framework.")
        aboutInfo.SetCopyright("(C) 2018")
        aboutInfo.AddDeveloper("Andriy Kushynskyy")
        wx.adv.AboutBox(aboutInfo)
    
    def OnConnectView_Handler(self, event):
        print("Event handler 'OnConnectView_Handler' not implemented!")
        event.Skip()
        
    def OnDisconnectView_Handler(self, event):
        print("Event handler 'OnDisconnectView_Handler' not implemented!")
        event.Skip()

    def OnExitApp_Handler(self, event):
        answer = wx.MessageBox("Do you really want to quit?", "Confirm", wx.YES_NO, self.view)
        
        if (answer == wx.YES):
            self.view.Close()
        
    def OnDisplayActiveTab_Handler(self, event):
        item = self.GetMenuBar().FindItemById(event.GetId())
        print(item.GetText())
        
    def OnCalculate_Handler(self, event):
        print("Event handler 'OnCalculate_Handler' not implemented!")
        items = self._historicalViewController.GetModel().GetImported().GetItems()
        for i in range(len(items)):
            name = items[i].GetName()
            print(name)
            data = items[i].GetData()
            for row in data:
                print(row)
            
    
        
