from models.expense import Expense
import csv

expenses = []

def load_expenses(filepath="expenses.csv"):
    try:
        categories = set()
        with open(filepath, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                categories.add(row['category'])
                expenses.append(
                    Expense(
                        name=row["name"],
                        category=row["category"],
                        date=row["date"]
                    )
                )
        Expense.load_categories(categories)
    except FileNotFoundError:
        raise Exception(f"The expense sheet {filepath} was not found.")
