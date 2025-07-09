import tkinter as tk
from tkinter import ttk
from logic.components import LINE_WIRE_CALCULATIONS
from gui.tab_base import create_table

def create_wire_calc_tab(notebook, data):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Wire Size Calculations")
    create_table(frame, LINE_WIRE_CALCULATIONS, data)