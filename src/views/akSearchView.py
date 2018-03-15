# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:14:29 2018

@author: Andriy
"""
import wx

class AkSearchView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        
        self.text_Name = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_Description = wx.TextCtrl(self, wx.ID_ANY, "")
        self.btnSearch = wx.Button(self, wx.ID_ANY, "Search")

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.text_Name.SetMinSize((70, 23))
        self.text_Description.SetMinSize((120, 23))
        self.btnSearch.SetMinSize((80, 23))
        
    def __do_layout(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        grid_Inputs = wx.FlexGridSizer(2, 3, 0, 0)        
        lblName = wx.StaticText(self, wx.ID_ANY, "Name")
        grid_Inputs.Add(lblName, 0, 0, 0)        
        lblDescription = wx.StaticText(self, wx.ID_ANY, "Description")
        grid_Inputs.Add(lblDescription, 0, wx.LEFT, 10)
        grid_Inputs.Add((0, 0), 0, 0, 0)
        grid_Inputs.Add(self.text_Name, 0, 0, 0)
        grid_Inputs.Add(self.text_Description, 0, wx.LEFT, 10)
        grid_Inputs.Add(self.btnSearch, 0, wx.LEFT, 20)
        
        sizer.Add(grid_Inputs, 0, wx.EXPAND, 0)
        
        self.SetSizer(sizer)
        self.Layout()