# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:35:59 2018

@author: Andriy
"""
import wx
import wx.adv

class AkJournalView(wx.Panel):
    def __init__(self, *args, **kw):
        super(AkJournalView, self).__init__(*args, **kw)

        self.calendar_Note = wx.adv.CalendarCtrl(self, wx.ID_ANY)
        self.btn_Ok = wx.Button(self, wx.ID_ANY, "OK")
        self.btn_Clear = wx.Button(self, wx.ID_ANY, "Clear")
        self.text_Note = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_RICH2)
        self.lst_Notes = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)

        self.__set_properties()
        self.__do_layout()
       
    def __set_properties(self):
        self.btn_Ok.SetMinSize((60, 26))
        self.btn_Clear.SetMinSize((60, 26))
        self.text_Note.SetMinSize((740, 190))
        
        self.lst_Notes.InsertColumn(0, "Date", format=wx.LIST_FORMAT_LEFT, width=372)
        self.lst_Notes.InsertColumn(1, "Note", format=wx.LIST_FORMAT_LEFT, width=304)

    def __do_layout(self):
        sizer_Journal = wx.BoxSizer(wx.VERTICAL)
        hBox_TopJournal = wx.BoxSizer(wx.HORIZONTAL)
        hBox_TextNote = wx.BoxSizer(wx.HORIZONTAL)
        vBox_Calendar = wx.BoxSizer(wx.VERTICAL)
        hBox_Buttons = wx.BoxSizer(wx.HORIZONTAL)
        vBox_Calendar.Add(self.calendar_Note, 0, 0, 0)
        hBox_Buttons.Add(self.btn_Ok, 0, wx.LEFT | wx.RIGHT, 5)
        hBox_Buttons.Add(self.btn_Clear, 0, 0, 0)
        vBox_Calendar.Add(hBox_Buttons, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        hBox_TopJournal.Add(vBox_Calendar, 0, 0, 0)
        hBox_TextNote.Add(self.text_Note, 1, wx.EXPAND, 0)
        hBox_TopJournal.Add(hBox_TextNote, 1, wx.EXPAND, 0)
        sizer_Journal.Add(hBox_TopJournal, 1, wx.EXPAND, 0)
        sizer_Journal.Add(self.lst_Notes, 4, wx.EXPAND, 0)
        self.SetSizer(sizer_Journal)

        self.Layout()        
        
        