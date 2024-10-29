import tkinter as tk

registered_users = {}

def register():
    def submit_registration():
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_var.get()
        aadhar_number = aadhar_entry.get()
        voter_id = voter_entry.get()
        pan_card = pan_entry.get()
        mobile_number = mobile_entry.get()

        registered_users[name] = {
            'Age': age,
            'Gender': gender,
            'Aadhar Number': aadhar_number,
            'Voter ID': voter_id,
            'PAN Card': pan_card,
            'Mobile Number': mobile_number
        }

        print("Registration successful!")

    registration_window = tk.Tk()
    registration_window.title("Registration Form")

    name_label = tk.Label(registration_window, text="Full Name:")
    name_label.pack()
    name_entry = tk.Entry(registration_window)
    name_entry.pack()

    age_label = tk.Label(registration_window, text="Age:")
    age_label.pack()
    age_entry = tk.Entry(registration_window)
    age_entry.pack()

    gender_label = tk.Label(registration_window, text="Gender:")
    gender_label.pack()
    gender_var = tk.StringVar()
    gender_choices = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    for choice in gender_choices:
        gender_radio = tk.Radiobutton(registration_window, text=choice[0], variable=gender_var, value=choice[1])
        gender_radio.pack()

    aadhar_label = tk.Label(registration_window, text="Aadhar Number:")
    aadhar_label.pack()
    aadhar_entry = tk.Entry(registration_window)
    aadhar_entry.pack()

    voter_label = tk.Label(registration_window, text="Voter ID:")
    voter_label.pack()
    voter_entry = tk.Entry(registration_window)
    voter_entry.pack()

    pan_label = tk.Label(registration_window, text="PAN Card:")
    pan_label.pack()
    pan_entry = tk.Entry(registration_window)
    pan_entry.pack()

    mobile_label = tk.Label(registration_window, text="Mobile Number:")
    mobile_label.pack()
    mobile_entry = tk.Entry(registration_window)
    mobile_entry.pack()

    submit_button = tk.Button(registration_window, text="Submit", command=submit_registration)
    submit_button.pack()

    registration_window.mainloop()

def login():
    print("Login Page")
    print("----------")
    username = input("Username/Email: ")
    password = input("Password: ")

    if username in registered_users:
        print("Login successful!")
        # Continue with your logic here
    else:
        print("Invalid username or password. Please try again.")

register()
login()
