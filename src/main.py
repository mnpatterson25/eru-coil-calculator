# main.py

import tkinter as tk
from gui.input_form import build_input_form

root = tk.Tk()
root.title("VAV Coil Entry + Calculator")
root.geometry("1400x800")

build_input_form(root)

root.mainloop()
