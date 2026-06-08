from .validations import get_deposit_amount, get_card_number, get_pin, get_withdraw_amount
from .constants import (
    ERR_CROSS_BANK_DEPOSIT, SUCCESS_DEPOSIT,
    BALANCE_HEADER, BALANCE_LABEL_NAME, BALANCE_LABEL_CARD, BALANCE_LABEL_BANK,
    BALANCE_LABEL_AMOUNT, BALANCE_SEPARATOR,
    ERR_INSUFFICIENT_ATM_FUNDS, ERR_INSUFFICIENT_USER_FUNDS, ERR_DAILY_LIMIT,
    ERR_CROSS_BANK_FEE, SUCCESS_WITHDRAWAL, MSG_CROSS_BANK_FEE, MSG_REMAINING_BALANCE
)


class ATM:
    """
    Represents an ATM machine that handles deposits, withdrawals, and balance inquiries.

    Attributes:
        atm_id (str): Unique identifier for this ATM (format: BankName_XXX).
        bank_name (str): Name of the bank that owns this ATM.
        balance (float): Current cash available in the ATM.
        bank (Bank): Reference to the parent Bank object (used for cross-bank fee revenue).
        location (str): Physical location of the ATM.
    """

    def __init__(self, atm_id, bank_name, initial_balance, bank, location):
        """
        Initializes an ATM with identification, cash, and location details.

        Args:
            atm_id (str): Auto-generated ATM ID (e.g., HDFC_001).
            bank_name (str): Name of the bank that owns this ATM.
            initial_balance (float): Starting cash loaded into the ATM.
            bank (Bank): Reference to the parent Bank object.
            location (str): Physical location of the ATM.
        """
        self.atm_id = atm_id
        self.bank_name = bank_name
        self.balance = initial_balance
        self.bank = bank
        self.location = location

    def deposit(self, current_user):
        """
        Handles a cash deposit from a user into the ATM.

        Deposit rules:
            - Cross-bank deposits are not allowed (card must belong to the same bank).
            - Minimum deposit: Rs. 100.
            - Deposit must be in multiples of Rs. 100.

        Args:
            current_user (User): The user making the deposit.
        """
        if self.bank_name != current_user.bank_name:
            print(ERR_CROSS_BANK_DEPOSIT)
            return

        amount = get_deposit_amount()
        current_user.balance += amount
        self.balance += amount
        print(SUCCESS_DEPOSIT.format(amount, current_user.balance))

    def check_balance(self, current_user):
        """
        Displays the account balance and related details for the authenticated user.

        Args:
            current_user (User): The authenticated user whose balance is being checked.
        """
        print(BALANCE_HEADER)
        print(BALANCE_LABEL_NAME.format(current_user.name))
        print(BALANCE_LABEL_CARD.format(current_user.card_number))
        print(BALANCE_LABEL_BANK.format(current_user.bank_name))
        print(BALANCE_LABEL_AMOUNT.format(current_user.balance))
        print(BALANCE_SEPARATOR)

    def withdraw(self, user):
        """
        Handles a cash withdrawal from the ATM by an authenticated user.

        Withdrawal rules:
            - Minimum withdrawal: Rs. 100.
            - Withdrawal must be in multiples of Rs. 100.
            - Maximum withdrawal per transaction: Rs. 10,000.
            - ATM must have sufficient cash.
            - User must have sufficient balance.
            - Limited to 10 withdrawals per day.
            - Cross-bank withdrawals incur a 5% fee (credited to the ATM's bank).

        Args:
            user (User): The authenticated user making the withdrawal.
        """
        amount = get_withdraw_amount()

        if self.balance < amount:
            print(ERR_INSUFFICIENT_ATM_FUNDS)
            return

        if user.balance < amount:
            print(ERR_INSUFFICIENT_USER_FUNDS)
            return

        if user.daily_withdrawal_count >= 10:
            print(ERR_DAILY_LIMIT)
            return

        fee = 0
        if self.bank_name != user.bank_name:
            fee = amount * 0.05
            total_deduction = amount + fee
            if user.balance < total_deduction:
                print(ERR_CROSS_BANK_FEE)
                return
            user.balance -= total_deduction
            self.bank.balance += fee
        else:
            user.balance -= amount

        self.balance -= amount
        user.daily_withdrawal_amount += amount
        user.daily_withdrawal_count += 1

        print(SUCCESS_WITHDRAWAL.format(amount))
        if fee > 0:
            print(MSG_CROSS_BANK_FEE.format(fee))
        print(MSG_REMAINING_BALANCE.format(user.balance))
