# components.py

# --- Line Wire Data ---
LINE_WIRE_CALCULATIONS = [
    "Line Current (Amps)",
    "Addl. 0.5 Amp",
    "125% Current",
    "Breaker",
    "Ampacity",
    "Line Wire Size (AWG)"
]

# --- Line Wire Fields ---
LINE_WIRE_FIELDS = [
    "Line Wire Size (AWG)",
    "Line Wire Color",
    "Line Wire Length (ft)"
]

# --- Control Wire Fields ---
CONTROL_WIRE_FIELDS = [
    "Control Wire Size (AWG)",
    "Control Wire Color",
    "Control Wire Length (ft)",
    "Control Wire Color2",
    "Control Wire Length2 (ft)",
]

# --- Ceramic Info ---
CERAMIC_INFO = [
    "Unit",
    "Passes",
    "Coils",
    "Ceramics",
    "Line",
    "Ceramics",
    "Coil End Post",
    "Ceramic Plug/Cap Sets",
    "Passes",
    "Number of Coils"
]

# --- Electrical Info ---
ELECTRICAL_COMPONENTS = {
    "Fuse Block Amps": "min_ge(FUSE_BLOCK_SIZES, breaker)",
    "Fuse Blocks/Unit": "1",
    "Fuse Amps": "breaker",
    "Fuses/Unit": "phase",
    "Contactor Amps": "min_ge(CONTACTOR_SIZES, current_125)",
    "Contactors/Unit": "1",
    "SCR Amps": "min_ge(SCR_SIZES, current_125)",
    "SCRs/Unit": "1",
    "Transformer VA": "'50' if '24V,50VA' in transformer_info else 'x'",
    "Transformers/Unit": "1",
    "Pressure Switch": "1",
    "Manual Reset": "1",
    "Auto Reset": "1",
    "Ground Lug": "1"
}

# --- Control Panel Info ---
CONTROL_PANEL_INFO = [
    "Size",
    "Disconnect",
    "Coil Handing",
    "Voltage",
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


        


# --- Coil Selection Info ---
COIL_SELECTION_INFO = [
    "Connection Type",
    "Resistance (ohm)",
    "Line Current",
    "Nichrome Wire Size (AWG)",
    "Number of Coils",
    "Passes",
    "Pitch",
    "Heat Element Length (in) per coil",
    "Unstretch Wounded Length (in)",
    "Stretched Wound Coil Length (in)",
    "Heat Element Length (ft) per unit"
]



# --- Basic Unit Info ---
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




# --- Input Form Columns (Main Entry Form) ---
INPUT_COLUMNS = [
    "Line", "Tag #", "Size", "Material", "Coil Handing",
    "Disconnect", "Transformer Voltage", "Voltage", "kW"
]

# --- Dropdown Options for Entry Fields ---
DROPDOWN_OPTIONS = {
    "Size": ["10x15", "10x21", "16x30"],
    "Material": ["Galvanized"],
    "Coil Handing": ["Left", "Right"],
    "Transformer Voltage": ["a", "b", "c"],
    "Voltage": ["480/3", "120/1"],
    "Disconnect": ["STD", "KE"]
}









coil_columns = [
    "Connection Type",
    "Resistance (ohm)",
    "Line Current",
    "Nichrome Wire Size (AWG)",
    "Number of Coils",
    "Passes",
    "Pitch",
    "Heat Element Length (in) per coil",
    "Unstretch Wounded Length (in)",
    "Stretched Wound Coil Length (in)",
    "Heat Element Length (ft) per unit"
]




