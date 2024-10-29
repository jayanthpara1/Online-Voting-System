def login():
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
        "Andhra Pradesh": ["YSRCP", "TDP", "BJP","INC"],
        "Arunachal Pradesh": ["BJP", "INC"],
        "Telangana":["BRS","BJP","INC"]
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

# Create the main window
root = tk.Tk()
root.title("State Election System")

# Generate and send OTP (in a real application, you would send it via SMS)
otp = generate_otp()
send_otp("1234567890", otp)

# Create and pack OTP entry field and submit button
otp_label = tk.Label(root, text="Enter OTP:")
otp_label.pack()
entry_otp = tk.Entry(root)
entry_otp.pack()
submit_otp_button = tk.Button(root, text="Submit OTP", command=submit_otp)
submit_otp_button.pack()

# Create and pack state-related widgets initially hidden
state_label = tk.Label(root, text="Select State:")
state_var = tk.StringVar()
state_dropdown = tk.OptionMenu(root, state_var, "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Benga")
state_dropdown.pack_forget()
show_parties_button = tk.Button(root, text="Show Parties", command=show_political_parties)
show_parties_button.pack_forget()

# Create and pack political party-related widgets initially hidden
party_label = tk.Label(root, text="Select Political Party:")
party_var = tk.StringVar()
party_dropdown = tk.OptionMenu(root, party_var, "Loading...")

# Create and pack radio buttons for political parties (initially hidden)
party_radio_label = tk.Label(root, text="Select Political Party:")
selected_party_var = tk.StringVar()
party_radio_label.pack_forget()

# Create and pack vote button (initially hidden)
vote_button = tk.Button(root, text="Vote", command=vote)
vote_button.pack_forget()

# Start the Tkinter main loop
root.mainloop()
