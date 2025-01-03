import json
import os
import uuid
from Order import Order

class Payment:
    PAYMENT_FILE = 'Data/payment.json'

    def __init__(self, order):
        self.paymentID = str(uuid.uuid4())
        self.orderID = order.orderID
        self.itemID = order.itemID
        self.buyerID = order.buyerID
        self.sellerID = order.sellerID
        self.amount = order.amount
        self.status = 'Pending'
        self.savePayment()

    def savePayment(self):
        payment_data = {
            'paymentID': self.paymentID,
            'orderID': self.orderID,
            'itemID': self.itemID,
            'buyerID': self.buyerID,
            'sellerID': self.sellerID,
            'amount': self.amount,
            'status': self.status
        }

        try:
            payments = self.loadData(self.PAYMENT_FILE)
            payments = [payment for payment in payments if payment['paymentID'] != self.paymentID]
            payments.append(payment_data)
            self.writeData(self.PAYMENT_FILE, payments)
            print("Payment saved successfully")
        except Exception as e:
            print(f"Error in savePayment: {e}")

    def processPayment(self):
        try:
            # Simulate payment processing
            self.status = 'Completed'
            self.savePayment()
            print(f"Payment {self.paymentID} processed for Order {self.orderID}")
        except Exception as e:
            print(f"Error in processPayment: {e}")

    def viewPayment(self):
        try:
            payments = self.loadData(self.PAYMENT_FILE)
            payment = next((p for p in payments if p['paymentID'] == self.paymentID), None)
            if payment:
                print("Payment details:", payment)
                return payment
            else:
                print(f"Payment with ID {self.paymentID} not found")
                return None
        except Exception as e:
            print(f"Error in viewPayment: {e}")
            return None

    def updatePaymentStatus(self, newStatus):
        try:
            valid_statuses = ['Pending', 'Completed', 'Refunded', 'Failed']
            if newStatus not in valid_statuses:
                raise ValueError("Invalid status")
            self.status = newStatus
            self.savePayment()
            print(f"Payment {self.paymentID} status updated to {newStatus}")
        except Exception as e:
            print(f"Error in updatePaymentStatus: {e}")

    @staticmethod
    def loadData(filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    @staticmethod
    def writeData(filepath, data):
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    print("Payment Class implementation requires a payment gateway" )