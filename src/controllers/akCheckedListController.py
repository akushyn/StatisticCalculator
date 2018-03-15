# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:11:43 2018

@author: Andriy
"""
import wx
from src.views.akCheckedListView import AkCheckedListView
from src.models.akCheckedListModel import AkCheckedListModel

class AkCheckedListController:
    def __init__(self):
        self.checkedListView = AkCheckedListView(None)
        self.checkedListModel = AkCheckedListModel()

        self.view.Bind(wx.EVT_BUTTON, self.onSelectAllInstruments_btnClick_Handler, self.view.btnSelectAll)
        self.view.Bind(wx.EVT_BUTTON, self.onDeselectAllInstruments_btnClick_Handler, self.view.btnDeselectAll)
        self.view.Bind(wx.EVT_BUTTON, self.onInsertItems_btnClick_Handler, self.view.btn_Insert)
        self.view.Bind(wx.EVT_BUTTON, self.onDeleteItem_btnClick_Handler, self.view.btn_Remove)
