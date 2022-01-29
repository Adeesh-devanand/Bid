import tkinter

def clearRoot(root):
    for widgets in root.winfo_children():
        widgets.destroy()
