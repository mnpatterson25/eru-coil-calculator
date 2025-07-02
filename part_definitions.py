# part_definitions.py

# --- Fuse block sizes and part numbers ---
FUSE_BLOCK_SIZES = [30, 60]
FUSE_BLOCK_MODELS = {
    (3, 30): "60308T",
    (3, 60): "60608T",
    (1, 30): "LFT600301C-ND",
    (1, 60): "VFT600601C"
}

# --- Contactor sizes and part numbers ---
CONTACTOR_SIZES = [25, 40, 1000]
CONTACTOR_MODELS = {
    25: "DPE18B7",
    40: "DPE32B7"
}

# --- SCR sizes and part numbers ---
SCR_SIZES = [25, 40, 50, 70]
SCR_MODELS = {
    40: "SN480D40ZW",
    60: "SN480D60ZW"
}

# --- Disconnect models ---
DISCONNECT_MODELS = {
    ("STD", 25): "466-273",
    ("STD", 40): "466-277"
}

# --- Transformer wire colors ---
TRANSFORMER_WIRE_COLORS = {
    480: "Grey",
    277: "Yellow",
    240: "Orange",
    120: "Black",
    208: "RED"
}