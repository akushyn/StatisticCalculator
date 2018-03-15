# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:59:27 2018

@author: Andriy
"""

#!/usr/bin/python
 
import wx
 
def onButton(event):
    print("Button pressed.")
 
app = wx.App()
 
frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,200,50)
 
# Create text input
dlg = wx.TextEntryDialog(frame, 'Enter some text','Text Entry')
dlg.SetValue("Default")
if dlg.ShowModal() == wx.ID_OK:
    print('You entered: %s\n' % dlg.GetValue())
dlg.Destroy()