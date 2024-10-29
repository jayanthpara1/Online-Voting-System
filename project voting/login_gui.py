from tkinter import messagebox, Tk, Label, Entry, Button

# Pre-defined user details
user_details = {
    "User1": {"aadhar_number": "123", "voter_id": "123"},
    "User2": {"aadhar_number": "987654321098", "voter_id": "B5678"},
    "User3": {"aadhar_number": "456789012345", "voter_id": "C9012"}
}

def login():
    aadhar = aadhar_entry.get()
    voter_id = voter_id_entry.get()
    
    for user, details in user_details.items():
        if aadhar == details['aadhar_number'] and voter_id == details['voter_id']:
            messagebox.showinfo("Success", f"Login successful - Welcome {user}!")
            import voting1
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
login_button = Button(window, text="Login", command=login)
login_button.pack()

# Start GUI event loop
window.mainloop()
