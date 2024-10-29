import tkinter as tk
from tkinter import messagebox  # Add this import
import random

# Dummy database for Aadhar and Voter ID mapping (Replace this with a real database)
user_database = {
    '123456789012': 'voter1',
    '987654321098': 'voter2'
}

# Generate a 6-digit OTP
def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

# Login function
def login():
    aadhar = aadhar_entry.get()
    voter_id = voter_id_entry.get()
    
    # Check if Aadhar and Voter ID match
    if aadhar in user_database and user_database[aadhar] == voter_id:
        otp = generate_otp()
        print(f"Successful Login! Your OTP is: {otp}")  # Print OTP to console
        messagebox.showinfo("Login Successful", "Successful Login!")
        show_otp_entry(otp)
    else:
        messagebox.showerror("Error", "Invalid Aadhar or Voter ID")

# OTP verification function
def verify_otp(otp):
    entered_otp = otp_entry.get()
    if entered_otp == otp:
        show_voting_page()
    else:
        messagebox.showerror("Error", "Invalid OTP")

# Voting function
def vote():
    selected_party = party_selection.get()
    messagebox.showinfo("Success", f"You voted for {selected_party}")
    window.destroy()

# Function to display the OTP entry page
def show_otp_entry(otp):
    login_frame.pack_forget()
    otp_entry_frame.pack()
    otp_label.config(text=f"Enter OTP sent to your registered mobile number:")
    verify_button.config(command=lambda: verify_otp(otp))

# Function to display the voting page
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

# Create the main window
window = tk.Tk()
window.title("Online Election")

# Login Page
login_frame = tk.Frame(window)
login_frame.pack()

aadhar_label = tk.Label(login_frame, text="Aadhar Number:")
aadhar_label.pack()

aadhar_entry = tk.Entry(login_frame)
aadhar_entry.pack()

voter_id_label = tk.Label(login_frame, text="Voter ID:")
voter_id_label.pack()

voter_id_entry = tk.Entry(login_frame)
voter_id_entry.pack()

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack()

# OTP Entry Page
otp_entry_frame = tk.Frame(window)

otp_label = tk.Label(otp_entry_frame, text="", font=("Helvetica", 12))
otp_label.pack()

otp_entry = tk.Entry(otp_entry_frame)
otp_entry.pack()

verify_button = tk.Button(otp_entry_frame, text="Verify OTP", command=lambda: verify_otp(""))
verify_button.pack()

# Voting Page
voting_frame = tk.Frame(window)

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

# Dummy party list for a state (Replace this with real data)
party_list = {

    'Karnataka': ['Party A', 'Party B', 'Party C'],
    'Tamil Nadu': ['Party X', 'Party Y', 'Party Z']
}

vote_button = tk.Button(voting_frame, text="Vote", command=vote)
vote_button.pack()

window.mainloop()
