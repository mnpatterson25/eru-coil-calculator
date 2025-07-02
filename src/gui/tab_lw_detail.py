import tkinter as tk
from tkinter import ttk

# detail_tab.py
def create_detail_tab(notebook, data):
    from gui.tab_base import create_table
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Line Wire Detail")
    columns = ["Line Wire Size (AWG)", "Line Wire Color", "Line Wire Length (ft)"]
    create_table(frame, columns, data)
