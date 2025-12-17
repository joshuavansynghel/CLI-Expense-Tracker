from models.expense import Expense
import csv

class StorageHandler:
    
    def __init__(self, filepath="expenses.csv"):
        self.filepath = filepath
        self.expenses = self.load(filepath)

    def load(self):

        expenses = []

        try:
            # Open file and append each row as an expense
            with open(self.filepath) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    expenses.append(
                        Expense(
                            name=row["name"],
                            category=row["category"],
                            amount=row["amount"],
                            date=row["date"],
                            note=row["note"]
                        )
                    )
            return expenses
        
        except FileNotFoundError:
            raise Exception(f"The expense sheet {self.filepath} was not found")


    def save(self): 

        fieldnames = ["amount", "name", "category", "date", "note"]

        with open(self.filepath, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames)

            writer.writeheader()

            for expense in self.expenses:
                writer.writer({
                    "amount": expense.amount,
                    "name": expense.name,
                    "category": expense.category,
                    "date": expense.date,
                    "note": expense.note
                })

    def delete(self, expense_id):
        self.expenses = [e for e in self.expenses if e.id != expense_id]

    def add_expense(self, new_expense):
        self.expenses.append(new_expense)
        
