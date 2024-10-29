import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import random

# Dummy database for Aadhar and Voter ID mapping (Replace this with a real database)
user_database = {
    '123456789012': 'voter1',
    '987654321098': 'voter2'
}

# Dummy party list for a state (Replace this with real data)
party_list = {
    'Karnataka': ['Party A', 'Party B', 'Party C'],
    'Tamil Nadu': ['Party X', 'Party Y', 'Party Z']
}

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
            otp = generate_otp()
            print(f"Successful Login! Your OTP is: {otp}")  # Print OTP to console
            messagebox.showinfo("Login Successful", "Successful Login!")
            show_otp_entry(otp)
        else:
            result_label.config(text="Login Failed. Please try again.")
    except FileNotFoundError:
        result_label.config(text="No Excel file found")

def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

def verify_otp(otp):
    entered_otp = otp_entry.get()
    if entered_otp == otp:
        show_voting_page()
    else:
        messagebox.showerror("Error", "Invalid OTP")

def vote():
    selected_party = party_selection.get()
    messagebox.showinfo("Success", f"You voted for {selected_party}")
    window.destroy()

def show_otp_entry(otp):
    login_frame.pack_forget()
    otp_entry_frame.pack()
    otp_label.config(text=f"Enter OTP sent to your registered mobile number:")
    verify_button.config(command=lambda: verify_otp(otp))

def show_voting_page():
    otp_entry_frame.pack_forget()
    voting_frame.pack()
    states = list(party_list.keys())
    state_selection.set(states[0])  # Set the default state
    state_dropdown['menu'].delete(0, 'end')  # Clear existing values
    for state in states:
        state_dropdown['menu'].add_command(label=state, command=lambda s=state: state_selection.set(s))
    
    # Set the default party
    parties = party_list.get(states[0], [])
    party_selection.set(parties[0])
    party_dropdown['menu'].delete(0, 'end')  # Clear existing values
    for party in parties:
        party_dropdown['menu'].add_command(label=party, command=lambda p=party: party_selection.set(p))

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

# OTP Entry Page
otp_entry_frame = tk.Frame(app)

otp_label = tk.Label(otp_entry_frame, text="", font=("Helvetica", 12))
otp_label.pack()

otp_entry = tk.Entry(otp_entry_frame)
otp_entry.pack()

verify_button = tk.Button(otp_entry_frame, text="Verify OTP", command=lambda: verify_otp(""))
verify_button.pack()

# Voting Page
voting_frame = tk.Frame(app)

state_label = tk.Label(voting_frame, text="Select State:")
state_label.pack()

state_selection = tk.StringVar()
state_dropdown = tk.OptionMenu(voting_frame, state_selection, "Select State")
state_dropdown.pack()

party_label = tk.Label(voting_frame, text="Select Party:")
party_label.pack()

party_selection = tk.StringVar()
party_dropdown = tk.OptionMenu(voting_frame, party_selection, "Select Party")
party_dropdown.pack()

vote_button = tk.Button(voting_frame, text="Vote", command=vote)
vote_button.pack()

app.mainloop()
