# tab_ceramics.py

import tkinter as tk
from tkinter import ttk
from logic.components import CERAMIC_INFO
from gui.tab_base import create_table

def add_ceramics_tab(notebook, data):
    ceramic_frame = ttk.Frame(notebook)
    notebook.add(ceramic_frame, text="Ceramics")
    create_table(ceramic_frame, CERAMIC_INFO, data)


#from logic.calculations import passes_actual
#from logic.coil_calculator import coils_qty, passes_actual
#ceramics = 0
#def add_ceramics_tab(notebook, data, coil_data):
#for idx, coil in enumerate(coil_data):
#ceramics = passes_actual * 2 * coils_qty