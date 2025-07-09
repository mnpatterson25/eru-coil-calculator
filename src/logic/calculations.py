import math
from logic.constants import *
#FUSE_SIZES, AMPACITY, CONTACTOR_SIZES, SCR_SIZE_RATINGS, DISCONNECT_SIZES, FB_SIZES
#from logic.coil_calculator import connection_type, passes_actual
from logic.coil_calculator import *

##############################################################################
############################# AMPERAGE FUNCTIONS #############################
##############################################################################
def get_contactor_amp(required_current):
    return next((size for size in CONTACTOR_SIZES if size >= required_current), "x")
##############################################################################
def get_scr_amp(required_current):
    for min_rating, scr_size in SCR_SIZE_RATINGS.items():
        if min_rating >= required_current:
            return scr_size
    return "x"
##############################################################################
def min_ge(values, target):
    return next((v for v in values if v >= target), "N/A")

from logic.components import *
from logic.coil_calculator import calculate_coil_options
from logic.model_mappings import *

line_no = 0

def process_unit_data(units):
    result = []

    for unit in units:
        ### GET DATA ###
        line_no = unit["Line"]
        tag_no = unit["Tag #"]
        unit_size = unit["Size"]
        material = unit["Material"]
        handing = unit["Coil Handing"]
        dc_type = unit["Disconnect"]
        tran_VA = unit["Transformer Voltage"]
        voltage_ph = unit["Voltage/Phase"]
        power_kw = unit["kW"]
        voltage = int(voltage_ph.split("/")[0]) if isinstance(voltage_ph, str) else int(voltage_ph)
        phase = int(unit.get("Phase", 3))

        #coil_data = calculate_coil_options(voltage, power_kw, unit_size, 3, phase, "wye")[:1]
        #unit.update(coil_data[0] if coil_data else {})

        ### CALCULATIONS ###
        current_base = (power_kw * 1000) / (voltage * math.sqrt(3 if phase == 3 else 1))
        current_lw = math.ceil(current_base)
        current_add_half = current_lw + 0.5
        current_125 = math.ceil(current_add_half * 1.25)
        breaker = next((b for b in FUSE_SIZES if b >= current_125), "N/A")
        gauge_lw = next((lwgauge for lwgauge, ampac in AMPACITY.items() if ampac >= breaker), "N/A")
        ampacity = AMPACITY.get(gauge_lw, "N/A")
        #try:
        #    gauge_lw_calc = next((g for g, a in AMPACITY.items() if a >= breaker))
        #    ampacity = AMPACITY[gauge_lw_calc]
        #except StopIteration:
        #    gauge_lw_calc, ampacity = "N/A"        
        #try:
        #    gauge_lw_val = int(gauge_lw_calc)
        #    gauge_lw = (
        #        "14" if gauge_lw_val >= 14 else
        #        "12" if gauge_lw_val == 12 else
        #        "8" if gauge_lw_val in (10, 8) else
        #        "ERROR"
        #    )
        #except:
        #    gauge_lw = "ERROR"

        #unit.update(updated_fields)
        ### SINGLE VALUE UPDATES ###
        fb_amps = next((size for size in FB_SIZES if size >= breaker), "N/A")
        f_amps = breaker
        f_unit = phase
        c_amps = next((size for size in CONTACTOR_SIZES if size >= current_125), "N/A")
        dc_amps = next((size for size in DISCONNECT_SIZES if size >= current_125), "N/A")
        scr_amps = next((size for size in SCR_SIZE_RATINGS if size >= current_125), "N/A")
        unit["T_VA"] = "50" if str(unit.get("Transformer Voltage", "")).startswith("24V,50VA") else "x"
        result.append(unit)

        ### FIELD UPDATES ###
        unit.update({
            # BASIC TAB
            "Line": line_no,
            "Tag #": tag_no,
            "Size": unit_size,
            "Disconnect": dc_type,
            "Coil Handing": handing,
            "kW": power_kw,
            "Voltage": voltage,
            "Phase": phase,
            # WIRE SIZE CALC TAB
            "Line Current (Amps)": current_lw,
            "Addl. 0.5 Amp": current_add_half,
            "125% Current": current_125,
            "Breaker": breaker,
            "Ampacity": ampacity,
            "Line Wire Size (AWG)": gauge_lw,
            # LINE WIRE DETAIL TAB
            "Line Wire Color": color_lw,
            "Line Wire Length (ft)": length_lw,
            # CONTROL WIRE DETAIL TAB
            "Control Wire Size (AWG)": gauge_cw,
            "Control Wire Color": color_cw1,
            "Control Wire Length 1 (ft)": length_cw1,
            "Control Wire Color 2": color_cw2,
            "Control Wire Length 2 (ft)": length_cw2,
            # CERAMICS TAB
            #"Unit": line_no,
            #"Passes": passes_actual,
            #"Coils": coils_qty,
            #"Ceramics": ceramics,
            #"Coil End Post": ceramics_posts,
            #"Ceramic Plug/Cap Sets": ceramics_caps,
            # ELECTRICAL INFO TAB
            "Fuse Block Amps": min_ge(FB_SIZES, breaker),
            "Fuse Blocks/Unit": fb_unit,
            "Fuse Amps": min_ge(FUSE_SIZES, breaker),
            "Fuses/Unit": phase,
            "Contactor Amps": min_ge(CONTACTOR_SIZES, current_125),
            "Contactors/Unit": c_unit,
            "Disconnect Amps": min_ge(DISCONNECT_SIZES, current_125),
            "Disconnect/Unit": dc_unit,
            "SCR Amps": min_ge(SCR_SIZE_RATINGS, current_125),
            "SCRs/Unit": scr_unit,
            #"Transformer VA": "'50' if '24V,50VA' in transformer_info else 'x'",
            "Transformers/Unit": tran_unit,
            "Pressure Switch": p_switch,
            "Manual Reset": man_reset,
            "Auto Reset": auto_reset,
            "Ground Lug": ground_lug,
            # CONTROL PANEL INFO TAB
            #"Connection Type": get_conn_type(connection_type),
            "Dip Switch": get_dip_switch(phase),
            "Transformer Wire Used": get_transformer_wire(voltage),
            "Fuse Block Model": get_fb_model(f_unit, fb_amps),
            "Contactor Model": get_c_model(c_amps),
            "Disconnect Model": get_dc_model(dc_type, dc_amps),
            "SCR Model": get_scr_model(scr_amps)
        })

    return result