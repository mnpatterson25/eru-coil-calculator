# tab_control_panel.py
from tkinter import ttk
from tab_base import create_table

def add_control_panel_tab(notebook, data):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Control Panel Info")

    control_panel_columns = [
        "Size", "Disconnect", "Handing", "Voltage", "Connection Type", "Passes", "Line Wire Size (AWG)",
        "Fuse Block Amps", "Fuse Amps", "Fuses/Unit", "Contactor Amps", "Disconnect Amps", "SCR Amps",
        "Dip Switch", "Transformer Wire Used", "Fuse Block Model", "Contactor Model",
        "Disconnect Model", "SCR Model"
    ]

    create_table(frame, control_panel_columns, data)
