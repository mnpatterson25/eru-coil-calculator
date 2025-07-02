import tkinter as tk
from tkinter import ttk

# control_wire_tab.py
def create_control_wire_tab(notebook, data):
    from tab_base import create_table
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Control Wire Size")
    columns = ["Size (AWG)", "Color", "Length (ft)", "Color2", "Length2 (ft)"]
    create_table(frame, columns, data)