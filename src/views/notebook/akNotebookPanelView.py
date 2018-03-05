# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 22:11:07 2018

@author: Andriy
"""

import wx
from src.views.notebook.akJournalView import AkJournalPanelView

class AkNotebookView(wx.Notebook):
    def __init__(self, *args, **kwds):
        wx.Notebook.__init__(self, *args, **kwds)
        
        self.notebook_Summary = wx.Panel(self, wx.ID_ANY)
        self.notebook_Graphs = wx.Panel(self, wx.ID_ANY)
        self.notebook_Periods = wx.Panel(self, wx.ID_ANY)
        #self.notebook_Journal = AkJournalPanelView()
    
        self.__do_layout()
    
    def __do_layout(self):        
        self.AddPage(self.notebook_Summary, "Summary")
        self.AddPage(self.notebook_Graphs, "Graphs")
        self.AddPage(self.notebook_Periods, "Periods")
        #self.AddPage(self.notebook_Journal, "Journal")    
        
        self.Layout()