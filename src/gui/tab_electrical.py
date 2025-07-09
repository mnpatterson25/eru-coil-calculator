from tkinter import ttk
from gui.tab_base import create_table
from logic.constants import FB_SIZES, CONTACTOR_SIZES, SCR_SIZE_RATINGS
from logic.components import ELECTRICAL_COMPONENTS
from logic.components import *

def add_electrical_tab(notebook, data, coil_data):
    if not coil_data:
        return

    panel_frame = ttk.Frame(notebook)
    notebook.add(panel_frame, text="Electrical Info")

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
            "Fuse Blocks/Unit": fb_unit,
            "Fuse Amps": breaker,
            "Fuses/Unit": phase,
            "Contactor Amps": min_ge(CONTACTOR_SIZES, current_125),
            "Contactors/Unit": c_unit,
            "SCR Amps": min_ge(SCR_SIZE_RATINGS, current_125),
            "SCRs/Unit": scr_unit,
            "Transformer VA": "50" if "24V,50VA" in transformer_info else "x",
            "Transformers/Unit": tran_unit,
            "Pressure Switch": p_switch,
            "Manual Reset": man_reset,
            "Auto Reset": auto_reset,
            "Ground Lug": ground_lug
        })
    create_table(panel_frame, ELECTRICAL_COMPONENTS, panel_data)
