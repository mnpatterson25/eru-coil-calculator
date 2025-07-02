import tkinter as tk
from tkinter import ttk
from logic.components import LINE_WIRE_FIELDS
from gui.tab_base import create_table

def create_detail_tab(notebook, data):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Line Wire Detail")
    create_table(frame, LINE_WIRE_FIELDS, data)