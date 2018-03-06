# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 10:16:06 2018

@author: Andriy
"""

from src.models.akGraphsModel import AkGraphsModel
from src.views.akGraphsView import AkGraphsView

class AkGraphsController:
    def __init__(self):
        self.model = AkGraphsModel()
        self.view = AkGraphsView(None)