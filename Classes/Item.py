import json
import os
import uuid

class Item:
    ITEMS_FILE = 'Data/items.json'

    # -----------------------------------------------------------
    # constructor for this class 
    # -----------------------------------------------------------
    def __init__(self, sellerID, itemName, itemDescription, itemPrice,  itemCategory, itemMediaUrl='', itemMediaId=''):
        self.itemID = str(uuid.uuid4())
        self.sellerID = sellerID
        self.itemName = itemName
        self.itemDescription = itemDescription
        self.commentCount = 0
        self.itemPrice = itemPrice
        self.itemMediaId = itemMediaId
        self.itemCategory = itemCategory
        self.itemMediaUrl = itemMediaUrl
        self.save_item()

    # -----------------------------------------------------------
    # saves the item instance to the items.json file
    # -----------------------------------------------------------
    def save_item(self):
        item_data = {
            "itemID": self.itemID,
            "sellerID": self.sellerID,
            "itemName": self.itemName,
            "itemDescription": self.itemDescription,
            "commentCount": self.commentCount,
            "itemPrice": self.itemPrice,
            "itemMediaId": self.itemMediaId,
            "itemCategory": self.itemCategory,
            "itemMediaUrl": self.itemMediaUrl
        }
    #handles the exception if any occurs while saving the item data to the items.json file
        try:
            items = []
            if os.path.exists(self.ITEMS_FILE):
                with open(self.ITEMS_FILE, 'r') as file:
                    items = json.load(file)
                
                # Remove existing item data if it exists
                items = [item for item in items if item['itemID'] != self.itemID]
            
            items.append(item_data)
            with open(self.ITEMS_FILE, 'w') as file:
                json.dump(items, file, indent=4)
            print("Item saved successfully")
        except Exception as e:
            print(f"Error in save_item: {e}")

    
    # -----------------------------------------------------------
    # edits the Item and saves it to the items.json file
    # -----------------------------------------------------------
    def editItem(self, itemName=None, itemDescription=None, itemPrice=None, itemMediaId=None, itemCategory=None, itemMediaUrl=None):
        try:
            if itemName is not None:
                self.itemName = itemName
            if itemDescription is not None:
                self.itemDescription = itemDescription
            if itemPrice is not None:
                self.itemPrice = itemPrice
            if itemMediaId is not None:
                self.itemMediaId = itemMediaId
            if itemCategory is not None:
                self.itemCategory = itemCategory
            if itemMediaUrl is not None:
                self.itemMediaUrl = itemMediaUrl
            self.save_item()
            print("Item edited successfully")
        except Exception as e:
            print(f"editItem error: {e}")

    # -----------------------------------------------------------
    # deletes the item from the items.json file
    # -----------------------------------------------------------
    def deleteItem(self, itemID):
        try:
            if os.path.exists(self.ITEMS_FILE):
                with open(self.ITEMS_FILE, 'r') as file:
                    items = json.load(file)
                
                # Remove the item from the list
                items = [item for item in items if item['itemID'] != itemID]
                
                with open(self.ITEMS_FILE, 'w') as file:
                    json.dump(items, file, indent=4)
            print("Item deleted successfully")
        except Exception as e:
            print(f"deleteItem error: {e}")

    # -----------------------------------------------------------
    # views the item instance from the items.json file
    # -----------------------------------------------------------
    
    def viewItem(self, itemID):
        try:
            if os.path.exists(self.ITEMS_FILE):
                with open(self.ITEMS_FILE, 'r') as file:
                    items = json.load(file)
                item = next((item for item in items if item['itemID'] == itemID), None)
                print("Item viewed successfully:", item)
                return item
        except Exception as e:
            print(f"viewItem error: {e}")

if __name__ == "__main__":
    # -----------------------------------------------------------
    # testing the Item class
    # -----------------------------------------------------------
    item = Item("seller123", "Laptop", "A high-end gaming laptop", 1500, "media123", "Electronics", "http://example.com/media123")
    print(item.__dict__)
    item.editItem(itemName="Gaming Laptop", itemPrice=1400)
    item.viewItem("681f7c0e-9ee8-4dfe-9a9e-3cb2a6da9ddb")
