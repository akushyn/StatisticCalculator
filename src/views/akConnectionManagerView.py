# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:22:10 2018

@author: Andriy
"""

import wx

class AkConnectionManagerView(wx.Dialog):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.SYSTEM_MENU
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((370, 235))
        self.panel = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_RAISED)
        self.lstConnections = wx.ListBox(self.panel, wx.ID_ANY, choices=["c"])
        self.btn_Add = wx.Button(self.panel, wx.ID_ANY, "Add...")
        self.btn_Change = wx.Button(self.panel, wx.ID_ANY, "Change...")
        self.btn_Remove = wx.Button(self.panel, wx.ID_ANY, "Remove")
        self.btn_Close = wx.Button(self.panel, wx.ID_ANY, "Close")

        self.__set_properties()
        self.__do_layout()


    def __set_properties(self):

        self.SetTitle("Connection Set Up")
        self.lstConnections.SetMinSize((240, 168))
        self.btn_Add.SetMinSize((70, 26))
        self.btn_Change.SetMinSize((70, 26))
        self.btn_Remove.SetMinSize((70, 26))
        self.btn_Close.SetMinSize((70, 26))


    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        hBox = wx.BoxSizer(wx.HORIZONTAL)
        hBox_Buttons = wx.BoxSizer(wx.VERTICAL)
        hBox.Add(self.lstConnections, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.TOP, 10)
        hBox_Buttons.Add(self.btn_Add, 0, wx.BOTTOM | wx.TOP, 5)
        hBox_Buttons.Add(self.btn_Change, 0, wx.BOTTOM | wx.TOP, 5)
        hBox_Buttons.Add(self.btn_Remove, 0, wx.BOTTOM | wx.TOP, 5)
        hBox_Buttons.Add(self.btn_Close, 0, wx.TOP, 5)
        hBox.Add(hBox_Buttons, 0, wx.LEFT | wx.TOP, 15)
        self.panel.SetSizer(hBox)
        sizer.Add(self.panel, 1, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer)
        self.Layout()