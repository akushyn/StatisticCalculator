# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:46:33 2018

@author: Andriy
"""

class AkJournalNoteItemModel:
    def __init__(self, date, note):
            self._date = date
            self._note = note
    def GetDate(self):
        return self._date
    
    def GetNote(self):
        return self._note
    
    def ToString(self):
        return ' '.join([self._date, self._note])
        
class AkJournalModel():
    def __init__(self):
        self._notes = []
    
    def GetNotes(self):
        return self._notes
    
    def AddNoteItem(self, noteItem):
        self._notes.append(noteItem)
                
    def GetCount(self):
        return len(self._notes)
        
    def GetItem(self, idx):
        item = self._notes[idx]
        return AkJournalNoteItemModel(item.GetDate(), item.GetNote())
             