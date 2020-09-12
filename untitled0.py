# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:59:02 2020

@author: reaga
"""
import tkinter.messagebox
import tkinter as tk
def clickme():
    tkinter.messagebox.showinfo(title="恭喜",message='恭喜')
window = tk.Tk()
window.title("睿家的第一個GUI")
window.geometry("300x300")


label = tk.Label(window,text="請輸入您的instagram帳密",bg="#ADFEDC",fg="#123321")
label.pack()
entry=tk.Entry(window,width=20)
entry.pack()

button = tk.Button(window,text="完成",command = clickme)
button.pack()
window.mainloop()
