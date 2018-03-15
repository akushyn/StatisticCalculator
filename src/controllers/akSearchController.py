# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:26:17 2018

@author: Andriy
"""
import wx
from src.views.akSearchView import AkSearchView

class AkSearchController:
    def __init__(self):
        self.searchView = AkSearchView(None)
        
        self.view.Bind(wx.EVT_BUTTON, self.onSearchInstrument_btnClick_Handler, self.searchView.btnSearch)
