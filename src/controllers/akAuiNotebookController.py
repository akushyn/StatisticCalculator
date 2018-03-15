# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 22:46:47 2018

@author: Andriy
"""
import wx
from src.models.akAuiNotebookModel import AkAuiNotebookModel

class AkAuiNotebookController():
    def __init__(self, view):
        self.model = AkAuiNotebookModel()
        self.view = view
        
        #self.view.Bind(wx.aui.AUI_NB_CLOSE_ON_ACTIVE_TAB, self.onCloseActiveTabHandler, self.view)
        
    def onCloseActiveTabHandler(self):
        print("onCloseActiveTabHandler is not implemented!")