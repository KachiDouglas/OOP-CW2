import sys
import os

# -----------------------------------------------------------
# Add the directory containing the Classes folder to the Python path
# -----------------------------------------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Classes')))

from Admin import Admin
from Employee import Employee
from Item import Item
from Order import Order
from Payment import Payment
from Comment import Comment
from Notification import Notification
from Refund_request import RefundRequest
from User import User

def main():
    print("Welcome to Employee forum system for second hand selling")
    print("What would you like to do?")
    print("1. Create a new Admin")
    print("2. Create a new Employee")
    print("3. Edit profile")
    print("4. Post a new item")
    print("5. Post a new comment")
    print("6. Make an order")
    print("7. Make a payment")
    print("8. View transactions")
    print("9. View an item")

    choice = input("Enter the number of the action you would like to perform: ")

    if choice == "1":
        create_admin()
    elif choice == "2":
        create_employee()
    elif choice == "3":
        print("this feature is not available yet")
    elif choice == "4":
        post_item()
    elif choice == "5":
        post_comment()
    elif choice == "6":
        make_order()
    elif choice == "7":
        make_payment()
    elif choice == "8":
        view_transactions()
    elif choice == "9":
        view_item()
    else:
        print("Invalid choice")

def create_admin():
    try:
        firstName = input("Enter admin first name: ")
        lastName = input("Enter admin last name: ")
        email = input("Enter admin email: ")
        password = input("Enter admin password: ")
        admin = Admin(firstName, lastName, email, password)
        print(f"Admin {firstName} created successfully!")
    except Exception as e:
        print(f"An error occurred while creating admin: {e}")

def create_employee():
    try:
        firstName = input("Enter employee first name: ")
        lastName = input("Enter employee last name: ")
        email = input("Enter employee email: ")
        password = input("Enter employee password: ")
        employee = Employee(firstName, lastName, email, password)
        print(f"Employee {firstName} created successfully!")
    except Exception as e:
        print(f"An error occurred while creating employee: {e}")

def post_item():
    try:
        sellerID = input("Enter your user ID (grab an id from the Data/user.json file): ")
        itemName = input("Enter item name: ")
        itemDescription = input("Enter item description: ")
        itemPrice = float(input("Enter item price: "))
        itemCategory = input("Enter a category this item will belong: ")
        item = Item(sellerID, itemName, itemDescription, itemPrice, itemCategory)
        print("Item posted successfully!")
    except Exception as e:
        print(f"An error occurred while posting item: {e}")

def post_comment():
    try:
        ownerID = input("Enter your user ID: ")
        message = input("Enter comment message: ")
        itemID = input("Enter item ID: ")
        comment = Comment(ownerID, message, itemID)
        print("Comment posted successfully!")
    except Exception as e:
        print(f"An error occurred while posting comment: {e}")

def make_payment():
    try:
        print("This feature is not available yet")
    except Exception as e:
        print(f"An error occurred while making payment: {e}")

def make_order():
    try:
        itemID = input("Enter item ID: ")
        buyerID = input("Enter buyer ID: ")
        paymentID = input("Enter payment ID: ")
        total_amount = float(input("Enter total amount: "))
        order = Order(itemID, buyerID, paymentID, total_amount)
        print("Order made successfully!")

    except Exception as e:
        print(f"An error occurred while making order: {e}")


def view_transactions():
    try:
        transactions = Order.load_data('Data\order.json')
        for transaction in transactions:
            print(transaction)
    except Exception as e:
        print(f"An error occurred while viewing transactions: {e}")
        

def view_item():
    try:
        theItemID = input("Enter item ID: ")
        items = Order.load_data('Data\items.json')
        for item in items:
            if item['itemID'] == theItemID:
                print(item)
    except Exception as e:
        print(f"An error occurred while viewing item: {e}")

if __name__ == "__main__":
    main()