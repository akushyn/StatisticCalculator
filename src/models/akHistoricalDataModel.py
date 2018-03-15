# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:06:34 2018

@author: Andriy
"""

from wx.lib.pubsub import pub
from src.controllers.akPubEvents import AkPubEvents 
from src.models.akModel import AkModel


class AkHistoricalDataModel:
    def __init__(self):
        self._imported = AkImported()
    

    def GetImported(self):
        return self._imported
    
        
class AkInstrument(AkModel):
     
    def __init__(self, name, data):
        self.name = name
        self.data = data
            
    def SetName(self, name):
        self.name = name
        pub.sendMessage(AkPubEvents.INSTRUMENT_CHANGED, name=self.name)

    def SetData(self, data):
        self.data = data
        print("set new data")
        pub.sendMessage(AkPubEvents.INSTRUMENT_CHANGED, data=self.data)
        
    def GetName(self):
        return self.name
    
    def GetData(self):
        return self.data
        
class AkImported:
    def __init__(self):
        self._items = []
        
    def Add(self, item):
        self._items.append(item)
        
        # send message for all views which use this data model
        pub.sendMessage(AkPubEvents.IMPORTED_DATA_CHANGED, items=self._items)
        
    def Get(self, index):
        self._items[index]
        
    def Remove(self, index):
        pass
    
    def GetItems(self):
        return self._items
    
    def GetCount(self):
        return len(self._items)