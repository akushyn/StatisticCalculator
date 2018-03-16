# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 12:45:51 2018

@author: Andriy
"""
from src.models.akCalculatorModel import AkCalculatorModel
from src.controllers.akController import AkController
from src.views.akCalculatorView import AkCalculatorView

class AkCalculatorController(AkController):
    def __init__(self):
        AkController.__init__(self)
        self.model = AkCalculatorModel()
        self.view = AkCalculatorView(None)
