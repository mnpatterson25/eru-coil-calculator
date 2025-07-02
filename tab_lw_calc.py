import tkinter as tk
from tkinter import ttk

# wire_calc_tab.py
def create_wire_calc_tab(notebook, data):
    from tab_base import create_table
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Wire Size Calculations")
    columns = ["Line Current (Amps)", "Addl. 0.5 Amp", "125% Current", "Breaker", "Ampacity", "Wire Gauge"]
    create_table(frame, columns, data)