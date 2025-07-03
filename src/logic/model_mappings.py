import pandas as pd
##############################################################################
############################## LOOKUP FUNCTIONS ##############################
##############################################################################
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
##############################################################################
def get_dip_switch(phase):
    if phase == 3:
        return "3,5,6"
    return "3,5"
##############################################################################
def get_conn_type(connection_type):
    if connection_type == "Wye":
        return "WYE"
    return "DELTA"
##############################################################################
def get_fb_model(f_unit, fb_amp):
    if f_unit == 3:
        return {30: "60308T", 60: "60608T"}.get(fb_amp, "x")
    return {30: "LFT600301C-ND", 60: "VFT600601C"}.get(fb_amp, "y")
##############################################################################
def get_c_model(c_amps):
    return {25: "DPE18B7", 40: "DPE32B7"}.get(c_amps, "x")
##############################################################################
def get_dc_model(dc_type, dc_amps):
    if dc_type == "STD":
        return {25: "466-273", 40: "466-277"}.get(dc_amps, "x")
    return "KNIFE EDGE"
##############################################################################
def get_scr_model(scr_amps):
    return "SN480D60ZW" if scr_amps > 40 else "SN480D40ZW"
##############################################################################
############################ ASSIGNMENT FUNCTIONS ############################
##############################################################################
def assign_transformer_wire(df):
    df["Transformer Wire Used"] = df["Voltage"].apply(lambda v: get_transformer_wire(v))
    return df
##############################################################################
def assign_fb_model(df):
    df["Fuse Block Model"] = df.apply(lambda x: get_fb_model(x.get("Fuses/Unit", 3), x.get("Fuse Block Amps", 0)), axis=1)
    return df
##############################################################################
def assign_c_model(df):
    df["Contactor Model"] = df["Contactor Amps"].apply(get_c_model)
    return df
##############################################################################
def assign_dc_model(df):
    df["Disconnect Model"] = df.apply(lambda x: get_dc_model(x.get("Disconnect Type", "STD"), x.get("Disconnect Amps", 0)), axis=1)
    return df
##############################################################################
def assign_scr_model(df):
    df["SCR Model"] = df["SCR Amps"].apply(get_scr_model)
    return df
##############################################################################