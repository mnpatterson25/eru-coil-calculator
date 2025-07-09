import tkinter as tk
from tkinter import ttk
from gui.tab_base import create_table
from logic.components import LINE_WIRE_FIELDS
from logic.components import LINE_WIRE_CALCULATIONS
from logic.components import CONTROL_WIRE_FIELDS
from logic.components import CONTROL_PANEL_INFO
from logic.components import CERAMIC_INFO
from logic.components import BASIC_UNIT_INFO

def add_basic_tab(notebook, data):
    basic_frame = ttk.Frame(notebook)
    notebook.add(basic_frame, text="Basic Unit Info")
    create_table(basic_frame, BASIC_UNIT_INFO, data)

def add_detail_tab(notebook, data):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Line Wire Detail")
    create_table(frame, LINE_WIRE_FIELDS, data)

def add_wire_calc_tab(notebook, data):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Wire Size Calculations")
    create_table(frame, LINE_WIRE_CALCULATIONS, data)

def add_control_wire_tab(notebook, data):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Control Wire Detail")
    create_table(frame, CONTROL_WIRE_FIELDS, data)

def add_control_panel_tab(notebook, data):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Control Panel Info")
    create_table(frame, CONTROL_PANEL_INFO, data)

def add_ceramics_tab(notebook, data):
    ceramic_frame = ttk.Frame(notebook)
    notebook.add(ceramic_frame, text="Ceramics")
    create_table(ceramic_frame, CERAMIC_INFO, data)