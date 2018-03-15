# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:33:38 2018

@author: Andriy
"""

class AkInstrumentManagerModel:
    def __init__(self):
        self._watchListItems = AkWatchListData([])
        
    def GetWatchListItems(self):
        return self._watchListItems    
        

class AkWatchListData:
    def __init__(self, items):
        self.list = [[items]]
        
    def Delete(self, idx):
        del self.list[idx]

    def Add(self, items):
        self.list.append(items)

    def GetItemsByIndex(self, idx):
        return self.list[idx]
    
    def Insert(self, idx, items):
        self.list.insert(idx, items) 
        