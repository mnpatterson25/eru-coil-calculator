import tkinter as tk
from tkinter import ttk, messagebox

def show_coil_selection_popup(coil_options, on_selection_callback):
    """Popup that shows multiple coil options for a single line item."""
    popup = tk.Toplevel()
    popup.title("Select Coil Configuration")
    popup.geometry("600x400")

    label = ttk.Label(popup, text="Select a coil configuration:")
    label.pack(pady=10)

    tree = ttk.Treeview(popup, columns=list(coil_options[0].keys()), show='headings')
    for col in coil_options[0].keys():
        tree.heading(col, text=col)
        tree.column(col, width=100)
    for option in coil_options:
        tree.insert("", "end", values=list(option.values()))

    tree.pack(fill="both", expand=True)

    def on_double_click(event):
        selected = tree.focus()
        if selected:
            values = tree.item(selected, "values")
            option = dict(zip(coil_options[0].keys(), values))
            on_selection_callback(option)
            popup.destroy()

    tree.bind("<Double-1>", on_double_click)

    close_btn = ttk.Button(popup, text="Cancel", command=popup.destroy)
    close_btn.pack(pady=5)


# NEW: Multi-line popup
def show_all_coil_selections_popup(parent, unit_data, coil_options_by_line, on_all_selections_done):
    selected_options = {}  # line_index -> selected coil config

    popup = tk.Toplevel(parent)
    popup.title("Coil Selections for All Units")
    popup.geometry("800x500")

    label = ttk.Label(popup, text="Click 'Select' or 'Change' to assign coil options per unit:")
    label.pack(pady=10)

    container = ttk.Frame(popup)
    canvas = tk.Canvas(container, height=400)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scroll_frame = ttk.Frame(canvas)

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    container.pack(fill="both", expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    row_widgets = []

    def refresh_table():
        for widgets in row_widgets:
            for w in widgets:
                w.destroy()
        row_widgets.clear()

        headers = ["Line", "Tag #", "Size", "Coil Option Selected", "Action"]
        for col, text in enumerate(headers):
            header = ttk.Label(scroll_frame, text=text, font=("Segoe UI", 10, "bold"))
            header.grid(row=0, column=col, padx=10, pady=6)

        for idx, unit in enumerate(unit_data):
            widgets = []

            tag = unit.get("Tag #", "")
            size = unit.get("Size", "")
            selection = selected_options.get(idx, None)

            if selection:
                # Build label if not already present
                coil_label = selection.get("Label")
                if not coil_label:
                    passes = selection.get("Actual Passes", "?")
                    gauge = selection.get("Gauge", "?")
                    coil_label = f"{passes}P/{gauge}G"
                status_icon = "✅"
                status_text = coil_label
                action_label = "Change"
            else:
                status_icon = "❌"
                status_text = "None"
                action_label = "Select"


            w1 = ttk.Label(scroll_frame, text=str(idx + 1), font=("Segoe UI", 10))
            w2 = ttk.Label(scroll_frame, text=tag, font=("Segoe UI", 10))
            w3 = ttk.Label(scroll_frame, text=size, font=("Segoe UI", 10))
            w4 = ttk.Label(scroll_frame, text=f"{status_icon} {status_text}", font=("Segoe UI", 10))

            def make_callback(index=idx):
                def callback():
                    options = coil_options_by_line.get(index, [])
                    if not options:
                        messagebox.showinfo("No Options", f"No coil options available for unit {index + 1}")
                        return

                    def on_selection(option):
                        if not option:
                            messagebox.showwarning("No Selection", f"No coil selected for unit {index + 1}")
                            return

                        # Add Label dynamically
                        passes = option.get("Actual Passes", "?")
                        gauge = option.get("Gauge", "?")
                        option["Label"] = f"{passes}P/{gauge}G"
                        selected_options[index] = option
                        refresh_table()

                    show_coil_selection_popup(options, on_selection)

                return callback

            action_btn = ttk.Button(scroll_frame, text=f"🔍 {action_label}", command=make_callback())

            w1.grid(row=idx + 1, column=0, padx=10, pady=4)
            w2.grid(row=idx + 1, column=1, padx=10, pady=4)
            w3.grid(row=idx + 1, column=2, padx=10, pady=4)
            w4.grid(row=idx + 1, column=3, padx=10, pady=4)
            action_btn.grid(row=idx + 1, column=4, padx=10, pady=4)

            widgets.extend([w1, w2, w3, w4, action_btn])
            row_widgets.append(widgets)

    refresh_table()

    def done():
        popup.destroy()
        on_all_selections_done(selected_options)

    done_btn = ttk.Button(popup, text="Done", command=done)
    done_btn.pack(pady=10)