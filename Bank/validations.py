import re
from datetime import datetime

from .constants import (
    ENTER_NAME, ERR_EMPTY_NAME, ERR_DIGITS_NAME,
    ENTER_DOB, ERR_DOB_FORMAT, ERR_DOB_AGE, ERR_DOB_HIGHER_AGE,
    ENTER_PHONE_NUMBER, ERR_PHONE_DIGITS, ERR_PHONE_LENGTH,
    ENTER_EMAIL, ERR_EMAIL_FORMAT,
    ENTER_AADHAR_NUMBER, ERR_AADHAR_DIGITS, ERR_AADHAR_LENGTH,
    ENTER_PAN_NUMBER, ERR_PAN_FORMAT,
    ENTER_INITIAL_BALANCE, ERR_BALANCE_NOT_NUMBER, ERR_BALANCE_MIN,
    ENTER_ATM_INITIAL_BALANCE, ERR_ATM_BALANCE_MIN,
    ENTER_AMOUNT_TO_ADD, ERR_ATM_TOPUP_MIN,
    ENTER_LOCATION, ERR_LOCATION_SHORT, ERR_LOCATION_LONG
)


def validate_name():
    while True:
        name = input(ENTER_NAME)
        if not name:
            print(ERR_EMPTY_NAME)
            continue
        if any(ch.isdigit() for ch in name):
            print(ERR_DIGITS_NAME)
            continue
        return name


def validate_dob():
    while True:
        dob = input(ENTER_DOB)
        try:
            dob_date = datetime.strptime(dob, "%d/%m/%Y")
        except ValueError:
            print(ERR_DOB_FORMAT)
            continue

        today = datetime.now()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        if age < 16:
            print(ERR_DOB_AGE)
            continue
        if age > 100:
            print(ERR_DOB_HIGHER_AGE)
            continue
        return dob


def validate_phone_number():
    while True:
        phone = input(ENTER_PHONE_NUMBER)
        if not phone.isdigit():
            print(ERR_PHONE_DIGITS)
            continue
        if len(phone) != 10:
            print(ERR_PHONE_LENGTH)
            continue
        return phone


def validate_email():
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    while True:
        email = input(ENTER_EMAIL)
        if not pattern.fullmatch(email):
            print(ERR_EMAIL_FORMAT)
            continue
        return email.lower()


def validate_aadhar_number():
    while True:
        aadhar = input(ENTER_AADHAR_NUMBER)
        if not aadhar.isdigit():
            print(ERR_AADHAR_DIGITS)
            continue
        if len(aadhar) != 12:
            print(ERR_AADHAR_LENGTH)
            continue
        return aadhar


def validate_pan_number():
    pattern = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]$")
    while True:
        pan = input(ENTER_PAN_NUMBER)
        if not pattern.fullmatch(pan.upper()):
            print(ERR_PAN_FORMAT)
            continue
        return pan.upper()


def validate_amount(prompt, minimum, error_message):
    while True:
        value = input(prompt)
        try:
            amount = float(value)
        except ValueError:
            print(ERR_BALANCE_NOT_NUMBER)
            continue
        if amount < minimum:
            print(error_message)
            continue
        return amount


def validate_initial_balance():
    return validate_amount(ENTER_INITIAL_BALANCE, 1000, ERR_BALANCE_MIN)


def validate_atm_initial_balance():
    return validate_amount(ENTER_ATM_INITIAL_BALANCE, 100000, ERR_ATM_BALANCE_MIN)


def validate_atm_topup_balance():
    return validate_amount(ENTER_AMOUNT_TO_ADD, 50000, ERR_ATM_TOPUP_MIN)


def validate_location():
    while True:
        location = input(ENTER_LOCATION)
        if len(location) < 2:
            print(ERR_LOCATION_SHORT)
            continue
        if len(location) > 60:
            print(ERR_LOCATION_LONG)
            continue
        return location
