# coil_popup.py

import tkinter as tk
from tkinter import ttk, messagebox

def show_coil_selection_popup(options, unit_index):
    popup = tk.Toplevel()
    popup.title(f"Select Coil Option for Unit {unit_index + 1}")
    popup.grab_set()

    tk.Label(popup, text="Choose one of the following coil options:").pack(pady=5)
    selected_index = tk.IntVar(value=0)

    frame = ttk.Frame(popup)
    frame.pack(padx=10, pady=5, fill="both", expand=True)

    for i, option in enumerate(options):
        label = (
            f"Gauge: {option['Gauge']}, Passes: {option['Actual Passes']}, "
            f"Pitch: {option['Actual Pitch']:.3f}, Type: {option['Connection Type']}"
        )
        ttk.Radiobutton(frame, text=label, variable=selected_index, value=i).pack(anchor="w")

    def select_and_close():
        popup.destroy()

    ttk.Button(popup, text="Select", command=select_and_close).pack(pady=10)
    popup.wait_window()

    return options[selected_index.get()] if options else None
