import tkinter as tk
from tkinter import ttk

# basic_tab.py
def create_basic_tab(notebook, data):
    from tab_base import create_table
    basic_frame = ttk.Frame(notebook)
    notebook.add(basic_frame, text="Basic Unit Info")
    columns = ["Line", "Tag #", "Size", "Disconnect", "Coil Handing", "kW", "Voltage", "Phase"]
    create_table(basic_frame, columns, data)