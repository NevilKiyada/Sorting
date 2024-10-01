# File operations (CSV) 
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def read_csv(file_path):
    # ... existing code ...
    try:
        data = pd.read_csv(file_path)
        if data.shape[1] != 1:
            raise ValueError("CSV file should contain exactly one column")
        return data.iloc[:, 0].tolist()
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

def select_csv_file():
    # ... existing code ...
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path


