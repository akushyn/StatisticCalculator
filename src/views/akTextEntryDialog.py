# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 14:08:38 2018

@author: Andriy
"""
import wx

class AkTextEntryDialog(wx.Dialog):
    def __init__(self, parent, title, caption):
        style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        super(AkTextEntryDialog, self).__init__(parent, -1, title, style=style)
        
        text = wx.StaticText(self, -1, caption)
        input = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        input.SetInitialSize((400, 300))

        buttons = self.CreateButtonSizer(wx.OK|wx.CANCEL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 0, wx.ALL, 5)
        sizer.Add(input, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(buttons, 0, wx.EXPAND|wx.ALL, 5)
        self.SetSizerAndFit(sizer)
        self.input = input
    
    def SetValue(self, value):
        self.input.SetValue(value)
    
    def GetValue(self):
        return self.input.GetValue()