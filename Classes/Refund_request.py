import json
import os
import uuid
import datetime

class RefundRequest:
    REFUND_FILE = 'Data/refund.json'

    # -----------------------------------------------------------
    # constructor method for this class
    # -----------------------------------------------------------
    def __init__(self, orderID, reason, supportingDocuments=[]):
        self.refundRequestID = str(uuid.uuid4())
        self.orderID = orderID
        self.reason = reason
        self.supportingDocuments = supportingDocuments
        self.status = 'pending'
        self.date = datetime.datetime.now().isoformat()
        self.save_refund_request()

    # -----------------------------------------------------------
    # saves a refund request to the refund.json file upon instantiation of the class
    # -----------------------------------------------------------
    def save_refund_request(self):
        refund_data = {
            "refundRequestID": self.refundRequestID,
            "orderID": self.orderID,
            "reason": self.reason,
            "supportingDocuments": self.supportingDocuments,
            "status": self.status,
            "date": self.date
        }
        # handles exception if an error arise while saving 
        try:
            refunds = self.load_data(self.REFUND_FILE)
            refunds = [refund for refund in refunds if refund['refundRequestID'] != self.refundRequestID]
            refunds.append(refund_data)
            self.write_data(self.REFUND_FILE, refunds)
            print("Refund request saved successfully")
        except Exception as e:
            print(f"Error in save_refund_request: {e}")

    # -----------------------------------------------------------
    # changes the status of the refund request to submitted
    # -----------------------------------------------------------
    def submitRequest(self):
        try:
            if self.status != 'pending':
                raise ValueError("Refund request is not in pending status.")
            self.status = 'submitted'
            self.save_refund_request()
            print(f"Refund request {self.refundRequestID} submitted successfully.")
        except Exception as e:
            print(f"Error in submitRequest: {str(e)}")

    # -----------------------------------------------------------
    # changes the status of the refund request to approved
    # -----------------------------------------------------------
    def approveRequest(self):
        try:
            if self.status != 'submitted':
                raise ValueError("Refund request is not submitted yet.")
            self.status = 'approved'
            self.save_refund_request()
            print(f"Refund request {self.refundRequestID} approved.")
        except Exception as e:
            print(f"Error in approveRequest: {str(e)}")

    # -----------------------------------------------------------
    # changes the status of the refund request to rejected
    # -----------------------------------------------------------
    def rejectRequest(self):
        try:
            if self.status != 'submitted':
                raise ValueError("Refund request is not submitted yet.")
            self.status = 'rejected'
            self.save_refund_request()
            print(f"Refund request {self.refundRequestID} rejected.")
        except Exception as e:
            print(f"Error in rejectRequest: {str(e)}")

    # -----------------------------------------------------------
    # returns the status of the refund request
    # -----------------------------------------------------------
    def getStatus(self):
        try:
            return self.status
        except Exception as e:
            print(f"Error in getStatus: {str(e)}")

    # -----------------------------------------------------------
    # returns an array of supporting documents for the refund request
    # -----------------------------------------------------------
    def getSupportingDocuments(self):
        try:
            return self.supportingDocuments
        except Exception as e:
            print(f"Error in getSupportingDocuments: {str(e)}")
    
    # -----------------------------------------------------------
    # removes a supporting document from the refund request 
    # -----------------------------------------------------------
    def removeSupportingDoc(self, mediaID):
        try:
            self.supportingDocuments.remove(mediaID)
            self.save_refund_request()
            print(f"Document {mediaID} removed successfully.")
        except ValueError:
            print(f"Document {mediaID} not found in supporting documents.")
        except Exception as e:
            print(f"Error in removeSupportingDoc: {str(e)}")

    # -----------------------------------------------------------
    # accepts a valid status value and updates the status of the refund request
    # -----------------------------------------------------------
    def updateStatus(self, newStatus):
        try:
            if newStatus not in ['pending', 'submitted', 'approved', 'rejected']:
                raise ValueError("Invalid status value.")
            self.status = newStatus
            self.save_refund_request()
            print(f"Refund request {self.refundRequestID} status updated to {newStatus}.")
        except Exception as e:
            print(f"Error in updateStatus: {str(e)}")

    # -----------------------------------------------------------
    #  a static method to load refund.json file where the refund requests are stored
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
    #  a static method to write data to the refund.json file
    # -----------------------------------------------------------
    @staticmethod
    def write_data(filepath, data):
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    # -----------------------------------------------------------
    # testing the RefundRequest class
    # -----------------------------------------------------------
    refund_request = RefundRequest("order123", "Item not as described", ["doc1", "doc2"])
    print(refund_request.__dict__)
    refund_request.submitRequest()
    refund_request.approveRequest()
    refund_request.rejectRequest()
    print(refund_request.getStatus())
    print(refund_request.getSupportingDocuments())
    refund_request.updateStatus("approved")