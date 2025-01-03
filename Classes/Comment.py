import json
import os
import datetime
import uuid

class Comment:
    COMMENTS_FILE = 'Data/comment.json'

    # -----------------------------------------------------------
    # the constructor for the Comment class
    # -----------------------------------------------------------
    def __init__(self, ownerID, message, itemID):
        self.commentID = str(uuid.uuid4())
        self.ownerID = ownerID
        self.message = message
        self.itemID = itemID
        self.timestamp = datetime.datetime.now().isoformat()
        self.save_comment()

    # -----------------------------------------------------------
    # saves the comment instance to the comment.json file
    # -----------------------------------------------------------
    def save_comment(self):
        comment_data = {
            "commentID": self.commentID,
            "ownerID": self.ownerID,
            "message": self.message,
            "itemID": self.itemID,
            "timestamp": self.timestamp
        }

        try:
            comments = self.load_data(self.COMMENTS_FILE)
            comments = [comment for comment in comments if comment['commentID'] != self.commentID]
            comments.append(comment_data)
            self.write_data(self.COMMENTS_FILE, comments)
            print("Comment saved successfully")
        except Exception as e:
            print(f"Error in save_comment: {e}")

    # -----------------------------------------------------------
    # this creates a new comment
    # -----------------------------------------------------------
    @staticmethod
    def addComment(ownerID, message, itemID):
        try:
            return Comment(ownerID, message, itemID)
        except Exception as e:
            print(f"Error adding comment: {e}")

    # -----------------------------------------------------------
    # this method edits a comment with new message
    # -----------------------------------------------------------
    def editComment(self, new_message):
        try:
            self.message = new_message
            self.timestamp = datetime.datetime.now().isoformat()
            self.save_comment()
            print("Comment edited successfully")
        except Exception as e:
            print(f"Error editing comment: {e}")

    # -----------------------------------------------------------
    # this method deletes a comment
    # -----------------------------------------------------------
    def deleteComment(self):
        try:
            comments = self.load_data(self.COMMENTS_FILE)
            comments = [comment for comment in comments if comment['commentID'] != self.commentID]
            self.write_data(self.COMMENTS_FILE, comments)
            print("Comment deleted successfully")
        except Exception as e:
            print(f"Error deleting comment: {e}")

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
    # test the comment
    # -----------------------------------------------------------
    comment = Comment("9746ac83-9084-44ac-8fa9-c1ab48a279e6", "my new towel is nice i want it", "item123")
    print(comment.__dict__)
    comment.editComment("This is an edited comment")