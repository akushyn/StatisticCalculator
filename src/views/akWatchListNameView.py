# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:37:03 2018

@author: Andriy
"""
import wx

class AkWatchListNameView(wx.Dialog):  
    def __init__(self, parent, title, caption):
        super(AkWatchListNameView, self).__init__(parent, -1, title, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSize((240, 125))
        self.text_Name = wx.TextCtrl(self, wx.ID_ANY, "")

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Segoe UI"))

    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        vBox = wx.BoxSizer(wx.VERTICAL)
        buttons = self.CreateButtonSizer(wx.OK|wx.CANCEL)
        hBox_Inputs = wx.BoxSizer(wx.HORIZONTAL)
        lblName = wx.StaticText(self, wx.ID_ANY, "Name:")
        hBox_Inputs.Add(lblName, 1, wx.ALIGN_CENTER | wx.LEFT, 10)
        hBox_Inputs.Add(self.text_Name, 2, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 5)
        vBox.Add(hBox_Inputs, 1, wx.ALIGN_CENTER | wx.ALL, 0)
        vBox.Add(buttons, 1, wx.ALIGN_CENTER, 0)
        sizer.Add(vBox, 1, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer)
        self.Layout()
        self.Centre()

    def SetValue(self, value):
        self.text_Name.SetValue(value)
    
    def GetValue(self):
        return self.text_Name.GetValue()