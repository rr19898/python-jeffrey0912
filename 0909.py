# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:57:07 2020

@author: reaga
"""
from pytube import Youtube
import tkinter as tk
progress=0
def showProgess(stream,chunk,bytes_remaining):
    size=stream.filesize
    global progress
    preProgress= progress
    currentProgress=int((size-bytes_remaining)*100/size)
    progress=currentProgress
     if progress == 100:
         print("下載完成")
         return
     if preProgress != progress:
         scale.set(progress)
         window.update()
         print("目前進度"+str(congressProgress)+"%")
def onClick():
    global var
    var.set(entry.get())
        yt=Youtube(var.get(),on_progress_callback=showProgress)
        stream=yt.streams.first
        stream.downlaod()
    except:
        print(")
         
window = tk.Tk()
label = tk.Label(window, bg='#f00',text='請輸入網址')
label.pack()
var = tk.StringVar
entry.tk.Entry(window,width=50)
entry.pack()下載失敗"
window.title("Scale尺度")

scale = tk.Scale(window,label="進度條",
                 orient=tk.HORIZONTAL,
                 length=200)
scale.pack()
window.mainloop()