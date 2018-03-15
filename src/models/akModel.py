# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:05:10 2018

@author: Andriy
"""

class AkModel:
    def __init__(self, name="", data=[]):
        self.data = data
        self.name = name
        
    def GetName(self):
        return self.name
    
    def SetName(self, name):
        self.name = name
        
    def SetData(self, data):
        self.data = data
        
    def GetData(self):
        return self.data