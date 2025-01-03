import json
import os
import uuid
import datetime

from Item import Item

class Order:
    ORDERS_FILE = 'Data/order.json'

    # -----------------------------------------------------------
    # constructor for the Order class
    # -----------------------------------------------------------
    def __init__(self, itemID, buyerID, paymentID, total_amount):
        self.orderID = str(uuid.uuid4())
        self.itemID = itemID
        self.buyerID = buyerID
        self.status = "pending"
        self.paymentID = paymentID
        self.total_amount = total_amount
        self.date = datetime.datetime.now().isoformat()
        self.save_order()

    # -----------------------------------------------------------
    # saves the order instance to the order.json file
    # -----------------------------------------------------------
    def save_order(self):
        order_data = {
            "orderID": self.orderID,
            "itemID": self.itemID,
            "buyerID": self.buyerID,
            "status": self.status,
            "paymentID": self.paymentID,
            "total_amount": self.total_amount,
            "date": self.date
        }
    #handle errors
        try:
            orders = self.load_data(self.ORDERS_FILE)
            orders = [order for order in orders if order['orderID'] != self.orderID]
            orders.append(order_data)
            self.write_data(self.ORDERS_FILE, orders)
            print("Order saved successfully")
        except Exception as e:
            print(f"Error in save_order: {e}")

    # -----------------------------------------------------------
    # changes the status of an order to cancelled
    # -----------------------------------------------------------
    def cancelOrder(self):
        try:
            if self.status not in ["created", "pending"]:
                raise Exception("Order cannot be cancelled.")
            self.status = "cancelled"
            self.save_order()
            print(f"Order {self.orderID} cancelled successfully.")
        except Exception as e:
            print(f"Failed to cancel order: {e}")

    # -----------------------------------------------------------
    # accepts the terms and conditions of an order, not implemented properly
    # -----------------------------------------------------------
    def acceptTermsAndConditions(self):
        try:
            print("Terms and conditions accepted.")
        except Exception as e:
            print(f"Failed to accept terms and conditions: {e}")

    # -----------------------------------------------------------
    # takes a sum of all the prices and returns the total amount
    # -----------------------------------------------------------
    def calculateTotal(self, item_prices):
        try:
            self.total_amount = sum(item_prices)
            self.save_order()
            print(f"Total amount for order {self.orderID} is {self.total_amount}.")
        except Exception as e:
            print(f"Failed to calculate total amount: {e}")
  
    # -----------------------------------------------------------
    # views the status of an order
    # -----------------------------------------------------------
    def viewOrderStatus(self):
        try:
            print(f"Order {self.orderID} status is {self.status}.")
            return self.status
        except Exception as e:
            print(f"Failed to view order status: {e}")

    @staticmethod
    def load_data(filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    @staticmethod
    def write_data(filepath, data):
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    # -----------------------------------------------------------
    # testing the Order class
    # -----------------------------------------------------------
    order = Order("item123", "5b36cad9-4573-4451-8d8f-59570c1d2047", "a538c5d8-d6c1-44c3-9266-8d8cf3b93dd8", 100)
    print(order.__dict__)
    order.calculateTotal([50, 50])
    order.viewOrderStatus()
    order.cancelOrder()
    order.viewOrderStatus()