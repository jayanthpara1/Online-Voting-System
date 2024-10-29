import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import random

# Global variable to store OTP
otp = None

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp(phone_number, otp):
    # In a real application, you would use an SMS service API
    # This is a simplified example
    print(f"OTP Sent to {phone_number}: {otp}")

def login_and_proceed():
    global otp
    aadhar = aadhar_entry.get().strip()
    voter_id = voter_id_entry.get().strip()
    
    try:
        data = pd.read_excel('voter_data.xlsx')
        data['Aadhar Number'] = data['Aadhar Number'].astype(str).str.strip().str.lower()
        data['Voter ID'] = data['Voter ID'].astype(str).str.strip().str.lower()
        
        matching_data = data[(data['Aadhar Number'] == aadhar.lower()) & (data['Voter ID'] == voter_id.lower())]
        
        if not matching_data.empty:
            # Login Successful, generate and send OTP
            otp = generate_otp()
            send_otp("1234567890", otp)
            show_otp_entry()
        else:
            result_label.config(text="Login Failed. Please try again.")
    except FileNotFoundError:
        result_label.config(text="No Excel file found")

def show_otp_entry():
    aadhar_label.grid_forget()
    aadhar_entry.grid_forget()
    voter_id_label.grid_forget()
    voter_id_entry.grid_forget()
    login_button.grid_forget()
    otp_label.grid(row=4, column=0, columnspan=2)
    entry_otp.grid(row=5, column=0, columnspan=2)
    submit_otp_button.grid(row=6, column=0, columnspan=2)

def submit_otp():
    user_otp = entry_otp.get()
    if user_otp == otp:
        messagebox.showinfo("OTP Verified", "OTP is valid. You can now select your state.")
        show_states()
    else:
        messagebox.showerror("OTP Error", "Invalid OTP. Please try again.")

# Rest of your code for showing states and parties, handling votes, and the main window goes here

app = tk.Tk()
app.title("Login Page")

aadhar_label = ttk.Label(app, text="Aadhar Number:")
voter_id_label = ttk.Label(app, text="Voter ID:")

aadhar_label.grid(row=0, column=0)
voter_id_label.grid(row=1, column=0)

aadhar_entry = ttk.Entry(app)
voter_id_entry = ttk.Entry(app)

aadhar_entry.grid(row=0, column=1)
voter_id_entry.grid(row=1, column=1)

login_button = ttk.Button(app, text="Login", command=login_and_proceed)
login_button.grid(row=2, column=0, columnspan=2)

result_label = ttk.Label(app, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Hide OTP related widgets initially
otp_label = tk.Label(app, text="Enter OTP:")
otp_label.pack_forget()
entry_otp = tk.Entry(app)
entry_otp.pack_forget()
submit_otp_button = tk.Button(app, text="Submit OTP", command=submit_otp)
submit_otp_button.pack_forget()

app.mainloop()
