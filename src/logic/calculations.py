# calculations.py

import math
import pandas as pd
from logic.model_mappings import (
    get_transformer_wire,
    get_fuse_block_model,
    get_contactor_model,
    get_disconnect_model,
    get_scr_model
)
from logic.constants import FUSE_SIZES, AMPACITY, CONTACTOR_SIZES, SCR_SIZE_RATINGS

def apply_default_unit_fields(unit):
    unit.update({
        "Line Wire Color": "",
        "Line Wire Length (ft)": "",
        "Control Wire Size (AWG)": "18",
        "Control Wire Color": "",
        "Control Wire Length (ft)": "",
        "Control Wire Color2": "",
        "Control Wire Length2 (ft)": "",
    })
        
def get_contactor_amp(required_current):
    return next((size for size in CONTACTOR_SIZES if size >= required_current), "x")

def get_scr_amp(required_current):
    for min_rating, scr_size in SCR_SIZE_RATINGS.items():
        if min_rating >= required_current:
            return scr_size
    return "x"

def process_unit_data(units):
    result = []

    for unit in units:
        voltage = unit["Voltage"]
        kw = unit["kW"]
        voltage_val = int(voltage.split("/")[0]) if isinstance(voltage, str) else int(voltage)
        phase = int(unit.get("Phase", 3))

        base_current = (kw * 1000) / (voltage_val * math.sqrt(3 if phase == 3 else 1))
        line_current = math.ceil(base_current)
        add_current = line_current + 0.5
        current_125 = math.ceil(add_current * 1.25)
        breaker = next((b for b in FUSE_SIZES if b >= current_125), "N/A")

        try:
            wire = next((g for g, a in AMPACITY.items() if a >= breaker))
            amp = AMPACITY[wire]
        except StopIteration:
            wire = "N/A"
            amp = "N/A"

        try:
            wire_val = int(wire)
            if wire_val >= 14:
                lw_size = "14"
            elif wire_val == 12:
                lw_size = "12"
            elif wire_val == 10 or wire_val == 8:
                lw_size = "8"
            else:
                lw_size = "ERROR"
        except:
            lw_size = "ERROR"

        unit.update({
            "Phase": phase,
            "Line Current (Amps)": line_current,
            "Addl. 0.5 Amp": add_current,
            "125% Current": current_125,
            "Wire Gauge": wire,
            "Ampacity": amp,
            "Breaker": breaker,
            "Line Wire Size (AWG)": lw_size,
            #"Line Wire Color": "",
            #"Line Wire Length (ft)": "",
            #"CW_Size (AWG)": "18",
            #"CW_Color": "",
            #"CW_Length (ft)": "",
            #"CW_Color2": "",
            #"CW_Length (ft) 2": "",
            "Disconnect Type": unit.get("Disconnect", "STD"),
            "Dip Switch": "3,5,6",
        })

        unit["FB_Amp"] = 30 if breaker <= 30 else 60 if breaker <= 60 else "x"
        unit["F_Amps"] = breaker
        unit["F_Per Unit"] = phase
        unit["C_Amps"] = get_contactor_amp(current_125)
        unit["Disconnect Amps"] = get_contactor_amp(current_125)
        unit["SCR_Amps"] = get_scr_amp(current_125)
        unit["T_VA"] = "50" if str(unit.get("Transformer Voltage", "")).startswith("24V,50VA") else "x"

        result.append(unit)

    return result

def enrich_control_panel_info(data):
    df = pd.DataFrame(data)

    df["FB_Per unit"] = 1
    df["C_Per unit"] = 1
    df["SCR_Per unit"] = 1
    df["T_Per unit"] = 1
    df["Pressure switch"] = 1
    df["Man Reset"] = 1
    df["Auto Reset"] = 1
    df["Ground lug"] = 1

    df["Transformer Wire Used"] = df["Voltage"].apply(lambda v: get_transformer_wire(v))
    df["Fuse Block Model"] = df.apply(lambda x: get_fuse_block_model(x.get("F_Per Unit", 3), x.get("FB_Amp", 0)), axis=1)
    df["Contactor Model"] = df["C_Amps"].apply(get_contactor_model)
    df["Disconnect Model"] = df.apply(lambda x: get_disconnect_model(x.get("Disconnect Type", "STD"), x.get("Disconnect Amps", 0)), axis=1)
    df["SCR Model"] = df["SCR_Amps"].apply(get_scr_model)

    return df.to_dict(orient="records")


