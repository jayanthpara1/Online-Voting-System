from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Simulate a database for user data (replace this with a real database)
users = [
    {"aadhar": "1234567890", "voter_id": "VOTER123", "status": "Not Voted", "phone": "1234567890"}
]

# Store generated OTPs for users
otp_cache = {}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    aadhar = request.form['aadhar']
    voter_id = request.form['voter_id']

    user = next((u for u in users if u['aadhar'] == aadhar and u['voter_id'] == voter_id), None)

    if user:
        if user['status'] == 'Not Voted':
            otp = str(random.randint(100000, 999999))
            otp_cache[aadhar] = otp  # Store OTP in cache
            send_otp(user['phone'], otp)  # Simulate sending OTP via SMS
            return jsonify({"status": "OTP Sent"})
        else:
            return jsonify({"status": "Already Voted"})
    else:
        return jsonify({"status": "Login Failed"})

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    aadhar = request.form['aadhar']
    user_otp = request.form['otp']

    stored_otp = otp_cache.get(aadhar)

    if stored_otp and user_otp == stored_otp:
        users[0]['status'] = 'Voted'  # Mark the user as voted
        return jsonify({"status": "OTP Verified"})
    else:
        return jsonify({"status": "Invalid OTP"})

# Simulate sending OTP via SMS (replace this with a real SMS service)
def send_otp(phone_number, otp):
    print(f"OTP Sent to {phone_number}: {otp}")

if __name__ == '__main__':
    app.run(debug=True)
