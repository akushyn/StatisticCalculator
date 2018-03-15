# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:42:33 2018

@author: Andriy
"""
from src.views.akInstrumentsTreeView import AkInstrumentsTreeView
from src.models.akInstrumentsTreeModel import AkInstrumentsTreeModel

class AkInstrumentsTreeController:
    def __init_(self):
        self.instrumentsTreeView = AkInstrumentsTreeView(None)
        self.instrumentsTreeModel = AkInstrumentsTreeModel()