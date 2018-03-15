# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 08:24:12 2018

@author: Andriy
"""

class AkController(object):
    def __init__(self):
        self.model = None
        self.view = None
        self.views = []

    def GetModel(self):
        return self.model

    def GetView(self):
        return self.view

    def Register(self, view):
        self.view = view
        self.views.append(view)

    def Unregister(self, view):
        if view in self.views:
            self.views.remove(view)

    def Notify(self, event):
        for view in self.views:
            view.update(event)
        
class AkControllerService(object):
    def __init__(self):
        self.origin = None
        self.target = None

    def AddOrigin(self, origin):
        self.origin = origin

    def AddTarget(self, target):
        self.target = target

    def Redirect(self, event):
        if self.target:
            self.target.notify(event)
        else:
            print("No target controller found.")