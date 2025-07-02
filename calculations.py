# calculations.py

import math
import pandas as pd

FUSE_SIZES = [
    1, 2, 3, 6, 10, 15, 20, 25, 30, 35, 40, 45, 50,
    60, 70, 80, 90, 100, 110, 125, 150, 175, 200,
    225, 250, 300, 350, 400, 450, 500, 600, 800
]

AMPACITY = {
    "18": 10,
    "16": 13,
    "14": 18,
    "12": 25,
    "10": 30,
    "8": 55,
    "6": 75,
    "4": 95,
    "3": 110
}

CONTACTOR_SIZES = [25, 40, 1000]

SCR_SIZE_RATINGS = {
    20: 25,   # 25A SCR has 80% rating of 20A
    32: 40,   # 40A SCR → 32A
    40: 50,   # 50A SCR → 40A
    56: 70    # 70A SCR → 56A
}

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
            "Addl. .5 Amp": add_current,
            "125% Current": current_125,
            "Wire Gauge": wire,
            "Ampacity": amp,
            "Breaker": breaker,
            "Line Wire Size (AWG)": lw_size,
            "Line Wire Color": "",
            "Line Wire Length (ft)": "",
            "CW_Size (AWG)": "18",
            "CW_Color": "",
            "CW_Length (ft)": "",
            "CW_Color2": "",
            "CW_Length (ft) 2": "",
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

def get_transformer_wire(voltage):
    try:
        v = int(voltage)
    except:
        return "NO COLOR"
    return {
        480: "Grey",
        277: "Yellow",
        240: "Orange",
        120: "Black",
        208: "RED"
    }.get(v, "NO COLOR")

def get_fuse_block_model(f_per_unit, fb_amp):
    if f_per_unit == 3:
        return {30: "60308T", 60: "60608T"}.get(fb_amp, "x")
    return {30: "LFT600301C-ND", 60: "VFT600601C"}.get(fb_amp, "y")

def get_contactor_model(c_amps):
    return {25: "DPE18B7", 40: "DPE32B7"}.get(c_amps, "x")

def get_disconnect_model(disconnect_type, disconnect_amps):
    if disconnect_type == "STD":
        return {25: "466-273", 40: "466-277"}.get(disconnect_amps, "x")
    return "KNIFE EDGE"

def get_scr_model(scr_amps):
    return "SN480D60ZW" if scr_amps > 40 else "SN480D40ZW"
