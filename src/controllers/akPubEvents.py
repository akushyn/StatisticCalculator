# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:26:57 2018

@author: Andriy
"""

class AkPubEvents(object):
    IMPORTED_DATA_CHANGED = "imported.data.changed"
    IMPORTED_DATA_CHANGING = "imported.data.changing"
    INSTRUMENT_CHANGED = "instrument.changed"   
    
    
class AkHistoricalDataEvents(object):
    LIST_DATA_CONTROL_CHANGING = "list.data.control.changing"

class AkViewEvents(object):
    UPDATE_VIEW = 1
    PLOT_DATA = 2
    FINISH_UPDATE = 3    