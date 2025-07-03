# components.py




##############################################################################
################################# TAB LISTS ##################################
##############################################################################
# Values in calculations.py

BASIC_UNIT_INFO = [
    "Line",
    "Tag #",
    "Size",
    "Disconnect",
    "Coil Handing",
    "kW",
    "Voltage",
    "Phase"
]

LINE_WIRE_CALCULATIONS = [
    "Line Current (Amps)",
    "Addl. 0.5 Amp",
    "125% Current",
    "Breaker",
    "Ampacity",
    "Line Wire Size (AWG)"
]

LINE_WIRE_FIELDS = [
    "Line Wire Size (AWG)",
    "Line Wire Color",
    "Line Wire Length (ft)"
]

CONTROL_WIRE_FIELDS = [
    "Control Wire Size (AWG)",
    "Control Wire Color",
    "Control Wire Length 1 (ft)",
    "Control Wire Color 2",
    "Control Wire Length 2 (ft)",
]

CERAMIC_INFO = [
    "Unit",
    "Passes",
    "Coils",
    "Ceramics",
    "Coil End Post",
    "Ceramic Plug/Cap Sets",
]

ELECTRICAL_COMPONENTS = [
    "Fuse Block Amps",
    "Fuse Blocks/Unit",
    "Fuse Amps",
    "Fuses/Unit",
    "Contactor Amps",
    "Contactors/Unit",
    "SCR Amps",
    "SCRs/Unit",
    "Transformer VA",
    "Transformers/Unit",
    "Pressure Switch",
    "Manual Reset",
    "Auto Reset",
    "Ground Lug",
]

CONTROL_PANEL_INFO = [
    "Size",
    "Disconnect",
    "Coil Handing",
    "Voltage",
    "Phase",
    "Connection Type",
    "Passes",
    "Line Wire Size (AWG)",   
    "Fuse Block Amps",
    "Fuse Amps",
    "Fuses/Unit",
    "Contactor Amps",
    "Disconnect Amps",
    "SCR Amps",
    "Dip Switch",
    "Transformer Wire Used",
    "Fuse Block Model",    
    "Contactor Model",
    "Disconnect Model",
    "SCR Model"
]

##############################################################################
##############NEW STUFF#######################################################
##############################################################################
gauge_cw = 18
color_lw = "XX"
color_cw1 = "XX"
color_cw2 = "XX"
length_lw = "XX"
length_cw1 = "XX"
length_cw2 = "XX"
##############################################################################
fb_unit = 1
c_unit = 1
dc_unit = 1
scr_unit = 1
tran_unit = 1
p_switch = 1
man_reset = 1
auto_reset = 1
ground_lug = 1
##############################################################################
#import math
#from logic.constants import FUSE_SIZES, AMPACITY, FB_SIZES, SCR_SIZE_RATINGS, CONTACTOR_SIZES, DISCONNECT_SIZES
#from logic.coil_calculator import connection_type, passes_actual, coils_qty
#from gui.tab_ceramics import ceramics
#from logic.calculations import power_kw, voltage, phase
#############################################################################
#dip_switch =
##############################################################################
#passes_actual = passes_actual
#coils_qty = coils_qty
#ceramics = ceramics
#ceramics_posts = coils_qty * 2
#ceramics_caps = coils_qty * 2
##############################################################################
#connection_type = connection_type.capitalize()