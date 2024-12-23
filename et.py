import json
from datetime import datetime

class Expense:
    def __init__(self, amount, category, description=""):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

class ExpenseTracker:
    def __init__(self, file_name="expenses.json"):
        self.file_name = file_name
        self.expenses = self.load_expenses()
    
    def load_expenses(self):
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def add_expense(self, expense):
        self.expenses.append(expense.to_dict())
        self.save_expenses()
    
    def save_expenses(self):
        with open(self.file_name, "w") as file:
            json.dump(self.expenses, file, indent=4)
    
    def get_total_expense(self):
        return sum(expense["amount"] for expense in self.expenses)
    
    def filter_by_category(self, category):
        return [expense for expense in self.expenses if expense["category"] == category]
    
    def display_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\nRecorded Expenses:")
        for expense in self.expenses:
            print(
                f"- {expense['date']} | {expense['category']}: ${expense['amount']} | {expense['description']}"
            )

if __name__ == "__main__":
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Total Expense")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            try:
                amount = float(input("Enter the amount: "))
                category = input("Enter the category (e.g., Food, Transport, etc.): ")
                description = input("Enter a description (optional): ")
                expense = Expense(amount, category, description)
                tracker.add_expense(expense)
                print("Expense added successfully!")
            except ValueError:
                print("Invalid input. Please try again.")
        
        elif choice == "2":
            tracker.display_expenses()
        
        elif choice == "3":
            category = input("Enter the category to filter by: ")
            filtered_expenses = tracker.filter_by_category(category)
            if filtered_expenses:
                print(f"\nExpenses in category '{category}':")
                for expense in filtered_expenses:
                    print(
                        f"- {expense['date']} | ${expense['amount']} | {expense['description']}"
                    )
            else:
                print(f"No expenses found in category '{category}'.")
        
        elif choice == "4":
            print(f"Total Expense: ${tracker.get_total_expense():.2f}")
        
        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
