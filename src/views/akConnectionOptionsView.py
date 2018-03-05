# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:53:34 2018

@author: Andriy
"""
import wx

class AkConnectionOptionsView(wx.Dialog):
    def __init__(self, *args, **kwds):
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((451, 357))
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.text_ConnectionName = wx.TextCtrl(self, wx.ID_ANY, "")
        self.cb_Provider = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.chb_Startup = wx.CheckBox(self, wx.ID_ANY, "")
        self.btn_Save = wx.Button(self, wx.ID_ANY, "Save")
        self.btn_Cancel = wx.Button(self, wx.ID_ANY, "Cancel")

        self.__set_properties()
        self.__do_layout()


    def __set_properties(self):
        self.SetTitle("Connection Options")
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_ConnectionName.SetMinSize((190, 23))
        self.cb_Provider.SetMinSize((190, 23))

    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        hBox_Buttons = wx.BoxSizer(wx.HORIZONTAL)
        grid_Inputs = wx.GridSizer(0, 2, 0, 0)
        vBox = wx.BoxSizer(wx.VERTICAL)
        vBox_Labels = wx.BoxSizer(wx.VERTICAL)
        lblGeneral = wx.StaticText(self.panel, wx.ID_ANY, "General")
        lblGeneral.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        vBox_Labels.Add(lblGeneral, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 10)
        lblCaption = wx.StaticText(self.panel, wx.ID_ANY, "Enter your general connection information")
        vBox_Labels.Add(lblCaption, 0, wx.LEFT, 30)
        self.panel.SetSizer(vBox_Labels)
        vBox.Add(self.panel, 1, wx.EXPAND, 0)
        vBox.Add((20, 60), 0, wx.EXPAND, 0)
        sizer.Add(vBox, 1, wx.EXPAND, 0)
        lblConnectionName = wx.StaticText(self, wx.ID_ANY, "Connection name:")
        grid_Inputs.Add(lblConnectionName, 0, wx.LEFT, 20)
        grid_Inputs.Add(self.text_ConnectionName, 0, 0, 0)
        lblProvider = wx.StaticText(self, wx.ID_ANY, "Provider:")
        grid_Inputs.Add(lblProvider, 0, wx.LEFT, 20)
        grid_Inputs.Add(self.cb_Provider, 0, 0, 0)
        lblOnStartup = wx.StaticText(self, wx.ID_ANY, "Connect on startup:")
        grid_Inputs.Add(lblOnStartup, 0, wx.LEFT, 20)
        grid_Inputs.Add(self.chb_Startup, 0, 0, 0)
        sizer.Add(grid_Inputs, 1, wx.EXPAND, 0)
        hBox_Buttons.Add(self.btn_Save, 0, wx.RIGHT, 10)
        hBox_Buttons.Add(self.btn_Cancel, 0, 0, 0)
        sizer.Add(hBox_Buttons, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, 20)
        self.SetSizer(sizer)
        self.Layout()