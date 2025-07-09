# main.py

import tkinter as tk
from gui.input_form import build_input_form
from gui.input_form import AppContext

root = tk.Tk()
root.title("VAV Coil Entry + Calculator")
root.geometry("1400x800")

context = AppContext()
build_input_form(root, context)

root.mainloop()