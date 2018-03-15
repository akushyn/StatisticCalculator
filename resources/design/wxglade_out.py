# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0b3 on Sun Mar 11 20:55:27 2018
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class AkHistoricalDataManager(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AkHistoricalDataManager.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((607, 400))
        self.histDataMngr = wx.Notebook(self, wx.ID_ANY)
        self.importPageView = wx.Panel(self.histDataMngr, wx.ID_ANY, style=wx.BORDER_STATIC)
        self.cbInputFormat = wx.ComboBox(self.importPageView, wx.ID_ANY, choices=["Trade Workstation", "Metatrader 4"], style=wx.CB_DROPDOWN)
        self.cbTimeZone = wx.ComboBox(self.importPageView, wx.ID_ANY, choices=["UTC"], style=wx.CB_DROPDOWN)
        self.btnStartImport = wx.Button(self.importPageView, wx.ID_ANY, "Start Import")
        self.histDataMngr_Download = wx.Panel(self.histDataMngr, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AkHistoricalDataManager.__set_properties
        self.SetTitle("Historical Data Manager")
        self.cbInputFormat.SetSelection(0)
        self.cbTimeZone.SetSelection(0)
        self.importPageView.SetMinSize((600, 350))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AkHistoricalDataManager.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        vBox = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(2, 2, 2, 2)
        lblInpurFormat = wx.StaticText(self.importPageView, wx.ID_ANY, "Data Input Format")
        grid_sizer_1.Add(lblInpurFormat, 0, wx.ALL, 20)
        grid_sizer_1.Add(self.cbInputFormat, 0, wx.ALL | wx.EXPAND, 15)
        lblTimeZone = wx.StaticText(self.importPageView, wx.ID_ANY, "Time zone of imported data:")
        grid_sizer_1.Add(lblTimeZone, 0, wx.ALL, 20)
        grid_sizer_1.Add(self.cbTimeZone, 0, wx.ALL | wx.EXPAND, 15)
        vBox.Add(grid_sizer_1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 30)
        static_line_1 = wx.StaticLine(self.importPageView, wx.ID_ANY)
        vBox.Add(static_line_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.LEFT | wx.RIGHT, 20)
        vBox.Add(self.btnStartImport, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        vBox.Add((20, 20), 1, wx.EXPAND, 0)
        self.importPageView.SetSizer(vBox)
        self.histDataMngr.AddPage(self.importPageView, "Import")
        self.histDataMngr.AddPage(self.histDataMngr_Download, "Download")
        sizer.Add(self.histDataMngr, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        self.Layout()
        # end wxGlade

# end of class AkHistoricalDataManager