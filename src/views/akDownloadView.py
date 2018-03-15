# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 19:15:14 2018

@author: Andriy
"""
import wx
from wx.lib.pubsub import pub
from src.controllers.akPubEvents import AkPubEvents, AkHistoricalDataEvents
from src.views.controls.akTreeControl import AkTreeControl
from src.views.controls.akListCtrl import AkListCtrl

class AkDownloadView(wx.Panel):
    def __init__(self, parent, controller):
        super(AkDownloadView, self).__init__(parent)
        
        self.controller = controller
        
        self._tree = AkTreeControl(self)
        self._list = AkListCtrl(self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)

        self._btn_Download = wx.Button(self, wx.ID_ANY, "Download")
        self._btn_Filter = wx.Button(self, wx.ID_ANY, "Filter")

        self.dpStart = wx.adv.DatePickerCtrl(self, wx.ID_ANY)
        self.dpEnd = wx.adv.DatePickerCtrl(self, wx.ID_ANY)

        self._btn_Download.Bind(wx.EVT_BUTTON, self.OnDownloadButtonClick_Handler)  
        self._btn_Filter.Bind(wx.EVT_BUTTON, self.OnFilterButtonClick_Handler)  

        self.__set_properties()
        self.__do_layout()
        
    def __set_properties(self):
        self._btn_Download.SetMinSize((182, 26))
        self.dpStart.SetMinSize((123, 23))
        self.dpEnd.SetMinSize((123, 23))

    
    def __do_layout(self):
        treeSizer = wx.BoxSizer(wx.VERTICAL)
        lblSymbols = wx.StaticText(self, wx.ID_ANY, "Symbols:")  
        treeSizer.Add(lblSymbols, 0, wx.BOTTOM | wx.TOP, 5)
        treeSizer.Add(self._tree, 1, wx.EXPAND, 0)
        treeSizer.Add(self._btn_Download, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 15)

        importedSizer = wx.BoxSizer(wx.VERTICAL)   
        fxGrid = wx.FlexGridSizer(0, 2, 0, 0)
        lblStartDate = wx.StaticText(self, wx.ID_ANY, "Start date:")
        fxGrid.Add(lblStartDate, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        fxGrid.Add(self.dpStart, 0, wx.ALIGN_CENTER | wx.ALL, 5)   
        lblEndDate = wx.StaticText(self, wx.ID_ANY, "End date:")
        fxGrid.Add(lblEndDate, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        fxGrid.Add(self.dpEnd, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        vBox_Grid = wx.BoxSizer(wx.VERTICAL)
        vBox_Grid.Add(fxGrid, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
        vBox_Grid.Add(self._btn_Filter, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        sBox_Filter = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Filter data"), wx.HORIZONTAL)
        sBox_Filter.Add(vBox_Grid, 0, wx.EXPAND, 0)
        sBox_Filter.Add((60, 0), 1, 0, 0)
        
        
        lbl_Database = wx.StaticText(self, wx.ID_ANY, "Database:")
        importedSizer.Add(lbl_Database, 0, wx.BOTTOM | wx.TOP, 5)
        importedSizer.Add(self._list, 1, wx.EXPAND, 0) 
        importedSizer.Add(sBox_Filter, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.BOTTOM | wx.EXPAND | wx.TOP, 0)       
 
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(treeSizer, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)       
        sizer.Add(importedSizer, 2, wx.EXPAND, 0) 
        
        self.SetSizer(sizer)
        self.Layout()
      
#------------------------------------------------------------------------------        
# Event handler methods
#------------------------------------------------------------------------------




    def OnFilterButtonClick_Handler(self, event):
        print("Event handler 'OnFilterButtonClick_Handler' not implemented!")
        
    def OnDownloadButtonClick_Handler(self, event):
        print("Event handler 'OnDownloadButtonClick_Handler' not implemented!")

#------------------------------------------------------------------------------        
# Get/Set methods
#------------------------------------------------------------------------------

    def GetTree(self):
        return self._tree

    def GetList(self):
        return self._list
    
#------------------------------------------------------------------------------        
# Class methods
#------------------------------------------------------------------------------
         

#        importedTreeItem = tree.imported
#        tree.AppendItem(importedTreeItem, fileName)
        
        #self.SetItemHasChildren(imported)
        
        #self._treeView.GetTree().AppendItem()
        #csvData = []
        #for row in data:
        #    csvData.append(row)
        #    print(row)    
            
            
            