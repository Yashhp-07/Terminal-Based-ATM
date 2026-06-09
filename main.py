"""Main entry point for the Terminal-Based ATM System.

Seeds the system with pre-configured data and launches the interactive
menu-driven interface for Admin, Bank, and User roles.
"""

from Data.data import seed_system
from Menus.menu import Menu
from constants import (
    HEADER_WELCOME, MENU_ROLE_ADMIN, MENU_ROLE_BANK, MENU_ROLE_USER,
    MENU_ROLE_EXIT, PROMPT_SELECT_ROLE, ERR_INVALID_ROLE, EXIT_MSG
)


def main():
    admin = seed_system()
    menu = Menu(admin)

    while True:
        print(HEADER_WELCOME)
        print(MENU_ROLE_ADMIN)
        print(MENU_ROLE_BANK)
        print(MENU_ROLE_USER)
        print(MENU_ROLE_EXIT)

        choice = input(PROMPT_SELECT_ROLE)
        if choice == "1":
            menu.handle_admin()
        elif choice == "2":
            menu.handle_bank()
        elif choice == "3":
            menu.handle_user()
        elif choice == "4":
            print(EXIT_MSG)
            break
        else:
            print(ERR_INVALID_ROLE)


if __name__ == "__main__":
    main()
