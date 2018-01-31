# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:55:27 2018

@author: Andriy
"""

import tkinter as tk
import mainGUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = AkStatisticCalculator (root)
    mainGUI_support.init(root, top)
    root.mainloop()

w = None
def create_StatisticCalcForm(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = AkStatisticCalculator (w)
    mainGUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_AkStatisticCalculator():
    global w
    w.destroy()
    w = None


class AkStatisticCalculator:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        top.geometry("800x580+319+82")
        top.title("StatisticCalculator")
        top.configure(background="#d9d9d9")



        self.btnLoad = tk.Button(top)
        self.btnLoad.place(relx=0.8, rely=0.1, height=24, width=57)
        self.btnLoad.configure(activebackground="#d9d9d9")
        self.btnLoad.configure(activeforeground="#000000")
        self.btnLoad.configure(background="#d9d9d9")
        self.btnLoad.configure(command=mainGUI_support.loadCSVFile)
        self.btnLoad.configure(disabledforeground="#a3a3a3")
        self.btnLoad.configure(foreground="#000000")
        self.btnLoad.configure(highlightbackground="#d9d9d9")
        self.btnLoad.configure(highlightcolor="black")
        self.btnLoad.configure(pady="0")
        self.btnLoad.configure(text='''Load''')
        self.btnLoad.configure(width=57)

        self.btnCalc = tk.Button(top)
        self.btnCalc.place(relx=0.89, rely=0.1, height=24, width=57)
        self.btnCalc.configure(activebackground="#d9d9d9")
        self.btnCalc.configure(activeforeground="#000000")
        self.btnCalc.configure(command=mainGUI_support.calculate)
        self.btnCalc.configure(background="#d9d9d9")
        self.btnCalc.configure(disabledforeground="#a3a3a3")
        self.btnCalc.configure(foreground="#000000")
        self.btnCalc.configure(highlightbackground="#d9d9d9")
        self.btnCalc.configure(highlightcolor="black")
        self.btnCalc.configure(pady="0")
        self.btnCalc.configure(text='''Calc''')
        self.btnCalc.configure(width=57)


if __name__ == '__main__':
    vp_start_gui()


