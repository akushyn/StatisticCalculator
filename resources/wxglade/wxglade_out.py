# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0b3 on Sun Feb 25 11:16:24 2018
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class AkInstrumentManagerView(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AkInstrumentManagerView.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((600, 430))
        self.cbInstrumentLists = wx.ComboBox(self, wx.ID_ANY, choices=["Default"], style=wx.CB_DROPDOWN)
        self.lstWatchList = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        self.btnNew = wx.Button(self, wx.ID_ANY, "New")
        self.btnDelete = wx.Button(self, wx.ID_ANY, "Delete")
        self.text_Name = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_Description = wx.TextCtrl(self, wx.ID_ANY, "")
        self.btnSearch = wx.Button(self, wx.ID_ANY, "Search")
        self.btnSelectAll = wx.Button(self, wx.ID_ANY, "Select All")
        self.btnDeselectAll = wx.Button(self, wx.ID_ANY, "Deselect All")
        self.btn_Insert = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("G:\\Programming\\Projects\\StatisticCalculator\\images\\add.ico", wx.BITMAP_TYPE_ANY))
        self.btn_Remove = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("G:\\Programming\\Projects\\StatisticCalculator\\images\\delete.ico", wx.BITMAP_TYPE_ANY))
        self.lstInstrumentList = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        self.btnOK = wx.Button(self, wx.ID_ANY, "OK")
        self.btnCancel = wx.Button(self, wx.ID_ANY, "Cancel")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onNewListHandler, self.btnNew)
        self.Bind(wx.EVT_BUTTON, self.onDeleteListHandler, self.btnDelete)
        self.Bind(wx.EVT_BUTTON, self.onSearchHandler, self.btnSearch)
        self.Bind(wx.EVT_BUTTON, self.onSelectAllHandler, self.btnSelectAll)
        self.Bind(wx.EVT_BUTTON, self.onDeselectHandler, self.btnDeselectAll)
        self.Bind(wx.EVT_BUTTON, self.onInsertHandler, self.btn_Insert)
        self.Bind(wx.EVT_BUTTON, self.onRemoveHandler, self.btn_Remove)
        self.Bind(wx.EVT_BUTTON, self.onSaveAndApplyHandler, self.btnOK)
        self.Bind(wx.EVT_BUTTON, self.onCancelHandler, self.btnCancel)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AkInstrumentManagerView.__set_properties
        self.SetTitle("Instrument Manager")
        self.cbInstrumentLists.SetSelection(0)
        self.lstWatchList.SetMinSize((120, 439))
        self.btnNew.SetMinSize((60, 26))
        self.btnDelete.SetMinSize((60, 26))
        self.text_Name.SetMinSize((70, 23))
        self.text_Description.SetMinSize((120, 23))
        self.btnSearch.SetMinSize((80, 23))
        self.btnSelectAll.SetMinSize((70, 26))
        self.btnDeselectAll.SetMinSize((70, 26))
        self.btn_Insert.SetMinSize((25, 25))
        self.btn_Remove.SetMinSize((25, 25))
        self.lstInstrumentList.SetMinSize((250, 230))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AkInstrumentManagerView.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        vBox_Save = wx.BoxSizer(wx.HORIZONTAL)
        hBox_Left = wx.BoxSizer(wx.HORIZONTAL)
        vBox_Instruments = wx.BoxSizer(wx.VERTICAL)
        hBox_Instruments = wx.BoxSizer(wx.HORIZONTAL)
        vBox_Buttons = wx.BoxSizer(wx.VERTICAL)
        hBox_Search = wx.BoxSizer(wx.HORIZONTAL)
        grid_Inputs = wx.FlexGridSizer(2, 3, 0, 0)
        vBox_WatchList = wx.BoxSizer(wx.VERTICAL)
        hBox_ListButtons = wx.BoxSizer(wx.HORIZONTAL)
        lblInstuments = wx.StaticText(self, wx.ID_ANY, "Instrument lists:")
        vBox_WatchList.Add(lblInstuments, 0, wx.TOP, 5)
        vBox_WatchList.Add(self.cbInstrumentLists, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 5)
        vBox_WatchList.Add(self.lstWatchList, 1, wx.EXPAND, 0)
        hBox_ListButtons.Add(self.btnNew, 0, wx.LEFT | wx.RIGHT, 5)
        hBox_ListButtons.Add(self.btnDelete, 0, wx.LEFT | wx.RIGHT, 5)
        vBox_WatchList.Add(hBox_ListButtons, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        hBox_Left.Add(vBox_WatchList, 0, wx.ALL | wx.EXPAND, 10)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        hBox_Left.Add(static_line_1, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 10)
        lblCaption = wx.StaticText(self, wx.ID_ANY, "Available master instruments")
        vBox_Instruments.Add(lblCaption, 0, 0, 0)
        lblName = wx.StaticText(self, wx.ID_ANY, "Name")
        grid_Inputs.Add(lblName, 0, 0, 0)
        lblDescription = wx.StaticText(self, wx.ID_ANY, "Description")
        grid_Inputs.Add(lblDescription, 0, wx.LEFT, 10)
        grid_Inputs.Add((0, 0), 0, 0, 0)
        grid_Inputs.Add(self.text_Name, 0, 0, 0)
        grid_Inputs.Add(self.text_Description, 0, wx.LEFT, 10)
        grid_Inputs.Add(self.btnSearch, 0, wx.LEFT, 20)
        hBox_Search.Add(grid_Inputs, 0, wx.EXPAND, 0)
        vBox_Instruments.Add(hBox_Search, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 15)
        vBox_Buttons.Add(self.btnSelectAll, 0, wx.ALIGN_CENTER | wx.BOTTOM, 5)
        vBox_Buttons.Add(self.btnDeselectAll, 0, wx.ALIGN_CENTER, 0)
        vBox_Buttons.Add((20, 20), 1, wx.EXPAND, 0)
        vBox_Buttons.Add(self.btn_Insert, 0, 0, 0)
        vBox_Buttons.Add(self.btn_Remove, 0, 0, 0)
        hBox_Instruments.Add(vBox_Buttons, 0, wx.EXPAND | wx.RIGHT, 10)
        hBox_Instruments.Add(self.lstInstrumentList, 1, wx.EXPAND, 0)
        vBox_Instruments.Add(hBox_Instruments, 1, wx.EXPAND, 0)
        hBox_Left.Add(vBox_Instruments, 4, wx.ALL | wx.EXPAND, 10)
        sizer.Add(hBox_Left, 1, wx.EXPAND, 0)
        static_line_2 = wx.StaticLine(self, wx.ID_ANY)
        sizer.Add(static_line_2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        vBox_Save.Add(self.btnOK, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 40)
        vBox_Save.Add(self.btnCancel, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 40)
        sizer.Add(vBox_Save, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.TOP, 15)
        self.SetSizer(sizer)
        self.Layout()
        # end wxGlade

    def onNewListHandler(self, event):  # wxGlade: AkInstrumentManagerView.<event_handler>
        print("Event handler 'onNewListHandler' not implemented!")
        event.Skip()

    def onDeleteListHandler(self, event):  # wxGlade: AkInstrumentManagerView.<event_handler>
        print("Event handler 'onDeleteListHandler' not implemented!")
        event.Skip()

    def onSearchHandler(self, event):  # wxGlade: AkInstrumentManagerView.<event_handler>
        print("Event handler 'onSearchHandler' not implemented!")
        event.Skip()

    def onSelectAllHandler(self, event):  # wxGlade: AkInstrumentManagerView.<event_handler>
        print("Event handler 'onSelectAllHandler' not implemented!")
        event.Skip()

    def onDeselectHandler(self, event):  # wxGlade: AkInstrumentManagerView.<event_handler>
        print("Event handler 'onDeselectHandler' not implemented!")
        event.Skip()

    def onInsertHandler(self, event):  # wxGlade: AkInstrumentManagerView.<event_handler>
        print("Event handler 'onInsertHandler' not implemented!")
        event.Skip()

    def onRemoveHandler(self, event):  # wxGlade: AkInstrumentManagerView.<event_handler>
        print("Event handler 'onRemoveHandler' not implemented!")
        event.Skip()

    def onSaveAndApplyHandler(self, event):  # wxGlade: AkInstrumentManagerView.<event_handler>
        print("Event handler 'onSaveAndApplyHandler' not implemented!")
        event.Skip()

    def onCancelHandler(self, event):  # wxGlade: AkInstrumentManagerView.<event_handler>
        print("Event handler 'onCancelHandler' not implemented!")
        event.Skip()

# end of class AkInstrumentManagerView
