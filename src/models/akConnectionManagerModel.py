# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:01:43 2018

@author: Andriy
"""
from pubsub import publish

class AkConnectionManagerModel:
    def __init_(self):
        self._connections = []
        
    
    def addConnection(self, connectionName):
        self.connections.append(connectionName)
        publish.sendMessage("connections_changed", connection=connectionName)
        
    def deleteConnection(self, connectionName):
        self.connections.remove(connectionName)
        publish.sendMessage("connections_changed", connection=connectionName)