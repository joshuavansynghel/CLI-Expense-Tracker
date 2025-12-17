from models.expense import Expense
from storage.storage_handler import StorageHandler

def add_expense_command(subparsers):
    add_parser = subparsers.add_parser(
        "add",
        help="Add a new expense"
    )

    add_parser.add_argument(
        "--amount",
        type=float,
        required=True,
        help="Expense amount"
    )

    add_parser.add_argument(
        "--category",
        type=str,
        required=True,
        help="Expense category"
    )

    add_parser.add_argument(
        "--date",
        type=str,
        help="Expense date (YYYY-MM-DD)"
    )

    add_parser.add_argument(
        "--note",
        type=str,
        help="Optional note"
    )

    add_parser.set_defaults(func=handle_add_expense)

def handle_add_expense(args):
    # if args.date:
    #     validate_date(args.date)

    expense = Expense(
        amount=args.amount,
        category=args.category,
        date=args.date,
        note=args.note,
    )

    storage = StorageHandler()
    storage.add_expense(expense)
    storage.save()


