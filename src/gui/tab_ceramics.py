# tab_ceramics.py

from tkinter import ttk
from gui.tab_base import create_table

def add_ceramics_tab(notebook, data, coil_data):
    if not coil_data:
        return

    ceramic_frame = ttk.Frame(notebook)
    notebook.add(ceramic_frame, text="Ceramics")

    ceramic_columns = ["Unit", "Passes", "Coils", "Ceramics"]

    display_data = []

    for idx, coil in enumerate(coil_data):
        passes_raw = coil.get("Actual Passes", 0)
        coils_raw = coil.get("Number of Coils", 0)

        try:
            passes = int(passes_raw)
        except (ValueError, TypeError):
            passes = 0

        try:
            coils = int(coils_raw)
        except (ValueError, TypeError):
            coils = 0

        multiplier = 2  # Your original logic may have had this hardcoded
        ceramics = passes * multiplier * coils

        row = {
            "Unit": f"Unit {idx + 1}",
            "Passes": passes,
            "Coils": coils,
            "Ceramics": ceramics
        }
        display_data.append(row)

    create_table(ceramic_frame, ceramic_columns, display_data)
