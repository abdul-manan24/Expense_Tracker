import os
from datetime import datetime
import json

class ExpenseSheet():

    def __init__(self):
        self.expenses = {}

    def add_expense(self, description:str, amount):

        current_date = datetime.today()
        current_date = current_date.strftime("%Y-%m-%d")

        if not os.path.exists("expenses.json"):
            with open("expenses.json", "w"):
                pass

        if not os.path.getsize("expenses.json") == 0:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)

        id = len(self.expenses) + 1
        self.expenses[id] = {"Description": description, "Amount": f"${amount}", "Date": current_date}

        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)

        print(f"Expense added successfully! id assigned {id}")
        
    def update_expense(self, description:str, amount, id):

        current_date = datetime.today()
        current_date = current_date.strftime("%Y-%m-%d")

        with open("expenses.json", "r") as file:
            self.expenses = json.load(file)

        id = str(id)
        self.expenses[id]["Description"] = description
        self.expenses[id]["Amount"] = f"${amount}"
        self.expenses[id]["Date"] = current_date

        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)

        print(f"Task {id} updated successfully!")

    def delete_expense(self, id):

        with open("expenses.json", "r") as file:
            self.expenses = json.load(file)

        id = str(id)
        del self.expenses[id]

        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)

        print(f"Task {id} deleted successfully!")

    def list_expenses(self):
        with open("expenses.json", "r") as file:
            self.expenses = json.load(file)

        print(f"{"Id":<4} | {"Date":<15} | {"Description":<15} | {"Amount":>10}")
        print(f"-" * 53)

        for id, details in self.expenses.items():
            print(f"{id:<4} | {details["Date"]:<15} | {details["Description"]:<15} | {details["Amount"]:>10}")

    def summarize_expenses(self):

        with open("expenses.json", "r") as file:
            self.expenses = json.load(file)

        summary = 0

        for id, details in self.expenses.items():
            summary += details["Amount"]

        print(f"Total expenses: ${summary}")

def take_input():
    pass

if __name__ == "__main__":
    expense_sheet1 = ExpenseSheet()
    # expense_sheet1.add_expense("xyz", 20)
    # expense_sheet1.add_expense("abc", 30)
    # expense_sheet1.add_expense("dcs", 40)
    # expense_sheet1.add_expense("efg", 30)
    expense_sheet1.update_expense("Clothes", 100, 1)
    expense_sheet1.update_expense("Lunch", 50, 2)
    expense_sheet1.update_expense("Breakfast", 60, 3)
    expense_sheet1.update_expense("Hostel fee", 14000, 4)
    # expense_sheet1.summarize_expenses()
    expense_sheet1.list_expenses()