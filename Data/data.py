import hashlib

from Admin.admin import Admin
from Bank.bank import Bank
from Atm.atm import ATM
from Users.users import User


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


ADMIN_DATA = {"username": "admin", "password_hash": hash_password("admin123")}

BANKS_DATA = [
    {"bank_id": "BNK_000001", "name": "HDFC", "username": "hdfc_admin", "password": "hdfc123", "balance": 50000000},
    {"bank_id": "BNK_000002", "name": "SBI", "username": "sbi_admin", "password": "sbi123", "balance": 50000000},
]

ATMS_DATA = [
    {"atm_id": "HDFC_001", "bank_name": "HDFC", "balance": 500000, "location": "Andheri"},
    {"atm_id": "HDFC_002", "bank_name": "HDFC", "balance": 500000, "location": "Bandra"},
    {"atm_id": "SBI_001", "bank_name": "SBI", "balance": 500000, "location": "Dadar"},
    {"atm_id": "SBI_002", "bank_name": "SBI", "balance": 500000, "location": "Colaba"},
]

USERS_DATA = [
    {
        "user_id": "USR_000001", "name": "Yash Patel", "dob": "15/08/2001",
        "phone_number": "9876543210", "email": "yash@email.com",
        "aadhar_number": "111122223333", "pan_number": "ABCDE1234F",
        "balance": 50000, "bank_name": "HDFC", "card_number": "1111222233334444", "atm_pin": "1234"
    },
    {
        "user_id": "USR_000002", "name": "Priya Sharma", "dob": "22/03/1998",
        "phone_number": "9876543211", "email": "priya@email.com",
        "aadhar_number": "444455556666", "pan_number": "FGHIJ5678K",
        "balance": 75000, "bank_name": "HDFC", "card_number": "5555666677778888", "atm_pin": "5678"
    },
    {
        "user_id": "USR_000003", "name": "Amit Kumar", "dob": "10/11/1995",
        "phone_number": "9876543212", "email": "amit@email.com",
        "aadhar_number": "777788889999", "pan_number": "KLMNO9012P",
        "balance": 60000, "bank_name": "SBI", "card_number": "9999888877776666", "atm_pin": "9012"
    },
    {
        "user_id": "USR_000004", "name": "Neha Gupta", "dob": "05/06/2000",
        "phone_number": "9876543213", "email": "neha@email.com",
        "aadhar_number": "222233334444", "pan_number": "PQRST3456U",
        "balance": 85000, "bank_name": "SBI", "card_number": "3333444455556666", "atm_pin": "3456"
    },
]


def seed_system():
    admin = Admin(ADMIN_DATA["username"], ADMIN_DATA["password_hash"])

    for bank_data in BANKS_DATA:
        bank = Bank(
            bank_data["bank_id"], bank_data["name"],
            bank_data["username"], hash_password(bank_data["password"]),
            bank_data["balance"]
        )
        admin.banks[bank_data["name"]] = bank

    for atm_data in ATMS_DATA:
        bank = admin.banks[atm_data["bank_name"]]
        atm = ATM(atm_data["atm_id"], atm_data["bank_name"], atm_data["balance"], bank, atm_data["location"])
        bank.atms[atm_data["atm_id"]] = atm
        bank.balance -= atm_data["balance"]

    for user_data in USERS_DATA:
        bank = admin.banks[user_data["bank_name"]]
        user = User(
            user_data["user_id"], user_data["name"], user_data["dob"],
            user_data["phone_number"], user_data["email"],
            user_data["aadhar_number"], user_data["pan_number"],
            user_data["balance"], user_data["bank_name"],
            user_data["card_number"], user_data["atm_pin"]
        )
        bank.users[user_data["card_number"]] = user

    return admin
