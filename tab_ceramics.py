# tab_ceramics.py

from tkinter import ttk
from tab_base import create_table

def calculate_ceramic_parts(size, passes, coils):
    ceramic_multiplier = {
        "10x15": 4,
        "10x21": 6,
        "16x30": 8
    }
    multiplier = ceramic_multiplier.get(size, 0)
    return {
        "Ceramics": (passes or 0) * multiplier * (coils or 0),
        "Coil End Post": (coils or 0) * 2,
        "Ceramic Plug/Cap Sets": (coils or 0) * 2
    }


def add_ceramics_tab(notebook, data, coil_data):
    if not coil_data:
        return

    ceramic_frame = ttk.Frame(notebook)
    notebook.add(ceramic_frame, text="Ceramics")

    ceramic_columns = ["Ceramics", "Coil End Post", "Ceramic Plug/Cap Sets"]
    display_data = []

    for unit in data:
        selected = unit.get("Selected Coil", {})
        size = unit.get("Size", "")
        passes = selected.get("Passes", 0)
        coils = selected.get("Number of Coils", 0)
        part_data = calculate_ceramic_parts(size, passes, coils)
        display_data.append(part_data)


    create_table(ceramic_frame, ceramic_columns, display_data)