from pathlib import Path

class Expense:
    _id_file = Path("expense_id_counter.txt") # file to store last expense id
    categories = set() 

    def __init__(self, amount, name, category, date, note):
        self.id = self._next_id()
        self.amount = amount
        self.name = name
        self.category = self._validate_category(category)
        self.date = date
        self.note = note

    @classmethod
    def load_categories(cls, categories):
        cls.categories = set(categories)

    @classmethod
    def _load_counter(cls):
        if cls._id_file.exists():
            return int(cls._id_file.read_text())
        return 1
    
    @classmethod
    def _save_counter(cls, value):
        cls._id_file.write_text(str(value))

    @classmethod
    def _next_id(cls):
        counter = cls._load_counter()
        cls._save_counter(counter + 1)
        return counter
    
    @classmethod
    def _validate_category(cls, category):
        if category in cls.categories:
            return category
        
        print(f"Category {category} does not exist.")
        print(f"Existing categories: {', '.join(sorted(cls.categories))}")

        choice = input(f"Add '{category}' as a new category? (y/n): ").strip().lower()

        if choice == "y":
            cls.categories.add(category)
            return category

        while True:
            replacement = input("Enter an existing category: ").strip()
            if replacement in cls.categories:
                return replacement
            print(f"Invalid category. Try again.")

    