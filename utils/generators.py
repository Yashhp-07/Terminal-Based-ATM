# Generators for unique IDs and credentials

import random
import string


def generate_bank_id():
    """Generate a unique bank ID in format BNK_XXXXXX"""
    return "BNK_" + "".join(random.choices(string.digits, k=6))


def generate_user_id():
    """Generate a unique user ID in format USR_XXXXXX"""
    return "USR_" + "".join(random.choices(string.digits, k=6))


def generate_atm_id(bank_name):
    """Generate a unique ATM ID based on bank name and random number"""
    return f"{bank_name}_{str(random.randint(0, 999)).zfill(3)}"


def generate_card_number():
    """Generate a 16-digit card number"""
    return "".join(random.choices(string.digits, k=16))


def generate_pin():
    """Generate a 4-digit PIN"""
    return str(random.randint(0, 9999)).zfill(4)
