import tkinter as tk
from tkinter import ttk
from logic.components import BASIC_UNIT_INFO
from gui.tab_base import create_table

def create_basic_tab(notebook, data):
    basic_frame = ttk.Frame(notebook)
    notebook.add(basic_frame, text="Basic Unit Info")
    create_table(basic_frame, BASIC_UNIT_INFO, data)