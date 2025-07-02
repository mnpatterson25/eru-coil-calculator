import tkinter as tk
from tkinter import ttk
from logic.components import CONTROL_WIRE_FIELDS
from gui.tab_base import create_table

# control_wire_tab.py
def create_control_wire_tab(notebook, data):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Control Wire Detail")
    create_table(frame, CONTROL_WIRE_FIELDS, data)






    