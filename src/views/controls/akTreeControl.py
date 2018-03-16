# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 20:19:26 2018

@author: Andriy
"""
import wx
from wx.lib.pubsub import pub
import wx.lib.agw.customtreectrl as CT
from src.controllers.akPubEvents import AkPubEvents, AkHistoricalDataEvents
from src.utilities.akStringUtility import AkMenuString as ak

class AkTreeControl(CT.CustomTreeCtrl):
    ''' LazyTree is a simple "Lazy Evaluation" tree, that is, it only adds 
        items to the tree view when they are needed.'''

    def __init__(self, parent):
        super(AkTreeControl, self).__init__(parent, agwStyle=wx.TR_DEFAULT_STYLE | wx.TR_TWIST_BUTTONS)
        
        self.__collapsing = False
        
        root = self.AddRoot('Symbols')
        self.SetItemHasChildren(root)
        
        self.imported = self.AppendItem(root, 'Imported')
        self.SetItemHasChildren(self.imported)
        
        self.downloaded = self.AppendItem(root, 'Downloaded')
        self.SetItemHasChildren(self.downloaded)

        self.Bind(wx.EVT_TREE_ITEM_EXPANDING, self.OnExpandTreeItem_Handler)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSING, self.OnCollapseTreeItem_Handler)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnTreeItemDoubleClick_Handler)
        self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnShowPopup_Handler)

        pub.subscribe(self.AddImportedTreeItem, AkPubEvents.IMPORTED_DATA_CHANGED)
 
         #------------------------------------------------------------------------------
# Event handlers
#------------------------------------------------------------------------------
    def OnShowPopup_Handler(self, event):
        self.treeItemPopup = event.GetItem()
        if(self.ItemHasChildren(self.treeItemPopup) == False):
            self.popupmenu = wx.Menu()
            deleteItem = self.popupmenu.Append(ak.ID_DELETE, ak.ITEM_DELETE)
            self.Bind(wx.EVT_MENU, self.OnSelectContext_Handler, deleteItem)
            
            editItem = self.popupmenu.Append(ak.ID_EDIT, ak.ITEM_EDIT)
            self.Bind(wx.EVT_MENU, self.OnSelectContext_Handler, editItem)
            
            self.PopupMenu(self.popupmenu, event.GetPoint())
            self.popupmenu.Destroy()

    def OnSelectContext_Handler(self, event):
        item = self.popupmenu.FindItemById(event.GetId())
        if (item.GetText() == ak.ITEM_DELETE):
            #self.Delete(self.treeItemPopup)
            print("Delete item")
        elif (item.GetText() == ak.ITEM_EDIT): 
            print("Edit item")
        
    def OnExpandTreeItem_Handler(self, event):
        print("Event handler 'OnExpandTreeItem_Handler' not implemented!")
        print(event.GetEventObject())
        # Add a random number of children and randomly decide which 
        # children have children of their own.
        
        #nrChildren = random.randint(1, 6)
        #for childIndex in range(nrChildren):
        #    child = self.AppendItem(event.GetItem(), 'child %d'%childIndex)
        #    self.SetItemHasChildren(child, random.choice([True, False]))

    def OnCollapseTreeItem_Handler(self, event):
        print("Event handler 'OnCollapseTreeItem_Handler' not implemented!")
        # Be prepared, self.CollapseAndReset below may cause
        # another wx.EVT_TREE_ITEM_COLLAPSING event being triggered.

#        if self.__collapsing:
#            event.Veto()
#        else:
#            self.__collapsing = True
#            item = event.GetItem()
#            self.CollapseAndReset(item)
#            self.SetItemHasChildren(item)
#            self.__collapsing = False       


    def OnTreeItemDoubleClick_Handler(self,event):
        #print("Event handler 'OnTreeItemDoubleClick_Handler' not implemented!")
        print('Double clicked on', self.GetItemText(event.GetItem()))

        item = event.GetItem()
        data = self.GetItemData(item)
        
        pub.sendMessage(AkHistoricalDataEvents.LIST_DATA_CONTROL_CHANGING, data=data)   
        print("Pub sendMessage 'OnListDataChanging' called!") 
       
    def AddImportedTreeItem(self, items):
        self.DeleteChildren(self.imported)
        
        for i in range(len(items)):
            item = items[i]
            itemID = self.AppendItem(self.imported, item.GetName())
            self.SetItemData(itemID, item.GetData())  
            
            
            
            
                