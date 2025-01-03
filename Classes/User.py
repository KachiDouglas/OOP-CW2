import json
import os
import uuid
from Observer import Observer

class User(Observer):
    USER_FILE = 'Data/user.json'
    SESSION_FILE = 'Data/session.json'
    NOTIFICATIONS_FILE = 'Data/notifications.json'
    ITEMS_FILE = 'Data/items.json'
    TRANSACTIONS_FILE = 'Data/transactions.json'

    # -----------------------------------------------------------
    # the constructor for the User class
    # -----------------------------------------------------------
    def __init__(self, firstName, lastName, email, password):
        super().__init__()
        self.userID = self.createId()
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.notifications = []
        self.status = "active"
        self.saveUser()

    # -----------------------------------------------------------
    # returns a unique ID for the userID
    # -----------------------------------------------------------
    @staticmethod
    def createId():
        return str(uuid.uuid4())

    # -----------------------------------------------------------
    # saves the user instance to the user.json file
    # -----------------------------------------------------------
    def saveUser(self):
        user_data = {
            "userID": self.userID,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "notifications": self.notifications,
            "status": self.status
        }
    # handling errors during saving
        try:
            users = self.loadData(self.USER_FILE)
            users = [user for user in users if user['userID'] != self.userID]
            users.append(user_data)
            self.writeData(self.USER_FILE, users)
            print("User saved successfully")
        except Exception as e:
            print(f"Error in saveUser: {e}")

    # -----------------------------------------------------------
    # checks if a users record exists in the user.json file and gives them a session
    # -----------------------------------------------------------
    def login(self, email, password):
        try:
            users = self.loadData(self.USER_FILE)
            for user in users:
                if user['email'] == email and user['password'] == password:
                    self.writeData(self.SESSION_FILE, {"userID": user['userID']})
                    print("Login successful")
                    return True
            print("Login failed")
            return False
        except Exception as e:
            print(f"Error in login: {e}")

    # -----------------------------------------------------------
    # deletes the session
    # -----------------------------------------------------------
    def logout(self):
        try:
            if os.path.exists(self.SESSION_FILE):
                os.remove(self.SESSION_FILE)
                print("Logout successful")
        except Exception as e:
            print(f"Error in logout: {e}")

    # -----------------------------------------------------------
    # edit the user profile from the user.json file
    # -----------------------------------------------------------
    def editProfile(self, firstName=None, lastName=None, email=None, password=None):
        try:
            users = self.loadData(self.USER_FILE)
            for user in users:
                if user['userID'] == self.userID:
                    if firstName:
                        user['firstName'] = firstName
                    if lastName:
                        user['lastName'] = lastName
                    if email:
                        user['email'] = email
                    if password:
                        user['password'] = password
            self.writeData(self.USER_FILE, users)
            print("Profile edited successfully")
        except Exception as e:
            print(f"Error in editProfile: {e}")

    # -----------------------------------------------------------
    # the update method for the Observer class
    # -----------------------------------------------------------
    def update(self, notification):
        self.notifications.append(notification)
        self.saveUser()
        print(f"User {self.email} received notification: {notification}")

    # -----------------------------------------------------------
    # the getState method for the Observer class, it returns the notifications
    # -----------------------------------------------------------
    def getState(self):
        return self.notifications

    # -----------------------------------------------------------
    # reads the notifications from the notifications.json file
    # -----------------------------------------------------------
    def viewNotifications(self):
        try:
            notifications = self.loadData(self.NOTIFICATIONS_FILE)
            user_notifications = [notif for notif in notifications if notif['receiverID'] == self.userID]
            return user_notifications
        except Exception as e:
            print(f"Error in viewNotifications: {e}")

    # -----------------------------------------------------------
    # reads the items from the items.json file
    # -----------------------------------------------------------
    def viewPostedItems(self):
        try:
            items = self.loadData(self.ITEMS_FILE)
            user_items = [item for item in items if item['userID'] == self.userID]
            return user_items
        except Exception as e:
            print(f"Error in viewPostedItems: {e}")

    def filterItemsByPrice(self, lowPriceRange, upperPriceRange):
        try:
            items = self.loadData(self.ITEMS_FILE)
            filtered_items = [item for item in items if lowPriceRange <= item['price'] <= upperPriceRange]
            return filtered_items
        except Exception as e:
            print(f"Error in filterItemsByPrice: {e}")

    def filterByCategory(self, categories):
        try:
            items = self.loadData(self.ITEMS_FILE)
            filtered_items = [item for item in items if item['category'] in categories]
            return filtered_items
        except Exception as e:
            print(f"Error in filterByCategory: {e}")

    def viewTransactions(self):
        try:
            transactions = self.loadData(self.TRANSACTIONS_FILE)
            user_transactions = [transaction for transaction in transactions if transaction['userID'] == self.userID]
            return user_transactions
        except Exception as e:
            print(f"Error in viewTransactions: {e}")

    # -----------------------------------------------------------
    # utility method to load and write data to a json file
    # -----------------------------------------------------------
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
    user = User("radi", "Afudoh", "radi@gmail.com", "password")
    print(user.__dict__)
    user.login("radi@gmail.com", "password")