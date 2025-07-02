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