import tkinter as tk
from tkinter import ttk
import pandas as pd
import voting  # Import the voting module

def login():
    aadhar = aadhar_entry.get().strip()
    voter_id = voter_id_entry.get().strip()
    
    try:
        data = pd.read_excel('voter_data.xlsx')
        
        # Convert columns to string type
        data['Aadhar Number'] = data['Aadhar Number'].astype(str).str.strip().str.lower()
        data['Voter ID'] = data['Voter ID'].astype(str).str.strip().str.lower()
        
        matching_data = data[(data['Aadhar Number'] == aadhar.lower()) & (data['Voter ID'] == voter_id.lower())]
        
        if not matching_data.empty:
            result_label.config(text="Login Successful")
            # Open the voting window and close the login window
            app.withdraw()  # Hide the login window
            voting.open_voting_window()  # Open the voting window from the voting module
        else:
            result_label.config(text="Login Failed. Please try again.")
    except FileNotFoundError:
        result_label.config(text="No Excel file found")

app = tk.Tk()
app.title("Login Page")

# Labels
aadhar_label = ttk.Label(app, text="Aadhar Number:")
voter_id_label = ttk.Label(app, text="Voter ID:")

aadhar_label.grid(row=0, column=0)
voter_id_label.grid(row=1, column=0)

# Entry Widgets
aadhar_entry = ttk.Entry(app)
voter_id_entry = ttk.Entry(app)

aadhar_entry.grid(row=0, column=1)
voter_id_entry.grid(row=1, column=1)

# Login Button
login_button = ttk.Button(app, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2)

# Result Label
result_label = ttk.Label(app, text="")
result_label.grid(row=3, column=0, columnspan=2)

app.mainloop()
