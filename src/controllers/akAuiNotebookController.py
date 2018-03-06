# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 22:46:47 2018

@author: Andriy
"""
from src.models.akAuiNotebookModel import AkAuiNotebookModel

class AkAuiNotebookController():
    def __init__(self, view):
        self.model = AkAuiNotebookModel()
        self.view = view
        