import tkinter as tk
from tkinter import ttk
import pandas as pd

def save_data():
    name = name_entry.get()
    aadhar = aadhar_entry.get()
    voter_id = voter_id_entry.get()
    phone = phone_entry.get()
    age = age_var.get()
    gender = gender_var.get()

    # Create a DataFrame with the new columns ("Voting Status" and "Extra") initially set to empty strings
    data = {
        'Name': [name],
        'Aadhar Number': [aadhar],
        'Voter ID': [voter_id],
        'Phone Number': [phone],
        'Age': [age],
        'Gender': [gender],
        'Voting Status': [''],  # Add an empty column for Voting Status
        'Extra': ['']  # Add an empty column for Extra
    }

    df = pd.DataFrame(data)

    try:
        existing_data = pd.read_excel('database.xlsx')  # Change the file name here
        updated_data = pd.concat([existing_data, df], ignore_index=True)
        updated_data.to_excel('database.xlsx', index=False)  # Change the file name here
    except FileNotFoundError:
        df.to_excel('database.xlsx', index=False)  # Change the file name here

    clear_fields()

def clear_fields():
    name_entry.delete(0, 'end')
    aadhar_entry.delete(0, 'end')
    voter_id_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    age_var.set(18)  # Default age to 18
    gender_var.set('Male')  # Default gender to Male

app = tk.Tk()
app.title("Voter Information Form")

# Labels
name_label = ttk.Label(app, text="Name:")
aadhar_label = ttk.Label(app, text="Aadhar Number:")
voter_id_label = ttk.Label(app, text="Voter ID:")
phone_label = ttk.Label(app, text="Phone Number:")
age_label = ttk.Label(app, text="Age:")
gender_label = ttk.Label(app, text="Gender:")

name_label.grid(row=0, column=0)
aadhar_label.grid(row=1, column=0)
voter_id_label.grid(row=2, column=0)
phone_label.grid(row=3, column=0)
age_label.grid(row=4, column=0)
gender_label.grid(row=5, column=0)

# Entry Widgets
name_entry = ttk.Entry(app)
aadhar_entry = ttk.Entry(app)
voter_id_entry = ttk.Entry(app)
phone_entry = ttk.Entry(app)

name_entry.grid(row=0, column=1)
aadhar_entry.grid(row=1, column=1)
voter_id_entry.grid(row=2, column=1)
phone_entry.grid(row=3, column=1)

# Age Dropdown
age_var = tk.IntVar()
age_dropdown = ttk.Combobox(app, textvariable=age_var, values=list(range(18, 61)))
age_dropdown.grid(row=4, column=1)
age_dropdown.set(18)

# Gender Radio Buttons
gender_var = tk.StringVar()
gender_male = ttk.Radiobutton(app, text="Male", variable=gender_var, value="Male")
gender_female = ttk.Radiobutton(app, text="Female", variable=gender_var, value="Female")
gender_other = ttk.Radiobutton(app, text="Other", variable=gender_var, value="Other")

gender_male.grid(row=5, column=1)
gender_female.grid(row=5, column=2)
gender_other.grid(row=5, column=3)

# Save Button
save_button = ttk.Button(app, text="Save", command=save_data)
save_button.grid(row=6, column=0, columnspan=2)

# Clear Button
clear_button = ttk.Button(app, text="Clear", command=clear_fields)
clear_button.grid(row=6, column=2, columnspan=2)

app.mainloop()
