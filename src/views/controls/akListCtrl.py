# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 16:50:19 2018

@author: Andriy
"""
import wx

class AkListCtrl(wx.ListCtrl):
    '''
    Custom List control.
    '''
    def __init__(self, *args, **kwargs):
        super(AkListCtrl, self).__init__(*args, **kwargs)
        self.__set_properties()
        
    def __set_properties(self):
        self.AppendColumn("N", format=wx.LIST_FORMAT_LEFT, width=41)
        self.AppendColumn("Date", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.AppendColumn("Open", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.AppendColumn("High", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.AppendColumn("Low", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.AppendColumn("Close", format=wx.LIST_FORMAT_LEFT, width=-1)

        