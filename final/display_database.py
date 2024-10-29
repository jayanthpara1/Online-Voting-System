import tkinter as tk
from tkinter import ttk
import pandas as pd

def display_data():
    try:
        data = pd.read_excel('database.xlsx')  # Change the file name here
        display_frame.grid(row=2, column=0, columnspan=2)
        
        # Create a Treeview widget to display the data
        columns = list(data.columns)
        tree = ttk.Treeview(display_frame, columns=columns, show='headings')
        
        # Add column headers
        for col in columns:
            tree.heading(col, text=col)
        
        # Add data rows
        for index, row in data.iterrows():
            tree.insert("", "end", values=list(row))
        
        tree.pack(fill="both", expand=True)
    except FileNotFoundError:
        display_frame.grid_forget()
        messagebox.showerror("Error", "File not found.")

app = tk.Tk()
app.title("Excel Data Display")

# Display Button
display_button = ttk.Button(app, text="Display Data", command=display_data)
display_button.grid(row=0, column=0)

# Frame to display data
display_frame = tk.Frame(app)

app.mainloop()
