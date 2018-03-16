# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 11:55:44 2018

@author: Andriy
"""
import wx
from src.views.akSummaryView import AkSummaryView
from src.views.akGraphsView import AkGraphsView
from src.views.akJournalView import AkJournalView

class AkNotebookView(wx.Panel):
    def __init__(self, parent, controller):
        super(AkNotebookView, self).__init__(parent)
        
        self.controller = controller
        self.controller.Register(self)
        
        #wx.Panel.__init__(self, parent)

        #style = aui.AUI_NB_DEFAULT_STYLE ^ aui.AUI_NB_CLOSE_ON_ACTIVE_TAB
        self._notebook = wx.aui.AuiNotebook(self)
        
        self.summary = AkSummaryView(self._notebook) 
        self.graphs = AkGraphsView(self._notebook)
        self.journal = AkJournalView(self._notebook)
       
        self.__set_properties()    
        self.__do_layout()
         #self.view.Bind(wx.aui.AUI_NB_CLOSE_ON_ACTIVE_TAB, self.onCloseActiveTabHandler, self.view)
        
    def __set_properties(self):
        pass    
    
    def __do_layout(self):
        
        self._notebook.AddPage(self.summary, "Summary")
        self._notebook.AddPage(self.graphs, "Graphs")
        self._notebook.AddPage(self.journal, "Journal")

        sizer = wx.BoxSizer()
        sizer.Add(self._notebook, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def GetNotebook(self):
        return self._notebook