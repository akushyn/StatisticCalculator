# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:08:42 2018

@author: Andriy
"""
import wx

class AkView(wx.Object):
    def __init__(self, controller):
        
        self.controller = controller
        self.controller.Register(self)
        
        
    def __set_properties(self):
        pass
    
    def __do_layout(self):
        pass