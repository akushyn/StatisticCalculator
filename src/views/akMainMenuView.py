# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:30:14 2018

@author: Andriy
"""
import wx

class AkMainMenuView(wx.MenuBar):
    def __init__(self, *args, **kw):
        super(AkMainMenuView, self).__init__(*args, **kw)
        
        self.fileMenu = wx.Menu()
        self.connectMenuItem = wx.MenuItem(self.fileMenu, wx.ID_ANY, "Connect...")
        self.connectMenuItem.SetBitmap(wx.Bitmap('icons/menu/connect.bmp'))
        self.fileMenu.Append(self.connectMenuItem) 
        
        self.disconnectMenuItem = wx.MenuItem(self.fileMenu, wx.ID_ANY, "Disconnect...")
        self.disconnectMenuItem.SetBitmap(wx.Bitmap('icons/menu/disconnect.bmp'))
        self.fileMenu.Append(self.disconnectMenuItem)
        
        self.fileMenu.AppendSeparator()
        self.exitMenuItem = wx.MenuItem(self.fileMenu, wx.ID_ANY, '&Quit\tCtrl+Q')
        self.exitMenuItem.SetBitmap(wx.Bitmap('icons/menu/exit.bmp'))
        self.fileMenu.Append(self.exitMenuItem)
        
        self.Append(self.fileMenu, "&File")

        #--------------------------------------------------------------------------
        # Menu 'Tools'
        #------------------------
        toolsMenu = wx.Menu()
        
        self.itstrumentMngrMenuItem = wx.MenuItem(toolsMenu, wx.ID_ANY, "Instrument Manager...\tCtrl+I")
        self.itstrumentMngrMenuItem.SetBitmap(wx.Bitmap('icons/menu/instruments.bmp'))
        toolsMenu.Append(self.itstrumentMngrMenuItem)
        
        self.historyDataMngrMenuItem = wx.MenuItem(toolsMenu, wx.ID_ANY, "Historical Data Manager...\tCtrl+H")
        self.historyDataMngrMenuItem.SetBitmap(wx.Bitmap('icons/menu/history.bmp'))
        toolsMenu.Append(self.historyDataMngrMenuItem)
        
        toolsMenu.AppendSeparator()
        
        self.connectionMngrMenuItem = wx.MenuItem(toolsMenu, wx.ID_ANY, "Connection Manager...")
        self.connectionMngrMenuItem.SetBitmap(wx.Bitmap('icons/menu/connections.bmp'))
        toolsMenu.Append(self.connectionMngrMenuItem)
        
        self.optionsMenuItem = wx.MenuItem(toolsMenu, wx.ID_ANY, "Options...\tCtrl+O")
        self.optionsMenuItem.SetBitmap(wx.Bitmap('icons/menu/options.bmp'))
        toolsMenu.Append(self.optionsMenuItem)
        
        self.Append(toolsMenu, "&Tools")

        #--------------------------------------------------------------------------
        # Menu 'View'
        #------------------------
        viewMenu = wx.Menu()
        
        panels = wx.Menu()
      
        self.summaryCheckItem = panels.Append(wx.ID_ANY, 'Summary', kind=wx.ITEM_CHECK)
        self.graphsCheckItem = panels.Append(wx.ID_ANY, 'Graphs', kind=wx.ITEM_CHECK)        
        self.journalCheckItem = panels.Append(wx.ID_ANY, 'Journal', kind=wx.ITEM_CHECK)
               
        viewMenu.Append(-1, "Panels", panels)   
        self.Append(viewMenu, "&View")

        #--------------------------------------------------------------------------
        # Menu 'Help'
        #------------------------
        
        helpMenu = wx.Menu()
        
        self.helpMenuItem = wx.MenuItem(helpMenu, wx.ID_ANY, "Help...\tF1")
        self.helpMenuItem.SetBitmap(wx.Bitmap('icons/menu/help.bmp'))
        helpMenu.Append(self.helpMenuItem)
        
        self.aboutMenuItem = wx.MenuItem(helpMenu, wx.ID_ANY, "About...")
        self.aboutMenuItem.SetBitmap(wx.Bitmap('icons/menu/about.bmp'))
        helpMenu.Append(self.aboutMenuItem)
        
        self.Append(helpMenu, "&Help")
