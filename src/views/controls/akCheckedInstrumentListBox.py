# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:38:19 2018

@author: Andriy
"""
import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

class AkCheckedInstrumentListBox(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)