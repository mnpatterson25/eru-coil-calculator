FB_SIZES = [30, 60]
CONTACTOR_SIZES = [25, 40, 1000]
DISCONNECT_SIZES = [25, 40, 1000]

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

SCR_SIZE_RATINGS = {
    20: 25,   # 25A SCR has 80% rating of 20A
    32: 40,   # 40A SCR → 32A
    40: 50,   # 50A SCR → 40A
    56: 70    # 70A SCR → 56A
}

AWG_DATA = [
    {"Gauge": 16, "Diameter": 0.0508, "Resistance": 0.2517},
    {"Gauge": 18, "Diameter": 0.0403, "Resistance": 0.4002},
    {"Gauge": 20, "Diameter": 0.0320, "Resistance": 0.6363},
    {"Gauge": 22, "Diameter": 0.0253, "Resistance": 1.0118},
    {"Gauge": 24, "Diameter": 0.0201, "Resistance": 1.6088},
    {"Gauge": 26, "Diameter": 0.0159, "Resistance": 2.5581},
]

UNIT_SIZES = {
    "10x15": (15, 10),
    "10x21": (21, 10),
    "16x30": (30, 16)
}