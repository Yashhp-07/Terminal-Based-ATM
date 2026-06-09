"""Constants for the Admin module.

Contains prompts, errors, success messages, and display headers
used during bank registration and system-wide viewing operations.
"""

# Input prompts
ENTER_BANK_NAME = "Enter bank name: "
ENTER_BANK_USERNAME = "Enter bank username: "
ENTER_BANK_PASSWORD = "Enter bank password: "
ENTER_BANK_BALANCE = "Enter initial bank balance (minimum Rs. 10,00,000): "

# Validation errors
ERR_BANK_NAME_EMPTY = "Bank name cannot be empty."
ERR_BANK_NAME_LENGTH = "Bank name must be between 2 and 30 characters."
ERR_BANK_NAME_EXISTS = "A bank with this name already exists."
ERR_BANK_USERNAME_EMPTY = "Username cannot be empty."
ERR_BANK_USERNAME_LENGTH = "Username must be between 3 and 20 characters."
ERR_BANK_PASSWORD_SHORT = "Password must be at least 6 characters long."
ERR_BALANCE_NOT_NUMBER = "Please enter a valid number."
ERR_BALANCE_MIN = "Initial bank balance must be at least Rs. 10,00,000."

# Success messages
SUCCESS_BANK_CREATED = "\nBank created successfully!"

# View headers and messages
HEADER_CREATE_BANK = "\n--- Create Bank ---"
HEADER_ALL_BANKS = "\n--- All Banks ---"
HEADER_ALL_USERS = "\n--- All Users ---"
HEADER_ALL_ATMS = "\n--- All ATMs ---"
MSG_NO_BANKS = "No banks registered yet."
