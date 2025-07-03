# tab_coil.py

from tkinter import ttk
from gui.coil_popup import show_coil_selection_popup

coil_frame_global = None  # So we can refresh from other functions if needed

def add_coil_tab(notebook, data, coil_data):
    global coil_frame_global
    coil_frame = ttk.Frame(notebook)
    coil_frame_global = coil_frame
    notebook.add(coil_frame, text="Selected Coils")

    coil_columns = [
        "Connection Type",
        "Resistance (ohm)",
        "Line Current",
        "Nichrome Wire Size (AWG)",
        "Coils",
        "Passes",
        "Pitch",
        "Heat Element Length (in) per coil",
        "Unstretch Wounded Length (in)",
        "Stretched Wound Coil Length (in)",
        "Heat Element Length (ft) per unit",
        "Ceramics",
        "Coil End Post",
        "Ceramic Plug/Cap Sets"
    ]

    headers = coil_columns + ["Change"]
    for col, name in enumerate(headers):
        ttk.Label(coil_frame, text=name, font=("Segoe UI", 10, "bold"), background="#ddd").grid(row=0, column=col, padx=5, pady=5)

    for idx, unit in enumerate(data):
        row = idx + 1
        selected = unit.get("Selected Coil")

        if selected:
            display_row = [selected.get(col, selected.get("Gauge", "")) for col in coil_columns]
        else:
            display_row = ["N/A"] * len(coil_columns)

        for col, val in enumerate(display_row):
            ttk.Label(coil_frame, text=val).grid(row=row, column=col, padx=5, pady=3)

        def make_callback(index=idx):
            def callback():
                options = data[index].get("Coil Options", [])
                if not options:
                    from tkinter import messagebox
                    messagebox.showinfo("No Options", f"No coil options available for unit {index + 1}")
                    return

                def on_selection(option):
                    if option:
                        passes = option.get("Actual Passes", "?")
                        gauge = option.get("Gauge", "?")
                        option["Label"] = f"{passes}P/{gauge}G"
                        data[index]["Selected Coil"] = option

                        from gui.results_display import show_results, input_frame_global
                        show_results(data, input_frame_global, coil_data=[u.get("Selected Coil") for u in data])

                show_coil_selection_popup(options, on_selection)

            return callback

        change_btn = ttk.Button(coil_frame, text="🔍 Edit", command=make_callback())
        change_btn.grid(row=row, column=len(coil_columns), padx=5, pady=3)