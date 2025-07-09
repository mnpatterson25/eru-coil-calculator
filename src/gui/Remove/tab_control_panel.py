import tkinter as tk
from tkinter import ttk
from logic.components import CONTROL_PANEL_INFO
from gui.tab_base import create_table

def add_control_panel_tab(notebook, data):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Control Panel Info")
    create_table(frame, CONTROL_PANEL_INFO, data)