"""Constants for the Menu module.

Contains all user-facing strings used by the interactive menu system,
including authentication messages, menu options, headers, display formats,
input prompts, and error messages.
"""

# Separators
SEPARATOR_EQUAL = "=" * 45
SEPARATOR_DASH = "-" * 45

# Authentication - User
MSG_AUTH_SUCCESS = "Authentication successful."
ERR_INVALID_CREDENTIALS = "Invalid card number or PIN."
REMAINING_ATTEMPTS = "Attempts remaining: {}"
ERR_CREDENTIALS_EXHAUSTED = "Too many failed attempts. Access denied."

# Authentication - Admin
HEADER_ADMIN_LOGIN = "\n--- Admin Login ---"
SUCCESS_ADMIN_LOGIN = "Admin login successful."

# Authentication - Bank
ENTER_BANK_USERNAME = "Enter bank username: "
ENTER_BANK_PASSWORD = "Enter bank password: "
HEADER_BANK_LOGIN = "\n--- Bank Login ---"
SUCCESS_BANK_LOGIN = "Bank login successful."
ERR_WRONG_BANK_CREDENTIALS = "Wrong username or password."
ERR_WRONG_BANK_CREDENTIALS_REMAINING = "Attempts remaining: {}"
ERR_WRONG_BANK_CREDENTIALS_EXHAUSTED = "Too many failed attempts. Access denied."

# Headers
HEADER_SELECT_BANK = "\n--- Select Bank ---"
HEADER_SELECT_ATM = "\n--- Select ATM ---"
HEADER_ADMIN_PANEL = "\n--- Admin Panel ---"
HEADER_ATM_MENU = "\n--- ATM Menu ---"

# Menu options - Admin
MENU_ADMIN_CREATE_BANK = "1. Create a Bank"
MENU_ADMIN_VIEW_BANKS = "2. View All Banks"
MENU_ADMIN_VIEW_USERS = "3. View All Users"
MENU_ADMIN_VIEW_ATMS = "4. View All ATMs"
MENU_ADMIN_BACK = "5. Back to Main Menu"

# Menu options - Bank
MENU_BANK_CREATE_USER = "1. Create User Account"
MENU_BANK_DEPLOY_ATM = "2. Deploy ATM"
MENU_BANK_ADD_BALANCE = "3. Add Balance to ATM"
MENU_BANK_VIEW_USERS = "4. View All Users"
MENU_BANK_VIEW_ATMS = "5. View All ATMs"
MENU_BANK_BACK = "6. Back to Main Menu"

# Menu options - ATM
MENU_ATM_BALANCE = "1. Check Balance"
MENU_ATM_DEPOSIT = "2. Deposit"
MENU_ATM_WITHDRAW = "3. Withdraw"
MENU_ATM_CHANGE_PIN = "4. Change PIN"
MENU_ATM_BACK = "5. Back to Main Menu"

# Display formats
DISPLAY_BANK_ITEM = "{}. {}"
DISPLAY_ATM_ITEM = "{}. {} - {} ({})"
DISPLAY_BANK_PANEL_HEADER = "--- {} Bank Panel ---"
DISPLAY_BANK_FUNDS = "Bank Funds: Rs.{:.2f}"
DISPLAY_ATM_INFO = "ATM: {}"
DISPLAY_ATM_LOCATION = "Location: {}"

# Input prompts
ENTER_CHOICE = "Enter your choice: "
ENTER_SELECT_BANK = "Select a bank: "
ENTER_SELECT_ATM = "Select an ATM: "

# Errors
ERR_INVALID_CHOICE = "Invalid choice."
ERR_INVALID_CHOICE_RANGE = "Invalid choice. Please enter a number between 1 and {}."
ERR_INVALID_SELECTION = "Invalid selection."
ERR_NOT_A_NUMBER = "Please enter a valid number."

# Info messages
MSG_NO_BANKS_REGISTERED = "\nNo banks registered yet."
MSG_NO_ATMS_AVAILABLE = "\nNo ATMs available."
MSG_RETURNING_MAIN = "Returning to main menu."
