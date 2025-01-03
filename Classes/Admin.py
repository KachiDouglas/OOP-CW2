import json
import os
import uuid
from User import User

class Admin(User):
    ADMIN_FILE = 'Data/admin.json'
    EMPLOYEE_FILE = 'Data/employee.json'
    REFUND_FILE = 'Data/refund.json'
    TRANSACTION_FILE = 'Data/transactions.json'

    # -----------------------------------------------------------
    # constructor for the Admin class
    # -----------------------------------------------------------
    def __init__(self, firstName, lastName, email, password, employeeCount=0):
        super().__init__(firstName, lastName, email, password)
        self.employeeCount = employeeCount
        self.adminID = self.userID  
        self.save_admin()

    # -----------------------------------------------------------
    # saves the admin instance to the admin.json file
    # -----------------------------------------------------------
    def save_admin(self):
        admin_data = {
            "adminID": self.adminID,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "employeeCount": self.employeeCount
        }

        try:
            admins = self.load_data(self.ADMIN_FILE)
            admins = [admin for admin in admins if admin['adminID'] != self.adminID]
            admins.append(admin_data)
            self.write_data(self.ADMIN_FILE, admins)
            print("Admin saved successfully")
        except Exception as e:
            print(f"Error in save_admin: {e}")

    # -----------------------------------------------------------
    # changes the status of an employee to inactive
    # -----------------------------------------------------------
    def deactivateEmployee(self, employeeID):
        try:
            employees = self.load_data(self.EMPLOYEE_FILE)
            for employee in employees:
                if employee['employeeID'] == employeeID:
                    employee['status'] = 'inactive'
            self.write_data(self.EMPLOYEE_FILE, employees)
            print("Employee deactivated successfully")
        except Exception as e:
            print(f"deactivateEmployee error: {e}")

    # -----------------------------------------------------------
    # changes the status of an employee to active
    # -----------------------------------------------------------
    def reactivateEmployee(self, employeeID):
        try:
            employees = self.load_data(self.EMPLOYEE_FILE)
            for employee in employees:
                if employee['employeeID'] == employeeID:
                    employee['status'] = 'active'
            self.write_data(self.EMPLOYEE_FILE, employees)
            print("Employee reactivated successfully")
        except Exception as e:
            print(f"reactivateEmployee error: {e}")
            
    # -----------------------------------------------------------
    # reads the refund.json file and returns the refund requests
    # -----------------------------------------------------------
    def viewRefundRequest(self):
        try:
            refunds = self.load_data(self.REFUND_FILE)
            print("Refund requests:", refunds)
            return refunds
        except Exception as e:
            print(f"viewRefundRequest error: {e}")

    # -----------------------------------------------------------
    # reads the employee.json file and returns the employee details
    # -----------------------------------------------------------
    def viewEmployee(self, employeeID):
        try:
            employees = self.load_data(self.EMPLOYEE_FILE)
            employee = next((emp for emp in employees if emp['employeeID'] == employeeID), None)
            print("Employee details:", employee)
            return employee
        except Exception as e:
            print(f"viewEmployee error: {e}")

    # -----------------------------------------------------------
    # views the refund request and changes the status to approved
    # -----------------------------------------------------------
    def approveRefundRequest(self, refundID):
        try:
            refunds = self.load_data(self.REFUND_FILE)
            for refund in refunds:
                if refund['refundID'] == refundID:
                    refund['status'] = 'approved'
            self.write_data(self.REFUND_FILE, refunds)
            print("Refund request approved successfully")
        except Exception as e:
            print(f"approveRefundRequest error: {e}")

    # -----------------------------------------------------------
    # views the refund request and changes the status to rejected
    # -----------------------------------------------------------
    def rejectRefundRequest(self, refundID):
        try:
            refunds = self.load_data(self.REFUND_FILE)
            for refund in refunds:
                if refund['refundID'] == refundID:
                    refund['status'] = 'rejected'
            self.write_data(self.REFUND_FILE, refunds)
            print("Refund request rejected successfully")
        except Exception as e:
            print(f"rejectRefundRequest error: {e}")

    # -----------------------------------------------------------
    # appends a new transaction to the transactions.json file
    # -----------------------------------------------------------
    def registerTransaction(self, transaction_data):
        try:
            transactions = self.load_data(self.TRANSACTION_FILE)
            transactions.append(transaction_data)
            self.write_data(self.TRANSACTION_FILE, transactions)
            print("Transaction registered successfully")
        except Exception as e:
            print(f"registerTransaction error: {e}")

    # -----------------------------------------------------------
    # reads the transactions file and returns the transaction details
    # -----------------------------------------------------------
    def viewTransaction(self, transactionID):
        try:
            transactions = self.load_data(self.TRANSACTION_FILE)
            transaction = next((trans for trans in transactions if trans['transactionID'] == transactionID), None)
            print("Transaction details:", transaction)
            return transaction
        except Exception as e:
            print(f"viewTransaction error: {e}")

    # -----------------------------------------------------------
    # loads the data from a json file
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
    # testing the Admin class
    # -----------------------------------------------------------
    admin = Admin("Admin", "Douglas", "adminDouglas@gmail.com", "password", employeeCount=10)
    print(admin.__dict__)
    admin.deactivateEmployee("5b36cad9-4573-4451-8d8f-59570c1d2047")
    admin.reactivateEmployee("5b36cad9-4573-4451-8d8f-59570c1d2047")
    admin.viewRefundRequest()
    admin.viewEmployee("7d6f4939-b361-4c9d-8043-6d7c2e58d67c")
    admin.registerTransaction({"transactionID": "some_transaction_id", "amount": 100, "status": "completed"})