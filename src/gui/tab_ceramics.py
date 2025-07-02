# tab_ceramics.py

from tkinter import ttk
from gui.tab_base import create_table

def safe_int(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return 0

def add_ceramics_tab(notebook, data, coil_data):
    if not coil_data:
        return

    ceramic_frame = ttk.Frame(notebook)
    notebook.add(ceramic_frame, text="Ceramics")

    ceramic_columns = ["Unit", "Passes", "Coils", "Ceramics"]
    display_data = []

    for idx, coil in enumerate(coil_data):
        passes = safe_int(coil.get("Actual Passes"))
        coils = safe_int(coil.get("Number of Coils"))
        ceramics = passes * 2 * coils

        row = {
            "Unit": f"Unit {idx + 1}",
            "Passes": passes,
            "Coils": coils,
            "Ceramics": ceramics
        }
        display_data.append(row)

    create_table(ceramic_frame, ceramic_columns, display_data)
