# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:32:43 2018

@author: Andriy
"""
import tkinter as tk
import tkinter.filedialog as fileDialog

def Quit(ev):
    global root
    root.destroy()
    
def LoadFile(ev): 
    fn = fileDialog.Open(root, filetypes = [('*.csv files', '.csv')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end') 
    textbox.insert('1.0', open(fn, 'rt').read())
    
def SaveFile(ev):
    fn = fileDialog.SaveAs(root, filetypes = [('*.csv files', '.csv')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn+=".txt"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))

root = tk.Tk()

panelFrame = tk.Frame(root, height = 60, bg = 'gray')
textFrame = tk.Frame(root, height = 340, width = 600)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

textbox = tk.Text(textFrame, font='Arial 14', wrap='word')
scrollbar = tk.Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

loadBtn = tk.Button(panelFrame, text = 'Load')
saveBtn = tk.Button(panelFrame, text = 'Save')
quitBtn = tk.Button(panelFrame, text = 'Quit')

loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x = 10, y = 10, width = 40, height = 40)
saveBtn.place(x = 60, y = 10, width = 40, height = 40)
quitBtn.place(x = 110, y = 10, width = 40, height = 40)

root.mainloop()