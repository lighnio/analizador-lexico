import tkinter as tk

# Configuration
width = 300
height = 100
labelText = 'Hello Everyone'

root = tk.Tk()

def createMain():
    root.mainloop()

def addLabel():
    label = tk.Label(root, text=labelText, padx=width, pady=height)
    label.pack()