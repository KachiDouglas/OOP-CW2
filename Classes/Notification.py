import json
import os
import uuid
import datetime
from User import User
from Observer import Subject

class Notification(Subject):
    NOTIFICATIONS_FILE = 'Data/notifications.json'

    
    # -----------------------------------------------------------
    # constructor method for this class
    # -----------------------------------------------------------
    def __init__(self, notificationMessage, senderID, receiverID):
        super().__init__()
        self.notificationID = str(uuid.uuid4())
        self.notificationMessage = notificationMessage
        self.notificationDate = datetime.datetime.now().isoformat()
        self.senderID = senderID
        self.receiverID = receiverID
        self.status = "unread"
        self.saveNotification()

    def saveNotification(self):
        notification_data = {
            "notificationID": self.notificationID,
            "notificationMessage": self.notificationMessage,
            "notificationDate": self.notificationDate,
            "senderID": self.senderID,
            "receiverID": self.receiverID,
            "status": self.status
        }

        try:
            notifications = self.loadData(self.NOTIFICATIONS_FILE)
            notifications = [notification for notification in notifications if notification['notificationID'] != self.notificationID]
            notifications.append(notification_data)
            self.writeData(self.NOTIFICATIONS_FILE, notifications)
            self.notify(notification_data)
            print("Notification saved successfully")
        except Exception as e:
            print(f"Error in saveNotification: {e}")

    
    # -----------------------------------------------------------
    #  Attaches an observer
    # -----------------------------------------------------------    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    # -----------------------------------------------------------
    #  Removes an observer
    # ----------------------------------------------------------- 
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    # -----------------------------------------------------------
    #  Notifies all observers
    # -----------------------------------------------------------
    def notify(self, notification):
        for observer in self._observers:
            observer.update(notification)

    # -----------------------------------------------------------
    #  used to call the notify method for many observers
    # ----------------------------------------------------------- 
    def sendNotification(self):
        try:
            self.notify(f"Notification {self.notificationID}: {self.notificationMessage}")
            self.saveNotification()
            print(f"Notification sent to {self.receiverID} successfully")
        except Exception as e:
            print(f"sendNotification error: {e}")

    # -----------------------------------------------------------
    #  reads the notification from the notifications.json file
    # ----------------------------------------------------------- 
    def viewNotification(self):
        try:
            notifications = self.loadData(self.NOTIFICATIONS_FILE)
            notification = next((notif for notif in notifications if notif['notificationID'] == self.notificationID), None)
            print("Notification viewed successfully:", notification)
            return notification
        except Exception as e:
            print(f"viewNotification error: {e}")

    # -----------------------------------------------------------
    #  edits a notification to mark it as read'
    # ----------------------------------------------------------- 
    def markAsRead(self):
        try:
            notifications = self.loadData(self.NOTIFICATIONS_FILE)
            for notification in notifications:
                if notification['notificationID'] == self.notificationID:
                    notification['status'] = "read"
            self.writeData(self.NOTIFICATIONS_FILE, notifications)
            print("Notification marked as read successfully")
        except Exception as e:
            print(f"markAsRead error: {e}")

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
    user = User("kachi", "Afudoh", "afudohkachi@gmail.com", "password")
    notification = Notification("This is a notification", "sender123", user.userID)
    notification.attach(user)
    print(notification.__dict__)
    notification.sendNotification()
    notification.viewNotification()
    notification.markAsRead()