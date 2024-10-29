import tkinter as tk
from tkinter import ttk, messagebox
import random
import pandas as pd

# Global variables
user_database = {}  # Replace this with your database
#######################################################

333333333333333333333333333333333333333333333333333333333333

def login_page():
    def login():
        aadhar = aadhar_entry.get().strip()
        voter_id = voter_id_entry.get().strip()

        # Check if Aadhar and Voter ID match
        if aadhar in user_database and user_database[aadhar] == voter_id:
            otp = generate_otp()
            messagebox.showinfo("Login Successful", "Successful Login!")
            show_otp_entry(otp)
        else:
            messagebox.showerror("Error", "Invalid Aadhar or Voter ID")

    def generate_otp():
        return str(random.randint(100000, 999999))

    def show_otp_entry(otp):
        login_frame.pack_forget()
        otp_entry_frame.pack()
        otp_label.config(text=f"Enter OTP sent to your registered mobile number:")
        verify_button.config(command=lambda: verify_otp(otp))

    def verify_otp(otp):
        entered_otp = otp_entry.get()
        if entered_otp == otp:
            show_voting_page()
        else:
            messagebox.showerror("Error", "Invalid OTP")

    # Create the login window
    login_window = tk.Tk()
    login_window.title("Login Page")

    # Labels
    aadhar_label = ttk.Label(login_window, text="Aadhar Number:")
    voter_id_label = ttk.Label(login_window, text="Voter ID:")

    aadhar_label.grid(row=0, column=0)
    voter_id_label.grid(row=1, column=0)

    # Entry Widgets
    aadhar_entry = ttk.Entry(login_window)
    voter_id_entry = ttk.Entry(login_window)

    aadhar_entry.grid(row=0, column=1)
    voter_id_entry.grid(row=1, column=1)

    # Login Button
    login_button = ttk.Button(login_window, text="Login", command=login)
    login_button.grid(row=2, column=0, columnspan=2)

    login_window.mainloop()

def voting_page():
    def vote():
        selected_party = party_selection.get()
        messagebox.showinfo("Success", f"You voted for {selected_party}")
        voting_window.destroy()

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
    voting_window = tk.Tk()
    voting_window.title("Online Election")

    # OTP Entry Page
    otp_entry_frame = tk.Frame(voting_window)

    otp_label = tk.Label(otp_entry_frame, text="", font=("Helvetica", 12))
    otp_label.pack()

    otp_entry = tk.Entry(otp_entry_frame)
    otp_entry.pack()

    verify_button = tk.Button(otp_entry_frame, text="Verify OTP", command=lambda: verify_otp(""))
    verify_button.pack()

    # Voting Page
    voting_frame = tk.Frame(voting_window)

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

    voting_window.mainloop()

if __name__ == "__main__":
    # Load user database from the Excel sheet (Replace 'voter_data.xlsx' with your file)
    try:
        data = pd.read_excel('voter_data.xlsx')
        user_database = {str(row['Aadhar Number']): row['Voter ID'] for index, row in data.iterrows()}
    except FileNotFoundError:
        messagebox.showerror("Error", "No Excel file found")

    login_page()
    voting_page()
