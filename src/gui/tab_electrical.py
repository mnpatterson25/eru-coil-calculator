# tab_electrical.py

from tkinter import ttk
from gui.tab_base import create_table
from logic.constants import FB_SIZES, CONTACTOR_SIZES, SCR_SIZE_RATINGS

def add_electrical_tab(notebook, data, coil_data):
    if not coil_data:
        return

    panel_frame = ttk.Frame(notebook)
    notebook.add(panel_frame, text="Electrical Info")

    panel_columns = [
        "Fuse Block Amps", "Fuse Blocks/Unit", "Fuse Amps", "Fuses/Unit",
        "Contactor Amps", "Contactors/Unit", "SCR Amps", "SCRs/Unit",
        "Transformer VA", "Transformers/Unit", "Pressure Switch", "Manual Reset",
        "Auto Reset", "Ground Lug"
    ]

    panel_data = []

    for unit in data:
        breaker = unit.get("Breaker", 0)
        current_125 = unit.get("125% Current", 0)
        phase = unit.get("Phase", 3)
        transformer_info = unit.get("Transformer Voltage", "").strip()

        def min_ge(values, threshold):
            return next((x for x in values if x >= threshold), "x")

        panel_data.append({
            "Fuse Block Amps": min_ge(FB_SIZES, breaker),
            "Fuse Blocks/Unit": 1,
            "Fuse Amps": breaker,
            "Fuses/Unit": phase,
            "Contactor Amps": min_ge(CONTACTOR_SIZES, current_125),
            "Contactors/Unit": 1,
            "SCR Amps": min_ge(SCR_SIZE_RATINGS, current_125),
            "SCRs/Unit": 1,
            "Transformer VA": "50" if "24V,50VA" in transformer_info else "x",
            "Transformers/Unit": 1,
            "Pressure Switch": 1,
            "Manual Reset": 1,
            "Auto Reset": 1,
            "Ground Lug": 1
        })

    create_table(panel_frame, panel_columns, panel_data)
