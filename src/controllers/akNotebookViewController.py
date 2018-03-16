# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 22:46:47 2018

@author: Andriy
"""
from src.models.akNotebookModel import AkNotebookModel
from src.controllers.akController import AkController

class AkNotebookViewController(AkController):
    def __init__(self):
        AkController.__init__(self)
        self.model = AkNotebookModel()
       
        
