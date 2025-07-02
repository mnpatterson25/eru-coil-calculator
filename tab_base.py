import tkinter.font as tkfont
import tkinter as tk
from tkinter import ttk


def create_table(frame, columns, data):
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    tree.pack(fill="both", expand=True)

    font = tkfont.nametofont("TkDefaultFont")
    col_widths = {col: font.measure(col) + 20 for col in columns}  # Start with title width

    for row in data:
        for col in columns:
            val = str(row.get(col, ""))
            col_widths[col] = max(col_widths[col], font.measure(val) + 20)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=col_widths[col], anchor="center")

    for row in data:
        row_values = [row.get(col, "") for col in columns]
        tree.insert("", "end", values=row_values)
