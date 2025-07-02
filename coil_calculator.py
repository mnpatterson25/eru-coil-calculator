import math

awg_data = [
    {"Gauge": 16, "Diameter": 0.0508, "Resistance": 0.2517},
    {"Gauge": 18, "Diameter": 0.0403, "Resistance": 0.4002},
    {"Gauge": 20, "Diameter": 0.0320, "Resistance": 0.6363},
    {"Gauge": 22, "Diameter": 0.0253, "Resistance": 1.0118},
    {"Gauge": 24, "Diameter": 0.0201, "Resistance": 1.6088},
    {"Gauge": 26, "Diameter": 0.0159, "Resistance": 2.5581},
]

unit_sizes = {
    "10x15": (15, 10),
    "10x21": (21, 10),
    "16x30": (30, 16)
}

def calculate_coil_options(voltage, power_kw, unit_size, num_passes, phase=3, connection_type="wye"):
    pitch_min = 0.16
    pitch_max = 0.24

    if unit_size not in unit_sizes:
        return []

    unit_width, unit_height = unit_sizes[unit_size]
    B3 = unit_width
    B8 = 0.25
    B5 = unit_height / num_passes

    # Determine resistance (ohms) based on connection type
    if connection_type.lower() == "delta" and phase == 3:
        resistance = (phase * voltage ** 2) / (power_kw * 1000)
    else:
        resistance = (voltage ** 2) / (power_kw * 1000)

    # Line current (for reference)
    line_current = round((power_kw * 1000) / (voltage * math.sqrt(3 if phase == 3 else 1)), 2)

    results = []
    for row in awg_data:
        gauge = row["Gauge"]
        diameter = row["Diameter"]
        resistance_per_ft = row["Resistance"]

        # Step 1: Unwound length (in inches)
        unwound_length = (resistance / resistance_per_ft) * 12

        # Step 2: Wound length (unstretched)
        unstretch_wound = unwound_length * diameter / math.sqrt((math.pi * B8)**2 + diameter**2)

        # Step 3: Geometry-based pitch
        B6 = (B3 - 2) * num_passes + math.pi * B5 * (num_passes - 1)
        try:
            denominator = (unwound_length ** 2) / (B6 ** 2) - 1
            if denominator <= 0:
                continue
            actual_pitch = math.sqrt(((math.pi * B8) ** 2) / denominator)
            rounded_pitch = round(actual_pitch, 2)
        except (ZeroDivisionError, ValueError):
            continue

        if not (pitch_min <= rounded_pitch <= pitch_max):
            continue

        # Step 4: Use rounded pitch to recalculate stretched length
        stretched_length = (unwound_length * rounded_pitch) / math.sqrt((math.pi * B8) ** 2 + rounded_pitch ** 2)

        # Step 5: Passes and coil details
        passes_possible = (stretched_length + math.pi * B5) / (B3 - 2 + math.pi * B5)
        actual_passes = math.floor(passes_possible)
        number_of_coils = phase  # Default to 1 unless split needed
        total_ft_per_unit = (unwound_length / 12) * number_of_coils 

        # Append result in correct order
        results.append({
            "Gauge": gauge,  # Optional backward compatibility
            "Actual Passes": actual_passes,  # Optional backward compatibility
            "Actual Pitch": rounded_pitch,  # Optional backward compatibility
            "Connection Type": connection_type.capitalize(),
            "Resistance (ohm)": round(resistance, 4),
            "Line Current": line_current,
            "Nichrome Wire Size (AWG)": gauge,
            "Number of Coils": number_of_coils,
            "Passes": actual_passes,
            "Pitch": rounded_pitch,
            "Heat Element Length (in) per coil": round(unwound_length, 2),
            "Unstretch Wounded Length (in)": round(unstretch_wound, 2),
            "Stretched Wound Coil Length (in)": round(stretched_length, 2),
            "Heat Element Length (ft) per unit": round(total_ft_per_unit, 2)
        })

    return results
