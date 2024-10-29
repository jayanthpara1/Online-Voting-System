import tkinter as tk
import random
from tkinter import messagebox
import pandas as pd

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
    aadhar = aadhar_entry.get()  # Define 'aadhar' variable here
    voter_id = voter_id_entry.get()  # Define 'voter_id' variable here
    user_otp = entry_otp.get()
    
    if user_otp == otp:
        # Fetch user details from Excel sheet
        user_data = get_user_data(aadhar, voter_id)
        if user_data:
            name, phone_number = user_data
            messagebox.showinfo("OTP Verified", f"Welcome, {name}!\nOTP is valid. You can now select your state.")
            show_states()
        else:
            messagebox.showerror("User Not Found", "User with provided Aadhar and Voter ID not found.")
    else:
        messagebox.showerror("OTP Error", "Invalid OTP. Please try again.")

# Function to fetch user details from the Excel sheet
def get_user_data(aadhar, voter_id):
    try:
        data = pd.read_excel('voter_data.xlsx')
        user_data = data[(data['Aadhar Number'] == aadhar) & (data['Voter ID'] == voter_id)]
        if not user_data.empty:
            return user_data.iloc[0]['Name'], user_data.iloc[0]['Phone Number']
    except FileNotFoundError:
        pass
    return None

# ... Rest of the code ...

# Create the main window
root = tk.Tk()
root.title("State Election System")

# Generate and send OTP (in a real application, you would send it via SMS)
otp = generate_otp()
user_data = get_user_data(aadhar_entry.get(), voter_id_entry.get())
if user_data:
    name, phone_number = user_data
    send_otp(phone_number, otp)

# ... Rest of the code ...

# Start the Tkinter main loop
root.mainloop()
