# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 10:15:58 2018

@author: Andriy
"""

from src.models.akSummaryModel import AkSummaryModel
from src.views.akSummaryView import AkSummaryView

class AkSummaryController:
    def __init__(self):
        self.model = AkSummaryModel()
        self.view = AkSummaryView(None)
        