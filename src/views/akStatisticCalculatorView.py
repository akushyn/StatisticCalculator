# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:00:38 2018

@author: Andriy
"""

import wx
import wx.html
from src.controllers.akJournalController import AkJournalController

class AkStatisticCalculatorView(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((900, 600))
        
        self.InitMenuBar()
        
        self.btn_Calculate = wx.Button(self, wx.ID_ANY, "Calculate")
        self.notebook_Main = wx.Notebook(self, wx.ID_ANY) #AkNotebookPanelView() 
       
        self.notebook_Summary = wx.Panel(self.notebook_Main, wx.ID_ANY)
        self.notebook_Graphs = wx.Panel(self.notebook_Main, wx.ID_ANY)
        self.notebook_Periods = wx.Panel(self.notebook_Main, wx.ID_ANY)
        
        self.journalController = AkJournalController()
        #self.notebook_Journal = AkJournalPanelView(self.notebook_Main, wx.ID_ANY)

        #self.noteBookController = AkNotebookController()
        
        self.__set_properties()
        self.__do_layout()

     
    def InitMenuBar(self):
        #--------------------------------------------------------------------------
        # Menu 'File'
        #------------------------       
        menuBar = wx.MenuBar()
        
        fileMenu = wx.Menu()
        self.connectMenuItem = wx.MenuItem(fileMenu, wx.ID_ANY, "Connect...")
        self.connectMenuItem.SetBitmap(wx.Bitmap('images/menu/connect.bmp'))
        fileMenu.Append(self.connectMenuItem) 
        
        self.disconnectMenuItem = wx.MenuItem(fileMenu, wx.ID_ANY, "Disconnect...")
        self.disconnectMenuItem.SetBitmap(wx.Bitmap('images/menu/disconnect.bmp'))
        fileMenu.Append(self.disconnectMenuItem)
        
        fileMenu.AppendSeparator()
        self.exitMenuItem = wx.MenuItem(fileMenu, wx.ID_ANY, '&Quit\tCtrl+Q')
        self.exitMenuItem.SetBitmap(wx.Bitmap('images/menu/exit.bmp'))
        fileMenu.Append(self.exitMenuItem)
        
        menuBar.Append(fileMenu, "&File")

        #--------------------------------------------------------------------------
        # Menu 'Tools'
        #------------------------
        toolsMenu = wx.Menu()
        
        self.itstrumentMngrMenuItem = wx.MenuItem(toolsMenu, wx.ID_ANY, "Instrument Manager...\tCtrl+I")
        self.itstrumentMngrMenuItem.SetBitmap(wx.Bitmap('images/menu/instruments.bmp'))
        toolsMenu.Append(self.itstrumentMngrMenuItem)
        
        self.historyDataMngrMenuItem = wx.MenuItem(toolsMenu, wx.ID_ANY, "Historical Data Manager...\tCtrl+H")
        self.historyDataMngrMenuItem.SetBitmap(wx.Bitmap('images/menu/history.bmp'))
        toolsMenu.Append(self.historyDataMngrMenuItem)
        
        toolsMenu.AppendSeparator()
        
        self.connectionMngrMenuItem = wx.MenuItem(toolsMenu, wx.ID_ANY, "Connection Manager...")
        self.connectionMngrMenuItem.SetBitmap(wx.Bitmap('images/menu/connections.bmp'))
        toolsMenu.Append(self.connectionMngrMenuItem)
        
        self.optionsMenuItem = wx.MenuItem(toolsMenu, wx.ID_ANY, "Options...\tCtrl+O")
        self.optionsMenuItem.SetBitmap(wx.Bitmap('images/menu/options.bmp'))
        toolsMenu.Append(self.optionsMenuItem)
        
        menuBar.Append(toolsMenu, "&Tools")

        #--------------------------------------------------------------------------
        # Menu 'Help'
        #------------------------
        
        helpMenu = wx.Menu()
        
        self.helpMenuItem = wx.MenuItem(helpMenu, wx.ID_ANY, "Help...\tF1")
        self.helpMenuItem.SetBitmap(wx.Bitmap('images/menu/help.bmp'))
        helpMenu.Append(self.helpMenuItem)
        
        self.aboutMenuItem = wx.MenuItem(helpMenu, wx.ID_ANY, "About...")
        self.aboutMenuItem.SetBitmap(wx.Bitmap('images/menu/about.bmp'))
        helpMenu.Append(self.aboutMenuItem)
        
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)
           
    def __set_properties(self):
        self.SetTitle(_("Statistic Calculator"))

    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.notebook_Main.AddPage(self.notebook_Summary, "Summary")
        self.notebook_Main.AddPage(self.notebook_Graphs, "Graphs")
        self.notebook_Main.AddPage(self.notebook_Periods, "Periods")
        #self.notebook_Main.AddPage(self.journalController.view, "Journal")
        
        hBox_Calculate = wx.BoxSizer(wx.HORIZONTAL)
        hBox_Calculate.Add(self.btn_Calculate, 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        sizer.Add(hBox_Calculate, 0, wx.ALL | wx.EXPAND, 10)
        
        sizer.Add(self.notebook_Main, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer)
        self.Layout()
