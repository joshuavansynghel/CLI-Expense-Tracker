import argparse

from commands.add_expense import add_expense_command
from storage.storage_handler import StorageHandler
from models.expense import Expense

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(required=True)

    subparsers = subparsers.add_parser(
        title="commands",
        dest="command",
        required=True
    )

    # Register the add command
    add_expense_command(subparsers)

    args = parser.parse_args()

    # Dispatch to selected command
    args.func(args)

if __name__ == "__main__":
    main()