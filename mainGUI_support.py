# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:56:41 2018

@author: Andriy
"""

import sys
import tkinter.filedialog as fileDialog

def loadCSVFiles():
    print('mainGUI_support.loadCSVFiles')
    sys.stdout.flush()

    fn = fileDialog.Open(root, filetypes = [('*.csv files', '.csv')]).show()
    if fn == '':
        return
    print(fn)
  
def SaveFile(ev):
    fileName = fileDialog.SaveAs(root, filetypes = [('*.csv files', '.csv')]).show()
    if fileName == '':
        return
    if not fileName.endswith(".csv"):
        fileName+=".csv"
    #open(fn, 'wt').write(textbox.get('1.0', 'end'))

def calculate():
    print('mainGUI_support.calculate')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import mainGUI
    mainGUI.vp_start_gui()

