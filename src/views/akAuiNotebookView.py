# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 11:55:44 2018

@author: Andriy
"""
import wx
from src.views.akSummaryView import AkSummaryView
from src.views.akGraphsView import AkGraphsView
from src.views.akJournalView import AkJournalView

class AkAuiNotebookView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        self.notebook = wx.aui.AuiNotebook(self)
        
        self.summary = AkSummaryView(self.notebook) 
        self.graphs = AkGraphsView(self.notebook)
        self.journal = AkJournalView(self.notebook)
       
        
        self.__do_layout()
        
    def __do_layout(self):
        
        self.notebook.AddPage(self.summary, "Summary")
        self.notebook.AddPage(self.graphs, "Graphs")
        self.notebook.AddPage(self.journal, "Journal")

        sizer = wx.BoxSizer()
        sizer.Add(self.notebook, 1, wx.EXPAND)
        self.SetSizer(sizer)

