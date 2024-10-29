def login():
    aadhar = aadhar_entry.get().strip()
    voter_id = voter_id_entry.get().strip()
    
    try:
        data = pd.read_excel('voter_data.xlsx')
        
        # Convert both Aadhar and Voter ID to lowercase for a case-insensitive comparison
        data['Aadhar Number'] = data['Aadhar Number'].str.strip().str.lower()
        data['Voter ID'] = data['Voter ID'].str.strip().str.lower()
        
        matching_data = data[(data['Aadhar Number'] == aadhar.lower()) & (data['Voter ID'] == voter_id.lower())]
        
        if not matching_data.empty:
            result_label.config(text="Login Successful")
        else:
            result_label.config(text="Login Failed. Please try again.")
    except FileNotFoundError:
        result_label.config(text="No Excel file found")
