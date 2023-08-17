from tkinter import *
from tkinter import ttk
import listener

def create_window():
    root = Tk()
    root_frame = ttk.Frame(root, padding=400)
    root_frame.grid()

    ttk.Label(root_frame, text="~AUDIO VISUALISER~").grid(column=0, row=0)
    ttk.Button(root_frame, text="Listen", command=listener.fetch_decibels).grid(column=0, row=1)

    canvas = Canvas(root_frame, width=250, height=100)
    canvas.create_line()
        
    # style = ttk.Style()

    # style.theme_create('av', settings={
    #     'TFrame': {'configure': {'background': '#5A5A5A'}}
    # })

    # style.theme_use('av')
    root.mainloop()
    
create_window()