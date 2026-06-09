import re
from datetime import datetime


def validate_name():
    while True:
        name = input("Enter your full name: ")
        if not name:
            print("Name cannot be empty.")
            continue
        if any(ch.isdigit() for ch in name):
            print("Name cannot contain digits.")
            continue
        return name


def validate_dob():
    while True:
        dob = input("Enter your date of birth (DD/MM/YYYY): ")
        try:
            dob_date = datetime.strptime(dob, "%d/%m/%Y")
        except ValueError:
            print("Invalid date format. Use DD/MM/YYYY.")
            continue

        today = datetime.now()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        if age < 16:
            print("You must be at least 16 years old to open an account.")
            continue
        if age > 100:
            print("Age cannot exceed 100 years.")
            continue
        return dob


def validate_phone_number():
    while True:
        phone = input("Enter your phone number: ")
        if not phone.isdigit():
            print("Phone number must contain only digits.")
            continue
        if len(phone) != 10:
            print("Phone number must be exactly 10 digits.")
            continue
        return phone


def validate_email():
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    while True:
        email = input("Enter your email address: ")
        if not pattern.fullmatch(email):
            print("Invalid email format.")
            continue
        return email.lower()


def validate_aadhar_number():
    while True:
        aadhar = input("Enter your Aadhar number: ")
        if not aadhar.isdigit():
            print("Aadhar number must contain only digits.")
            continue
        if len(aadhar) != 12:
            print("Aadhar number must be exactly 12 digits.")
            continue
        return aadhar


def validate_pan_number():
    pattern = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]$")
    while True:
        pan = input("Enter your PAN number: ")
        if not pattern.fullmatch(pan.upper()):
            print("Invalid PAN format. Format: ABCDE1234F")
            continue
        return pan.upper()


def validate_amount(prompt, minimum, error_message):
    while True:
        value = input(prompt)
        try:
            amount = float(value)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if amount < minimum:
            print(error_message)
            continue
        return amount


def validate_initial_balance():
    return validate_amount(
        "Enter initial deposit amount (minimum Rs. 1,000): ",
        1000,
        "Initial deposit must be at least Rs. 1,000."
    )


def validate_atm_initial_balance():
    return validate_amount(
        "Enter initial ATM balance (minimum Rs. 1,00,000): ",
        100000,
        "ATM initial balance must be at least Rs. 1,00,000."
    )


def validate_location():
    while True:
        location = input("Enter ATM location: ")
        if len(location) < 2:
            print("Location must be at least 2 characters.")
            continue
        if len(location) > 60:
            print("Location must not exceed 60 characters.")
            continue
        return location
