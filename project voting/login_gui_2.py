from tkinter import messagebox, Tk, Label, Entry, Button

# Pre-defined user details
user_details = {
    "User1": {"aadhar_number": "123", "voter_id": "123"},
    "User2": {"aadhar_number": "987654321098", "voter_id": "B5678"},
    "User3": {"aadhar_number": "456789012345", "voter_id": "C9012"}
}

def login1():
    aadhar = aadhar_entry.get()
    voter_id = voter_id_entry.get()
    
    for user, details in user_details.items():
        if aadhar == details['aadhar_number'] and voter_id == details['voter_id']:
            messagebox.showinfo("Success", f"Login successful - Welcome {user}!")
            login()
            # from voting import 
            return
    
    messagebox.showerror("Error", "Invalid Aadhar number or Voter ID")

# Create window
window = Tk()
window.title("Login")
window.geometry("300x200")

# Labels
aadhar_label = Label(window, text="Aadhar Number:")
aadhar_label.pack()
voter_id_label = Label(window, text="Voter ID:")
voter_id_label.pack()

# Entry fields
aadhar_entry = Entry(window)
aadhar_entry.pack()
voter_id_entry = Entry(window)
voter_id_entry.pack()

# Login button
login_button = Button(window, text="Login", command=login1)
login_button.pack()



# Start GUI event loop
#
import tkinter as tk
import random
from tkinter import messagebox

# Function to generate a random 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP via SMS (simplified)
def send_otp(phone_number, otp):
    # In a real application, you would use an SMS service API
    # This is a simplified example
    print(f"OTP Sent to {phone_number}: {otp}")

# Function to handle OTP submission
def submit_otp():
    user_otp = entry_otp.get()
    if user_otp == otp:
        messagebox.showinfo("OTP Verified", "OTP is valid. You can now select your state.")
        show_states()
    else:
        messagebox.showerror("OTP Error", "Invalid OTP. Please try again.")

# Function to fetch and display Indian states
def show_states():
    state_label.pack()
    state_var.set("Select a State")
    state_dropdown.pack()
    show_parties_button.pack()

# Function to fetch and display political parties based on the selected state
def show_political_parties():
    selected_state = state_var.get()

    # You can use an API to fetch political parties based on the selected state
    # This is a simplified example using a hardcoded list
    parties = {
        "Andhra Pradesh": ["YSRCP", "TDP", "BJP", "INC"],
        "Arunachal Pradesh": ["BJP", "INC"],
        "Telangana": ["BRS", "BJP", "INC"]
        # Add parties for other states
    }

    selected_parties = parties.get(selected_state, [])
    if selected_parties:
        party_label.pack()
        party_var.set(selected_parties[0])
        party_dropdown['menu'].delete(0, 'end')  # Clear existing menu items
        for party in selected_parties:
            party_dropdown['menu'].add_command(label=party, command=lambda p=party: party_var.set(p))

        # Create and pack radio buttons for political parties
        create_party_radio_buttons(selected_parties)
        show_vote_button()
    else:
        party_label.pack_forget()
        party_dropdown.pack_forget()
        hide_vote_button()
        messagebox.showwarning("No Parties", "No political parties available for the selected state.")

# Function to create and pack radio buttons for political parties
def create_party_radio_buttons(parties):
    party_radio_label.pack()
    selected_party_var.set(parties[0])
    for party in parties:
        party_radio = tk.Radiobutton(root, text=party, variable=selected_party_var, value=party)
        party_radio.pack()

# Function to show the vote button
def show_vote_button():
    vote_button.pack()

# Function to hide the vote button
def hide_vote_button():
    vote_button.pack_forget()

# Function to handle voting
def vote():
    selected_party = selected_party_var.get()
    messagebox.showinfo("Vote Submitted", f"You have voted for {selected_party}. Thank you for participating in the election!")

# Main login function
def login():
    # Create the main window
    root = tk.Tk()
    root.title("State Election System")

    # Generate and send OTP (in a real application, you would send it via SMS)
    global otp
    otp = generate_otp()
    send_otp("1234567890", otp)

    # Create and pack OTP entry field and submit button
    otp_label = tk.Label(root, text="Enter OTP:")
    otp_label.pack()
    global entry_otp
    entry_otp = tk.Entry(root)
    entry_otp.pack()
    submit_otp_button = tk.Button(root, text="Submit OTP", command=submit_otp)
    submit_otp_button.pack()

    # Create and pack state-related widgets initially hidden
    global state_label, state_var, state_dropdown, show_parties_button
    state_label = tk.Label(root, text="Select State:")
    state_var = tk.StringVar()
    state_dropdown = tk.OptionMenu(root, state_var, "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Benga")
    state_dropdown.pack_forget()
    show_parties_button = tk.Button(root, text="Show Parties", command=show_political_parties)
    show_parties_button.pack_forget()

    # Create and pack political party-related widgets initially hidden
    global party_label, party_var, party_dropdown, party_radio_label, selected_party_var
    party_label = tk.Label(root, text="Select Political Party:")
    party_var = tk.StringVar()
    party_dropdown = tk.OptionMenu(root, party_var, "Loading...")

    # Create and pack radio buttons for political parties (initially hidden)
    party_radio_label = tk.Label(root, text="Select Political Party:")
    selected_party_var = tk.StringVar()
    party_radio_label.pack_forget()

    # Create and pack vote button (initially hidden)
    global vote_button
    vote_button = tk.Button(root, text="Vote", command=vote)
    vote_button.pack_forget()

    # Start the Tkinter main loop
    root.mainloop()

# Call the login function to run the application
#if __name__ == "__main__":
    #login()
window.mainloop()
