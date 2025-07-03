# input_form.py

import tkinter as tk
from tkinter import ttk, messagebox
from logic.calculations import process_unit_data
from logic.coil_calculator import calculate_coil_options
from gui.coil_popup import show_all_coil_selections_popup
from gui.results_display import show_results
import logic.shared_state
from logic.components import *

columns = [
    "Line", "Tag #", "Size", "Material", "Coil Handing",
    "Disconnect", "Transformer Voltage", "Voltage/Phase", "kW"
]
dropdown_options = {
    "Size": ["10x15", "10x21", "16x30"],
    "Material": ["Galvanized"],
    "Coil Handing": ["Left", "Right"],
   "Transformer Voltage": ["a", "b", "c"],
   "Voltage/Phase": ["480/3", "120/1"],
   "Disconnect": ["STD", "KE"]
}

unit_rows = []
input_frame = None


def build_input_form(root):
    global input_frame, table_frame

    input_frame = ttk.Frame(root)
    input_frame.pack(fill="both", expand=True)
    logic.shared_state.input_frame = input_frame

    canvas = tk.Canvas(input_frame)
    scrollbar = ttk.Scrollbar(input_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    table_frame = scrollable_frame

    for col, name in enumerate(columns):
        ttk.Label(table_frame, text=name, background="#ddd", padding=5).grid(row=0, column=col, sticky="nsew")
    ttk.Label(table_frame, text="Delete", background="#ddd", padding=5).grid(row=0, column=len(columns), sticky="nsew")

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10)

    ttk.Button(button_frame, text="Add Unit", command=add_unit_row).pack(side="left", padx=10)
    ttk.Button(button_frame, text="Submit All", command=submit_all).pack(side="left", padx=10)

    add_unit_row()


def add_unit_row():
    row_data = {}
    row_index = len(unit_rows) + 1

    for col_index, field in enumerate(columns):
        var = tk.StringVar()
        if field in dropdown_options:
            combo = ttk.Combobox(table_frame, values=dropdown_options[field], textvariable=var, width=12, state="readonly")
            combo.set(dropdown_options[field][0])
            combo.grid(row=row_index, column=col_index, padx=2, pady=2)
        else:
            entry = ttk.Entry(table_frame, textvariable=var, width=14)
            entry.grid(row=row_index, column=col_index, padx=2, pady=2)
        row_data[field] = var

    delete_btn = ttk.Button(table_frame, text="X", width=3, command=lambda: delete_unit_row(row_data))
    delete_btn.grid(row=row_index, column=len(columns), padx=2)
    row_data["_widgets"] = (row_index, delete_btn)

    unit_rows.append(row_data)


def delete_unit_row(row_data):
    index = unit_rows.index(row_data)
    for widget in table_frame.grid_slaves(row=index+1):
        widget.destroy()
    unit_rows.remove(row_data)
    rebuild_table()


def rebuild_table():
    for i, row in enumerate(unit_rows, start=1):
        for col_index, field in enumerate(columns):
            widget = table_frame.grid_slaves(row=row["_widgets"][0], column=col_index)
            if widget:
                widget[0].grid(row=i, column=col_index)
        row["_widgets"] = (i, row["_widgets"][1])
        row["_widgets"][1].grid(row=i, column=len(columns))


def submit_all():
    unit_data = []
    coil_options_by_line = {}

    for idx, row in enumerate(unit_rows):
        unit = {field: row[field].get() for field in columns}

        try:
            unit["Voltage/Phase"] = int(unit["Voltage/Phase"].split("/")[0])
            unit["kW"] = float(unit["kW"])
            unit_size = unit["Size"]
            passes_to_try = [6, 8] if unit_size == "16x30" else [6, 8, 12, 16]

            options = []
            for passes in passes_to_try:
                options += calculate_coil_options(unit["Voltage/Phase"], unit["kW"], unit_size, passes)

            coil_options_by_line[idx] = options
            unit["Coil Options"] = options

        except Exception as e:
            messagebox.showerror("Error", f"Error processing unit: {e}")
            return

        unit_data.append(unit)

    def on_all_selected_coils(selected_options):
        for idx, selected in selected_options.items():
            unit_data[idx]["Selected Coil"] = selected

        logic.shared_state.processed_data = process_unit_data(unit_data)
        all_selected = [unit.get("Selected Coil") for unit in unit_data]
        show_results(logic.shared_state.processed_data, logic.shared_state.input_frame, coil_data=all_selected)

    show_all_coil_selections_popup(input_frame, unit_data, coil_options_by_line, on_all_selected_coils)
