# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:06:22 2018

@author: Andriy
"""
from wx.lib.pubsub import pub
from src.controllers.akController import AkController
from src.models.akHistoricalDataModel import AkHistoricalDataModel
from src.controllers.akPubEvents import AkPubEvents
from src.models.akHistoricalDataModel import AkInstrument

class AkHistoricalDataController(AkController):
    def __init__(self):
        AkController.__init__(self)  
        
        self.model = AkHistoricalDataModel()
        
        pub.subscribe(self.onLoadData, AkPubEvents.IMPORTED_DATA_CHANGING)               
 
                
    def onLoadData(self, name, data, headers=None):
        instrument = AkInstrument(name, data)
        
        self.model.GetImported().Add(instrument)
        
