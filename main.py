import argparse
import os
from datetime import datetime
import json

class ExpenseSheet():

    def __init__(self):
        self.expenses = {}

    def add_expense(self, description:str, amount):
        """Adds expense to expense.json file with amount and brief description.

        Args:
            description (str): The brief description of expense.
            amount (float): The amount spent on expense.

        return:
            None

        """

        # To check if add argument is provided without amount and description.
        if amount is None and description is None:
            print("Please write amount and description in input section!\nfor user guide see readme.md file")
            return
        if amount is None:
            print("Please write amount in input section!\nfor user guide see readme.md file")
            return
        if description is None:
            print("Please write description in input section!\nfor user guide see readme.md file")
            return

        # save current date in variable
        current_date = datetime.today()
        current_date = current_date.strftime("%Y-%m-%d")

        # If file doesn't exist it will create automaticaly.
        if not os.path.exists("expenses.json"):
            with open("expenses.json", "w"):
                pass

        # If file is not empty then load its contents first in self.expenses
        if not os.path.getsize("expenses.json") == 0:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)

        # Calculates id for every expense.
        id = len(self.expenses) + 1 

        # If id already in expenses then move to new until its unique.
        while str(id) in self.expenses:
            id += 1

        self.expenses[id] = {"Description": description, "Amount": f"${amount}", "Date": current_date}

        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)

        print(f"Expense added successfully! id assigned {id}")
        
    def update_expense(self, description:str, amount, id):
        """Updates expense from expense.json file with amount and brief description.
        
            Args:
                description (str): The brief description of expense.
                amount (float): The amount spent on expense.
                id (int): The unique id of expense.
    
            return:
                None

            """

        try:

            # To check if update argument is provided without amount, description or id.

            if amount is None:
                print("Please write amount in input section!\nfor user guide see readme.md file")
                return
            if description is None:
                print("Please write description in input section!\nfor user guide see readme.md file")
                return
            if id is None:
                print("Please write id in input section!\nfor user guide see readme.md file")
                return

            # convert id to str so it can match with id from json file.
            id = str(id)

            # Terminate function if file is empty.    
            if os.path.getsize("expenses.json") == 0:
                print("File is empty, add expenses first!")
                return

            current_date = datetime.today()
            current_date = current_date.strftime("%Y-%m-%d")

            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)

            self.expenses[id]["Description"] = description
            self.expenses[id]["Amount"] = f"${amount}"
            self.expenses[id]["Date"] = current_date 

            with open("expenses.json", "w") as file:
                json.dump(self.expenses, file, indent=4)

            print(f"Task {id} updated successfully!")

        except FileNotFoundError as e:
            print("Error occured:", e)
        except KeyError as key:
            print(f"Id {key} doesn't exist in file!")

    def delete_expense(self, id):
        """Deletes expense from expense.json.
                
            Args:
                id (int): The unique id of expense to delete.
    
            return:
                None
    
            """
        try:

            # To check if delete argument is provided without id.
            if id is None:
                print("Please write id in input section!\nfor user guide see readme.md file")
                return

            # Type conversion of id is necessary because text from json file is always in string.
            id = str(id)
            
            if os.path.getsize("expenses.json") == 0:
                print("File is empty, add expenses first!")

            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)

            del self.expenses[id]

            with open("expenses.json", "w") as file:
                json.dump(self.expenses, file, indent=4)

            print(f"Task {id} deleted successfully!")

        except KeyError as key:
            print(f"Id {key} doesn't exist in file!")
        except FileNotFoundError as e:
            print("Error occurred", e)

    def list_expenses(self):
        """Lists all expenses stored in expense.json file."""

        try:

            if os.path.getsize("expenses.json") == 0:
                print("File is empty, add expenses first!")
                return

            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)

            print(f"{"Id":<4} | {"Date":<15} | {"Description":<15} | {"Amount":>10}")
            print(f"-" * 53)

            for id, details in self.expenses.items():
                print(f"{id:<4} | {details["Date"]:<15} | {details["Description"]:<15} | {details["Amount"]:>10}")

        except FileNotFoundError as e:
            print("Error occurred", e)

    def summarize_expenses(self, month=None):
        """Summarizes all expenses stored in expense.json file.

            Args:
                month (int) optional: Given month to summarize expenses.
            
            Returns:
                None

            """

        try:
            
            if os.path.getsize("expenses.json") == 0:
                print("File is empty, add expenses first!")
                return

            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)

            # If month argument is not given then it will summarize all 
            # the expenses otherwise, for given month only.
            if month is None:
                
                summary = 0

                for id, details in self.expenses.items():
                    amount = details["Amount"].strip("$")
                    summary += float(amount)

                print(f"Total expenses: ${summary}")

            else:

                summary = 0
                
                for id, details in self.expenses.items():
                    expense_month = details["Date"]
                    if str(month) == expense_month[5:7]:
                        amount = details["Amount"].strip("$")
                        summary += float(amount)

                print(f"Total expenses: ${summary}")

        except FileNotFoundError as e:
            print("Error occurred", e)

def main():
    """Takes input from user and executes all the function accordingly."""

    expense_sheet1 = ExpenseSheet()

    parser = argparse.ArgumentParser("A simple CLI application to track and manage expenses.")

    parser.add_argument("Function", type=str.lower, help="The name of function to call")

    parser.add_argument("-d", "--description", type=str.lower, help="The description of expense")

    parser.add_argument("-a", "--amount", type=float, help="The amount spent on expense")

    parser.add_argument("-id", "--id", type=int, help="The id of expense")

    parser.add_argument("-m", "--month", type=int, help="The month of expenses to summarize")

    args = parser.parse_args()

    if args.Function == "add":
        expense_sheet1.add_expense(args.description, args.amount)
    elif args.Function == "delete":
        expense_sheet1.delete_expense(args.id)
    elif args.Function == "update":
        expense_sheet1.update_expense(args.description, args.amount, args.id)
    elif args.Function == "list":
        expense_sheet1.list_expenses()
    elif args.Function == "summary":
        expense_sheet1.summarize_expenses(args.month)
    else:
        print("Incorrect command! please see readme.md for user guide")

if __name__ == "__main__":
    main()