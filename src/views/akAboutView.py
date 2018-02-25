# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:01:41 2018

@author: Andriy
"""
import wx

class AkAboutView(wx.Dialog):
 
    def __init__(self, parent):
 
        wx.Dialog.__init__(self, parent, wx.ID_ANY, title="About", size=(400,400))
 
        html = wxHTML(self)
 
        html.SetPage(
            ''
            
            "<h2>About the About Tutorial</h2>"
 
            "<p>This about box is for demo purposes only. It was created in June 2006"
 
            "by Mike Driscoll.</p>"
 
            "<p><b>Software used in making this demo:</h3></p>"
 
            '<p><b><a href="http://www.python.org">Python 2.4</a></b></p>'
 
            '<p><b><a href="http://www.wxpython.org">wxPython 2.8</a></b></p>'
            )
 
class wxHTML(wx.html.HtmlWindow):
     def OnLinkClicked(self, link):
            print("Event handler 'onAboutHandler' link clicked!")
