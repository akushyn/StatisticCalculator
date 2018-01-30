# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:32:43 2018

@author: Andriy
"""

import tkinter as tk
tk.root = tk.Tk()
tk.Button(tk.root, text = '1').pack(side = 'left')
tk.Button(tk.root, text = '2').pack(side = 'top')
tk.Button(tk.root, text = '3').pack(side = 'right')
tk.Button(tk.root, text = '4').pack(side = 'bottom')
tk.Button(tk.root, text = '5').pack(fill = 'both')

tk.root.mainloop()