import math
from logic.constants import AWG_DATA, UNIT_SIZES

def calculate_coil_options(voltage, power_kw, unit_size, passes_num, phase=3, connection_type="wye"):
    pitch_min = 0.16
    pitch_max = 0.24

    if unit_size not in UNIT_SIZES:
        return []

    unit_width, unit_height = UNIT_SIZES[unit_size]
    B3 = unit_width
    B8 = 0.25
    B5 = unit_height / passes_num

    # Determine resistance (ohms) based on connection type
    if connection_type.lower() == "delta" and phase == 3:
        resistance = (phase * voltage ** 2) / (power_kw * 1000)
    else:
        resistance = (voltage ** 2) / (power_kw * 1000)

    # Line current (for reference)
    current_line_calc = round((power_kw * 1000) / (voltage * math.sqrt(3 if phase == 3 else 1)), 2)

    results = []
    for row in AWG_DATA:
        gauge_nichrome = row["Gauge"]
        diameter_nichrome = row["Diameter"]
        resistance_ft = row["Resistance"]

        # Step 1: Unwound length (in inches)
        length_he_in = (resistance / resistance_ft) * 12

        # Step 2: Wound length (unstretched)
        length_he_in_unstretched = length_he_in * diameter_nichrome / math.sqrt((math.pi * B8)**2 + diameter_nichrome**2)

        # Step 3: Geometry-based pitch
        B6 = (B3 - 2) * passes_num + math.pi * B5 * (passes_num - 1)
        try:
            denominator = (length_he_in ** 2) / (B6 ** 2) - 1
            if denominator <= 0:
                continue
            pitch_actual = math.sqrt(((math.pi * B8) ** 2) / denominator)
            pitch_rounded = round(pitch_actual, 2)
        except (ZeroDivisionError, ValueError):
            continue

        if not (pitch_min <= pitch_rounded <= pitch_max):
            continue

        # Step 4: Use rounded pitch to recalculate stretched length
        length_he_in_stretched = (length_he_in * pitch_rounded) / math.sqrt((math.pi * B8) ** 2 + pitch_rounded ** 2)

        # Step 5: Passes and coil details
        passes_possible = (length_he_in_stretched + math.pi * B5) / (B3 - 2 + math.pi * B5)
        passes_actual = math.floor(passes_possible)
        coils_qty = phase if phase == 3 else 1
        length_he_ft = (length_he_in / 12) * coils_qty 
        ceramics = passes_actual * 2 * coils_qty
        ceramics_posts = 2 * coils_qty
        ceramics_caps = 2 * coils_qty

        # Append result in correct order
        results.append({
            "Gauge": gauge_nichrome,  # Optional backward compatibility
            "Actual Passes": passes_actual,  # Optional backward compatibility
            "Actual Pitch": pitch_rounded,  # Optional backward compatibility
            "Connection Type": connection_type.capitalize(),
            "Resistance (ohm)": round(resistance, 4),
            "Line Current": current_line_calc,
            "Nichrome Wire Size (AWG)": gauge_nichrome,
            "Coils": coils_qty,            
            "Passes": passes_actual,
            "Pitch": pitch_rounded,
            "Heat Element Length (in) per coil": round(length_he_in, 2),
            "Unstretch Wounded Length (in)": round(length_he_in_unstretched, 2),
            "Stretched Wound Coil Length (in)": round(length_he_in_stretched, 2),
            "Heat Element Length (ft) per unit": round(length_he_ft, 2),
            "Ceramics": ceramics,
            "Coil End Post": ceramics_posts,
            "Ceramic Plug/Cap Sets": ceramics_caps,
        })

    return results