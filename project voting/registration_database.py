import pandas as pd

# Function to save user data to Excel
def save_user_data(data):
    try:
        df_existing = pd.read_excel('userdata.xlsx')
        df_new = pd.DataFrame(data)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_excel('userdata.xlsx', index=False)
    except FileNotFoundError:
        df = pd.DataFrame(data)
        df.to_excel('userdata.xlsx', index=False)

# Function to check login credentials
def check_login(aadhar, voter_id):
    df = pd.read_excel('userdata.xlsx')
    user = df.loc[(df['Aadhar Number'] == aadhar) & (df['Voter ID'] == voter_id), 'Name']
    if len(user) > 0:
        return user.iloc[0]
    else:
        return None

# Function to display login success message
def display_login_success(name):
    print(f"Login successful! Welcome, {name}.")

# Main program
def main():
    # User registration
    data = []
    print("User Registration:")
    name = input("Name: ")
    aadhar = input("Aadhar Number: ")
    gender = input("Gender (M/F): ")
    age = input("Age: ")
    voter_id = input("Voter ID: ")
    pan_card = input("PAN Card Number: ")
    phone = input("Phone Number: ")
    data.append({
        'Name': name,
        'Aadhar Number': aadhar,
        'Gender': gender,
        'Age': age,
        'Voter ID': voter_id,
        'PAN Card Number': pan_card,
        'Phone Number': phone
    })
    save_user_data(data)
    print("User registered successfully!")

    # User login
    print("\nUser Login:")
    aadhar_login = input("Aadhar Number: ")
    voter_id_login = input("Voter ID: ")
    name = check_login(aadhar_login, voter_id_login)
    if name:
        display_login_success(name)
    else:
        print("Login failed. Invalid credentials.")

if __name__ == "__main__":
    main()
