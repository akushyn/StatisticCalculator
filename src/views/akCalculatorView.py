# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:00:38 2018

@author: Andriy
"""

import wx
import wx.html
import wx.aui
from src.views.akMainMenuView import AkMainMenuView

from src.views.akAuiNotebookView import AkAuiNotebookView

class AkCalculatorView(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        self.SetSize((900, 600))
        
        #self.InitMenuBar()
        self.mainMenu = AkMainMenuView()
        self.SetMenuBar(self.mainMenu)
        
        self.btn_Calculate = wx.Button(self, wx.ID_ANY, "Calculate")
        self.aui_notebook = AkAuiNotebookView(self)
        
        self.__set_properties()
        self.__do_layout()
       
    def __set_properties(self):
        self.SetTitle(_("Statistic Calculator"))

    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        hBox_Calculate = wx.BoxSizer(wx.HORIZONTAL)
        hBox_Calculate.Add(self.btn_Calculate, 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        hBox_Calculate.Add((0, 0), 0, 0, 0)
        sizer.Add(hBox_Calculate, 0, wx.ALL | wx.EXPAND, 10)
        
        sizer.Add(self.aui_notebook, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer)
        wx.CallAfter(self.aui_notebook.SendSizeEvent)
        self.Layout()
