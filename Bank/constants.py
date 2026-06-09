# KYC Input Prompts
ENTER_NAME = "Enter your full name: "
ENTER_DOB = "Enter your date of birth (DD/MM/YYYY): "
ENTER_PHONE_NUMBER = "Enter your phone number: "
ENTER_EMAIL = "Enter your email address: "
ENTER_AADHAR_NUMBER = "Enter your Aadhar number: "
ENTER_PAN_NUMBER = "Enter your PAN number: "
ENTER_INITIAL_BALANCE = "Enter initial deposit amount (minimum Rs. 1,000): "
ENTER_ATM_INITIAL_BALANCE = "Enter initial ATM balance (minimum Rs. 1,00,000): "
ENTER_LOCATION = "Enter ATM location: "

# Name errors
ERR_EMPTY_NAME = "Name cannot be empty."
ERR_DIGITS_NAME = "Name cannot contain digits."

# DOB errors
ERR_DOB_FORMAT = "Invalid date format. Use DD/MM/YYYY."
ERR_DOB_AGE = "You must be at least 16 years old to open an account."
ERR_DOB_HIGHER_AGE = "Age cannot exceed 100 years."

# Phone errors
ERR_PHONE_DIGITS = "Phone number must contain only digits."
ERR_PHONE_LENGTH = "Phone number must be exactly 10 digits."

# Email errors
ERR_EMAIL_FORMAT = "Invalid email format."

# Aadhar errors
ERR_AADHAR_DIGITS = "Aadhar number must contain only digits."
ERR_AADHAR_LENGTH = "Aadhar number must be exactly 12 digits."

# PAN errors
ERR_PAN_FORMAT = "Invalid PAN format. Format: ABCDE1234F"

# Balance errors
ERR_BALANCE_NOT_NUMBER = "Please enter a valid number."
ERR_BALANCE_MIN = "Initial deposit must be at least Rs. 1,000."
ERR_ATM_BALANCE_MIN = "ATM initial balance must be at least Rs. 1,00,000."

# Location errors
ERR_LOCATION_SHORT = "Location must be at least 2 characters."
ERR_LOCATION_LONG = "Location must not exceed 60 characters."

# ATM top-up
ENTER_AMOUNT_TO_ADD = "Enter amount to add to ATM (minimum Rs. 50,000): "
ERR_ATM_TOPUP_MIN = "Top-up amount must be at least Rs. 50,000."
HEADER_ADD_BALANCE = "\n--- Add Balance to ATM ---"
MSG_BALANCE_ADDED = "Successfully added Rs.{:.2f} to {}. New ATM balance: Rs.{:.2f}"
ERR_ATM_NOT_FOUND = "No ATMs available for this bank."
ERR_INSUFFICIENT_BANK_FUNDS = "Insufficient bank funds."

# View users
HEADER_VIEW_USERS = "\n--- Registered Users ---"
MSG_NO_USERS = "No users registered yet."

# View ATMs
HEADER_VIEW_ATMS = "\n--- Deployed ATMs ---"
MSG_NO_ATMS = "No ATMs deployed yet."

# Bank operation messages
HEADER_CREATE_USER = "\n--- Create User Account ---"
HEADER_CREATE_ATM = "\n--- Create ATM ---"
HEADER_ACCOUNT_SUCCESS = "\n--- Account Created Successfully ---"
MSG_ATM_SUCCESS = "\nATM created successfully!"
ERR_INSUFFICIENT_FUNDS = "Insufficient bank funds to deploy ATM with this balance."
