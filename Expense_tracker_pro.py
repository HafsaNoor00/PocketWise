import random
import json
from datetime import datetime


class Expense:
    def __init__(self, expense_id, amount, category, date, description, payment):
        self.id = expense_id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        self.payment = payment


class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.load_expenses()
        

    def add_expense(self, amount, category, date, description, payment):
        if not validate_amount(amount):
            return

        if not validate_category(category):
            return

        if not validate_date(date):
            return

        if not validate_description(description):
            return

        if not validate_payment(payment):
            return
        for existing_expense in self.expenses.values():
            
            if (
                existing_expense.amount == amount
                and existing_expense.category == category
                and existing_expense.date == date
                and existing_expense.description == description
                
        
             ):
             print("Duplicate expense detected.")
             return
         
        expense_id = random.randint(1000, 9999)

        while expense_id in self.expenses:
            expense_id = random.randint(1000, 9999)
        
        amount = float(amount)
        
        expense = Expense(
            expense_id,
            amount,
            category,
            date,
            description,
            payment
        )

        self.expenses[expense.id] = expense
        self.save_expenses()
        print("Expense added successfully!")
        print("Expense ID:", expense.id)
        

    def view_expense(self):
        if not self.expenses:
            print("No expenses found.")
            return

        for expense_id, expense in self.expenses.items():
            print("\n--------------------")
            print("ID:", expense.id)
            print("Amount:", expense.amount)
            print("Category:", expense.category)
            print("Date:", expense.date)
            print("Description:", expense.description)
            print("Payment:", expense.payment)

    def delete_expense(self):
        expense_id = input(
            "Enter the expense ID you want to delete: "
        ).strip()

        if expense_id.isdigit() and int(expense_id) in self.expenses:
            del self.expenses[int(expense_id)]
            self.save_expenses()
            print("Expense deleted successfully!")
        else:
            print("Expense not found.")

    def update_expense(self):
        expense_id = input(
            "Enter the expense ID you want to update: "
        ).strip()

        if not expense_id.isdigit() or int(expense_id) not in self.expenses:
            print("Expense not found.")
            return

        expense = self.expenses[int(expense_id)]

        field = input(
            "What do you want to update? "
            "amount/category/date/description/payment: "
        ).lower()

        if field == "amount":
            new_value = input("Enter new amount: ")
            
            if not validate_amount(new_value):
                return
            expense.amount = float(new_value)

        elif field == "category":
            new_value = input("Enter new category: ")
            if not validate_category(new_value):
                 return
            expense.category = new_value.title()

        elif field == "date":
            new_value = input("Enter new date: ")
            if not validate_date(new_value):
                return
            expense.date = new_value

        elif field == "description":
            new_value = input("Enter new description: ")
            if not validate_description(new_value):
                return
            expense.description = new_value

        elif field == "payment":
            new_value = input("Enter new payment: ")
            if not validate_payment(new_value):
                return
            expense.payment = new_value

        else:
            print("Invalid field.")
            return
        self.save_expenses()
        print("Expense updated successfully!")
        
    def filter_expense(self):
        category = input("Enter category : ").strip()
        amount = input("Enter minimum amount (or press Enter to skip): ").strip()
        date = input("Enter date (YYYY-MM-DD) (or press Enter to skip): ").strip()
        payment = input("Enter payment method (or press Enter to skip): ").strip()


        matches=[]
        
        for expense in self.expenses.values():
            if category and expense.category.lower() != category.lower():
                 continue
             
            
            if amount and expense.amount < float(amount):
                 continue
             
            if date and expense.date!= date:
                continue
            
            if payment and expense.payment.lower()!= payment.lower():
                continue
            
            
            
                
            matches.append(expense)
        
       

        if not matches:
            print("No matching expenses found.")
            return
            
        for expense in matches:
            print("\n--------------------")
            print("ID:", expense.id)
            print("Amount:", expense.amount)
            print("Category:", expense.category)
            print("Date:", expense.date)
            print("Description:", expense.description)
            print("Payment:", expense.payment)  
            
          
    def expense_summary(self):
        if not self.expenses:
            print("No expenses available.")
            return

        total = sum(expense.amount for expense in self.expenses.values())
        count = len(self.expenses)
        average = total / count

        highest = max(
        self.expenses.values(),
        key=lambda expense: expense.amount
        )

        lowest = min(
        self.expenses.values(),
        key=lambda expense: expense.amount
         )

        print("\n========== EXPENSE SUMMARY ==========")
        print("Total Expenses:", total)
        print("Number of Expenses:", count)
        print("Average Expense:", round(average, 2))

        print("\nHighest Expense:")
        print("ID:", highest.id)
        print("Amount:", highest.amount)
        print("Category:", highest.category)

        print("\nLowest Expense:")
        print("ID:", lowest.id)
        print("Amount:", lowest.amount)
        print("Category:", lowest.category)
        
    def save_expenses(self):
        data = {}

        for expense_id, expense in self.expenses.items():
            
        
            data[expense_id] = {
            "amount": expense.amount,
            "category": expense.category,
            "date": expense.date,
            "description": expense.description,
            "payment": expense.payment
        }

        with open("expenses.json", "w") as file:
            
            json.dump(data, file, indent=4)
            
    def load_expenses(self):
        try:
            with open("expenses.json","r") as file:
                data=json.load(file)
            
        
        
            for expense_id, expense_data in data.items():
                expense = Expense(
                int(expense_id),
                float(expense_data["amount"]),
                expense_data["category"],
                expense_data["date"],
                expense_data["description"],
                expense_data["payment"]
            )

            self.expenses[int(expense_id)] = expense
            
        except FileNotFoundError:
            pass
    
    def category_total(self):
        if not self.expenses:
            print("No expense found")
            return
        totals={}
        
        for expense in self.expenses.values():
            category=expense.category
            if category not in totals:
                totals[category] = 0

        totals[category] += expense.amount
        print("\n========== CATEGORY TOTALS ==========")

        for category, total in totals.items():
            print(category, ":", round(total, 2))
        
    def monthly_statistics(self):
            month = input("Enter month (YYYY-MM): ").strip()
            total = 0
            count = 0
            
            for expense in self.expenses.values():
                if expense.date.startswith(month):
                    total += expense.amount
                    count += 1

            if count == 0:
               print("No expenses found for this month.")
               return

            print("\n========== MONTHLY STATISTICS ==========")
            print("Month:", month)
            print("Total Spending:", round(total, 2))
            print("Number of Expenses:", count)
        
        
def validate_amount(amount):
    try:
        amount = float(amount)

        if amount <= 0:
            print("Amount must be greater than 0.")
            return False

        return True

    except ValueError:
        print("Amount must be a number.")
        return False


def validate_category(category):
    valid_categories = [
        "Food",
        "Transport",
        "Shopping",
        "Bills",
        "Entertainment",
        "Other"
    ]

    if category.strip().title() not in valid_categories:
        print("Invalid category.")
        return False

    return True


def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True

    except ValueError:
        print("Invalid date. Use YYYY-MM-DD format.")
        return False


def validate_description(description):
    if not description.strip():
        print("Description cannot be empty.")
        return False

    return True


def validate_payment(payment):
    valid_methods = [
        "Cash",
        "Card",
        "Bank Transfer",
        "Other"
    ]

    if payment.strip().title() not in valid_methods:
        print("Invalid payment method.")
        return False

    return True

def main():
    tracker=ExpenseTracker()
    
    while True:
        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Filter Expenses")
        print("6. Category Totals")
        print("7. Expense Summary")
        print("8. Monthly Statistics")
        print("9. Exit")
        
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            amount = input("Enter amount: ").strip()
            category = input("Enter category: ").strip()
            date = input("Enter date (YYYY-MM-DD): ").strip()
            description = input("Enter description: ").strip()
            payment = input("Enter payment method: ").strip()
            
            tracker.add_expense(
                amount,
                category,
                date,
                description,
                payment
            )

        elif choice=="2":
             tracker.view_expense()
                
        elif choice=="3":
             tracker.update_expense()
                
        elif  choice=="4":
            tracker.delete_expense()
            
        elif choice == "5":
            tracker.filter_expense()

        elif choice == "6":
            tracker.category_total()
        
        elif choice == "7":
            tracker.expense_summary()
        
        elif choice == "8":
            tracker.monthly_statistics()

        elif choice == "9":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__=="__main__":
    main()
