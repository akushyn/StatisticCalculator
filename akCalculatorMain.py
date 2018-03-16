# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:00:38 2018

@author: Andriy
"""

import wx
import gettext

from src.controllers.akCalculatorController import AkCalculatorController

class AkCalculatorMain(wx.App):
    def OnInit(self):
        
        self.controller = AkCalculatorController()
        self.SetTopWindow(self.controller.view)
        
        
        self.controller.view.Show()
        return True

if __name__ == "__main__":
    gettext.install("app") 

    app = AkCalculatorMain(0)
    app.MainLoop()