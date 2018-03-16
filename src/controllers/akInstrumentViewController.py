# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:31:31 2018

@author: Andriy
"""
import wx
from src.models.akInstrumentManagerModel import AkInstrumentManagerModel
from src.controllers.akController import AkController

class AkInstrumentViewController(AkController):
    def __init__(self):
        AkController.__init__(self)
        
        self.model = AkInstrumentManagerModel()
        

