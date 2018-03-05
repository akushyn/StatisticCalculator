# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 22:46:47 2018

@author: Andriy
"""
from src.views.notebook.akNotebookPanelView import AkNotebookPanelView
from src.models.akNotebookModel import AkNotebookModel
from src.controllers.akJournalController import AkJournalController

class AkNotebookController():
    def __init__(self):
        self.model = AkNotebookModel()
        self.view = AkNotebookPanelView()
        
        self.journalController = AkJournalController()
        