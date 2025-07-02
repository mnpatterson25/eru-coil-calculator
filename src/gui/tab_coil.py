# tab_coil.py

from tkinter import ttk
from gui.tab_base import create_table

def add_coil_tab(notebook, data, coil_data):
    if not coil_data:
        return

    coil_frame = ttk.Frame(notebook)
    notebook.add(coil_frame, text="Selected Coils")

    coil_columns = [
        "Connection Type", "Resistance (ohm)", "Line Current",
        "Nichrome Wire Size (AWG)", "Number of Coils", "Passes", "Pitch",
        "Heat Element Length (in) per coil", "Unstretch Wounded Length (in)",
        "Stretched Wound Coil Length (in)", "Heat Element Length (ft) per unit"
    ]

    display_data = []
    for unit in data:
        selected = unit.get("Selected Coil", {})
        row = {col: selected.get(col, selected.get("Gauge", "")) for col in coil_columns}
        display_data.append(row)

    create_table(coil_frame, coil_columns, display_data)