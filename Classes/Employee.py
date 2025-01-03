import json
import os
from User import User
import uuid

class Employee(User):
    EMPLOYEE_FILE = 'Data/employee.json'
    ITEMS_FILE = 'Data/items.json'
    COMMENTS_FILE = 'Data/comment.json'
    TRANSACTIONS_FILE = 'Data/transactions.json'

    # -----------------------------------------------------------
    # costructor for the Employee class
    # -----------------------------------------------------------
    def __init__(self, firstName, lastName, email, password, employeeType='full-time'):
        self.employeeID = str(uuid.uuid4())
        self.employeeType = employeeType
        super().__init__(firstName, lastName, email, password)
        self.save_employee()

    # -----------------------------------------------------------
    # this method saves the employee instance to the employee.json file
    # -----------------------------------------------------------
    def save_employee(self):
        employee_data = {
            "employeeID": self.employeeID,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "employeeType": self.employeeType,
            "status": self.status
        }
    #handles the exception if any occurs while saving the employee data to the employee.json file
        try:
            employees = self.load_data(self.EMPLOYEE_FILE)
            employees = [employee for employee in employees if employee['employeeID'] != self.employeeID]
            employees.append(employee_data)
            self.write_data(self.EMPLOYEE_FILE, employees)
            print("Employee saved successfully")
        except Exception as e:
            print(f"Error in save_employee: {e}")
    # -----------------------------------------------------------
    # this method posts an item to the items.json file
    # -----------------------------------------------------------
    def postItem(self, item_data):
        try:
            items = self.load_data(self.ITEMS_FILE)
            items.append(item_data)
            self.write_data(self.ITEMS_FILE, items)
            print("Item posted successfully")
        except Exception as e:
            print(f"postItem error: {e}")

    # -----------------------------------------------------------
    # this method is for creating comments and writing it to the comment.json file
    # -----------------------------------------------------------
    def postComment(self, comment_data):
        try:
            comments = self.load_data(self.COMMENTS_FILE)
            comments.append(comment_data)
            self.write_data(self.COMMENTS_FILE, comments)
            print("Comment posted successfully")
        except Exception as e:
            print(f"postComment error: {e}")

    # -----------------------------------------------------------
    # reads the transactions.json file and returns the transactions of the user
    # -----------------------------------------------------------
    def viewTransactions(self):
        try:
            transactions = self.load_data(self.TRANSACTIONS_FILE)
            user_transactions = [transaction for transaction in transactions if transaction['userID'] == self.userID]
            print("Transactions viewed successfully:", user_transactions)
            return user_transactions
        except Exception as e:
            print(f"viewTransactions error: {e}")

    # -----------------------------------------------------------
    # reads the employee.json file and returns the employee details
    # -----------------------------------------------------------
    def viewProfile(self):
        try:
            employees = self.load_data(self.EMPLOYEE_FILE)
            employee = next((emp for emp in employees if emp['employeeID'] == self.employeeID), None)
            print("Profile viewed successfully:", employee)
            return employee
        except Exception as e:
            print(f"viewProfile error: {e}")

    # -----------------------------------------------------------
    # loads data from a json file
    # -----------------------------------------------------------
    @staticmethod
    def load_data(filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    # -----------------------------------------------------------
    # writes data to a json file
    # -----------------------------------------------------------
    @staticmethod
    def write_data(filepath, data):
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    # -----------------------------------------------------------
    # testing the Employee class
    # -----------------------------------------------------------
    employee = Employee("zimUche", "benjamin", "benjamin.zim@gmail.com", "password", "full-time")
    print(employee.__dict__)
    employee.postItem({"itemID": "item123", "name": "Laptop", "price": 1000, "userID": "f3a3906f-dc45-4b1b-844c-4c2a558f8ebd"})
    employee.postComment({"commentID": "comment123", "content": "Great product!", "userID": "f3a3906f-dc45-4b1b-844c-4c2a558f8ebd"})
    employee.viewTransactions()
    employee.viewProfile()