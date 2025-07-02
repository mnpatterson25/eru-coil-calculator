# results_display.py

import tkinter as tk
from tkinter import ttk, messagebox
from gui.coil_popup import show_coil_selection_popup
from gui.tab_base import create_table
from gui.tab_basic import create_basic_tab as add_basic_tab
from gui.tab_lw_calc import create_wire_calc_tab as add_wire_calc_tab
from gui.tab_lw_detail import create_detail_tab as add_detail_tab
from gui.tab_cw_detail import create_control_wire_tab as add_control_tab
from gui.tab_coil import add_coil_tab
from gui.tab_ceramics import add_ceramics_tab
from gui.tab_electrical import add_electrical_tab
from gui.tab_control_panel import add_control_panel_tab

# Global state for refresh purposes
input_frame_global = None
processed_data_global = None
coil_data_global = None

result_container = None

def show_results(data, input_frame, coil_data=None):
    global result_container, input_frame_global, processed_data_global, coil_data_global

    input_frame_global = input_frame
    processed_data_global = data
    coil_data_global = coil_data

    if result_container:
        result_container.destroy()

    result_container = ttk.Frame(input_frame.master)
    result_container.pack(fill="both", expand=True, pady=20)

    notebook = ttk.Notebook(result_container)
    notebook.pack(fill="both", expand=True)

    add_basic_tab(notebook, data)
    add_wire_calc_tab(notebook, data)
    add_detail_tab(notebook, data)
    add_control_tab(notebook, data)    
    add_ceramics_tab(notebook, data, coil_data)
    add_electrical_tab(notebook, data, coil_data)
    add_control_panel_tab(notebook, data)
    add_coil_tab(notebook, data, coil_data)

def refresh_all_tabs():
    if processed_data_global and input_frame_global:
        show_results(processed_data_global, input_frame_global, coil_data_global)