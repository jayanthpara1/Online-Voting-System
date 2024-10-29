import tkinter as tk
from tkinter import ttk, messagebox
import random
import pandas as pd
from collections import defaultdict

# Create a dictionary to store the vote results
vote_results = defaultdict(int)

def login():
    aadhar = aadhar_entry.get().strip()
    voter_id = voter_id_entry.get().strip()
    
    try:
        data = pd.read_excel('database.xlsx')
        data['Aadhar Number'] = data['Aadhar Number'].astype(str).str.strip().str.lower()
        data['Voter ID'] = data['Voter ID'].astype(str).str.strip().str.lower()
        matching_data = data[(data['Aadhar Number'] == aadhar.lower()) & (data['Voter ID'] == voter_id.lower())]
        
        if not matching_data.empty:
            if matching_data['Voting Status'].values[0] == 'Voted':
                result_label.config(text="You have already voted.")
            else:
                result_label.config(text="Login Successful")
                data.loc[matching_data.index, 'Voting Status'] = 'Voted'
                data.to_excel('database.xlsx', index=False)
                app.destroy()
                open_voting_window()
        else:
            result_label.config(text="Login Failed. Please try again.")
    except FileNotFoundError:
        result_label.config(text="No Excel file found")
def save_vote_results_to_excel():
    # Load existing vote results from Excel
    existing_results = pd.read_excel('vote_results.xlsx')
    
    # Create a DataFrame from the vote_results dictionary
    new_results = pd.DataFrame(list(vote_results.items()), columns=['State_Party', 'Votes'])
    new_results[['State', 'Party']] = pd.DataFrame(new_results['State_Party'].to_list(), index=new_results.index)
    new_results = new_results.drop(columns=['State_Party'])
    
    # Concatenate the existing and new results
    all_results = pd.concat([existing_results, new_results], ignore_index=True)
    
    # Save the combined results to an Excel file
    all_results.to_excel('vote_results.xlsx', index=False)
    selected_party = selected_party_var.get()
        
    # Update the vote results dictionary
    selected_state = state_var.get()
    vote_results[(selected_state, selected_party)] += 1
        
    messagebox.showinfo("Vote Submitted", f"You have voted for {selected_party}. Thank you for participating in the election!")
    root.destroy()

def open_voting_window():
    def generate_otp():
        return str(random.randint(100000, 999999))
    
    def send_otp(phone_number, otp):
        print(f"OTP Sent to {phone_number}: {otp}")

    def submit_otp():
        user_otp = entry_otp.get()
        if user_otp == otp:
            messagebox.showinfo("OTP Verified", "OTP is valid. You can now select your state.")
            show_states()
            otp_label.pack_forget()
            entry_otp.pack_forget()
            submit_otp_button.pack_forget()
        else:
            messagebox.showerror("OTP Error", "Invalid OTP. Please try again.")

    def show_states():
        state_label.pack()
        state_var.set("Select a State")
        state_dropdown.pack()
        show_parties_button.pack()

    def show_political_parties():
        selected_state = state_var.get()
        parties = {
    "Andhra Pradesh": ["Telugu Desam Party (TDP)", "YSR Congress Party (YSRCP)", "Bharatiya Janata Party (BJP)", "Indian National Congress (INC)"],
    "Arunachal Pradesh": ["Bharatiya Janata Party (BJP)", "Indian National Congress (INC)", "National People's Party (NPP)", "Janata Dal (United) (JDU)"],
    "Assam": ["Bharatiya Janata Party (BJP)", "Indian National Congress (INC)", "All India United Democratic Front (AIUDF)", "Asom Gana Parishad (AGP)"]
    }
        
        selected_parties = parties.get(selected_state, [])
        
        if selected_parties:
            party_label.pack()
            party_var.set(selected_parties[0])
            party_dropdown['menu'].delete(0, 'end')
            
            for party in selected_parties:
                party_dropdown['menu'].add_command(label=party, command=lambda p=party: party_var.set(p))
            
            create_party_radio_buttons(selected_parties)
            show_vote_button()
        else:
            party_label.pack_forget()
            party_dropdown.pack_forget()
            hide_vote_button()
            messagebox.showwarning("No Parties", "No political parties available for the selected state.")

    def create_party_radio_buttons(parties):
        party_radio_label.pack()
        selected_party_var.set(parties[0])
        
        for party in parties:
            party_radio = tk.Radiobutton(root, text=party, variable=selected_party_var, value=party)
            party_radio.pack()

    def show_vote_button():
        vote_button.pack()

    def hide_vote_button():
        vote_button.pack_forget()

    def vote():
        selected_party = selected_party_var.get()
        
        # Update the vote results dictionary
        selected_state = state_var.get()
        vote_results[(selected_state, selected_party)] += 1
        
        messagebox.showinfo("Vote Submitted", f"You have voted for {selected_party}. Thank you for participating in the election!")
        root.destroy()

    root = tk.Tk()
    root.geometry('500x500')
    root.title("State Election System")

    otp = generate_otp()
    send_otp("your REGISTERED MOBILE NUMBER", otp)

    otp_label = tk.Label(root, text="Enter OTP:")
    otp_label.pack()

    entry_otp = tk.Entry(root)
    entry_otp.pack()

    submit_otp_button = tk.Button(root, text="Submit OTP", command=submit_otp)
    submit_otp_button.pack()

    state_label = tk.Label(root, text="Select State:")
    state_var = tk.StringVar()
    state_dropdown = tk.OptionMenu(root, state_var, "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal")
    state_label.pack_forget()
    state_dropdown.pack_forget()

    show_parties_button = tk.Button(root, text="Show Parties", command=show_political_parties)
    show_parties_button.pack_forget()

    party_label = tk.Label(root, text="")
    party_var = tk.StringVar()
    party_dropdown = tk.OptionMenu(root, party_var, "Loading...")
    party_label.pack_forget()
    party_dropdown.pack_forget()

    party_radio_label = tk.Label(root, text="Select Political Party:")
    selected_party_var = tk.StringVar()
    party_radio_label.pack_forget()

    vote_button = tk.Button(root, text="Vote", command=save_vote_results_to_excel)
    vote_button.pack_forget()

    root.mainloop()

app = tk.Tk()
app.geometry('500x500')
app.title("Login Page")

aadhar_label = ttk.Label(app, text="Aadhar Number:")
voter_id_label = ttk.Label(app, text="Voter ID:")
aadhar_label.grid(row=0, column=0)
voter_id_label.grid(row=1, column=0)

aadhar_entry = ttk.Entry(app)
voter_id_entry = ttk.Entry(app)
aadhar_entry.grid(row=0, column=1)
voter_id_entry.grid(row=1, column=1)

login_button = ttk.Button(app, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2)

result_label = ttk.Label(app, text="")
result_label.grid(row=3, column=0, columnspan=2)

app.mainloop()
'''
# Function to save the vote results to an Excel sheet
def save_vote_results_to_excel():
    # Load existing vote results from Excel
    existing_results = pd.read_excel('vote_results.xlsx')
    
    # Create a DataFrame from the vote_results dictionary
    new_results = pd.DataFrame(list(vote_results.items()), columns=['State_Party', 'Votes'])
    new_results[['State', 'Party']] = pd.DataFrame(new_results['State_Party'].to_list(), index=new_results.index)
    new_results = new_results.drop(columns=['State_Party'])
    
    # Concatenate the existing and new results
    all_results = pd.concat([existing_results, new_results], ignore_index=True)
    
    # Save the combined results to an Excel file
    all_results.to_excel('vote_results.xlsx', index=False)
    

# Create a button to save the vote results
save_results_button = tk.Button(text="Save Results", command=save_vote_results_to_excel)
save_results_button.pack()
'''

tk.mainloop()
