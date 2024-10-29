import tkinter as tk
from tkinter import ttk
import pandas as pd

def display_data():
    try:
        data = pd.read_excel('voter_data.xlsx')
        data_display.delete(1.0, tk.END)  # Clear previous data

        if data.empty:
            data_display.insert(tk.END, "No data available in the Excel file.")
        else:
            data_display.insert(tk.END, data.to_string(index=False))
    except FileNotFoundError:
        data_display.delete(1.0, tk.END)  # Clear previous data
        data_display.insert(tk.END, "No Excel file found.")

app = tk.Tk()
app.title("Display Voter Information")

# Display Button
display_button = ttk.Button(app, text="Display Data", command=display_data)
display_button.pack()

# Text Widget to Display Data
data_display = tk.Text(app, height=10, width=100)
data_display.pack()

app.mainloop()
