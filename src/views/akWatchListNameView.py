# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:37:03 2018

@author: Andriy
"""
import wx

class AkWatchListNameView(wx.Dialog):  
    def __init__(self, *args, **kwds):
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((225, 125))
        self.text_Name = wx.TextCtrl(self, wx.ID_ANY, "")
        self.btnOK = wx.Button(self, wx.ID_ANY, "OK")
        self.btnCancel = wx.Button(self, wx.ID_ANY, "Cancel")

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetTitle("Instrument list name")
        self.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Segoe UI"))
        self.btnOK.SetMinSize((50, 18))
        self.btnCancel.SetMinSize((50, 18))

    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        vBox = wx.BoxSizer(wx.VERTICAL)
        hBox_Buttons = wx.BoxSizer(wx.HORIZONTAL)
        hBox_Inputs = wx.BoxSizer(wx.HORIZONTAL)
        lblName = wx.StaticText(self, wx.ID_ANY, "Name:")
        hBox_Inputs.Add(lblName, 1, wx.ALIGN_CENTER | wx.LEFT, 10)
        hBox_Inputs.Add(self.text_Name, 2, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 5)
        vBox.Add(hBox_Inputs, 1, wx.ALIGN_CENTER | wx.ALL, 0)
        hBox_Buttons.Add(self.btnOK, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 15)
        hBox_Buttons.Add(self.btnCancel, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 15)
        vBox.Add(hBox_Buttons, 1, wx.ALIGN_CENTER, 0)
        sizer.Add(vBox, 1, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer)
        self.Layout()
        self.Centre()

