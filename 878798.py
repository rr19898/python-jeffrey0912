# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:06:49 2020

@author: reaga
"""

import tkinter as tk
window = tk.Tk()
window.title("單選按鈕")
string = tk.StringVar()
def selection():
    label.config(text="我喜歡"+string.get())
label = tk.Label(window, bg='#f00',text='尚未選擇')
label.pack()


radio1 = tk.Radiobutton(window,
                    text='Minecraft Python',
                    variable=string, value='Minecraft Python',
                    command=selection)
radio1.pack()
radio2 = tk.Radiobutton(window,
                    text='pygame',
                    variable=string, value='Pygame',
                    command=selection)
radio2.pack()
radio3 = tk.Radiobutton(window,
                    text='Tkinter',
                    variable=string, value='Tkinter',
                    command=selection)
radio3.pack()                    
window.mainloop()