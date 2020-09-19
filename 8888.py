# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:24:51 2020

@author: reaga
"""

import tkinter as tk
window=tk.Tk()


window.title("menu")
window.geometry("500x500")
menuBar=tk.Menu(window)
filemenu=tk.Menu(menuBar,tearoff=False)
filemenu.add_command(label="start")
filemenu.add_command(label="作弊")
filemenu.add_separator()
filemenu.add_command(label="exit")
menuBar.add_cascade(menu=filemenu)
filemenu2=tk.Menu(menuBar,tearoff=False)
filemenu2.add_command(label="八 ")
filemenu2.add_command(label="8  ")
menuBar.add_cascade(label="vv")
submenu=tk.Menu(filemenu2,tearoff=False)
submenu.add_command(label="888")
submenu.add_command(label="878")
filemenu2.add_cascade(label="999",menu=submenu)
window.config(menu=menuBar)
window.mainloop()
