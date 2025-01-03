import json
import os
import requests

class Media:
    MEDIA_FILE = 'Data/media.json'
    MEDIA_DIR = 'Data/media_files/'

    # -----------------------------------------------------------
    # the constructor for the Media class
    # -----------------------------------------------------------
    def __init__(self, mediaID, url, mediaType="photo"):
        self.mediaID = mediaID
        self.mediaType = mediaType
        self.url = url
        self.local_path = os.path.join(self.MEDIA_DIR, f"{self.mediaID}.{self.mediaType}")
        self.save_media()
        self.download_media()

    # -----------------------------------------------------------
    # saves the media instance to the media.json file
    # -----------------------------------------------------------
    def save_media(self):
        media_data = {
            "mediaID": self.mediaID,
            "mediaType": self.mediaType,
            "url": self.url,
            "local_path": self.local_path
        }

        try:
            media_list = []
            if os.path.exists(self.MEDIA_FILE):
                with open(self.MEDIA_FILE, 'r') as file:
                    media_list = json.load(file)
                
                # Remove existing media data if it exists
                media_list = [media for media in media_list if media['mediaID'] != self.mediaID]
            
            media_list.append(media_data)
            with open(self.MEDIA_FILE, 'w') as file:
                json.dump(media_list, file, indent=4)
            print("Media saved successfully")
        except Exception as e:
            print(f"Error in save_media: {e}")

    # -----------------------------------------------------------
    # tried to implement the download_media method, it doesnt work
    # -----------------------------------------------------------
    def download_media(self):
        try:
            if not os.path.exists(self.MEDIA_DIR):
                os.makedirs(self.MEDIA_DIR)
            response = requests.get(self.url)
            response.raise_for_status()
            with open(self.local_path, 'wb') as file:
                file.write(response.content)
            print(f"Media downloaded successfully to {self.local_path}")
        except Exception as e:
            print(f"Error in download_media: {e}")

    # -----------------------------------------------------------
    # reads the media file and returns the media details
    # -----------------------------------------------------------
    def deleteMedia(self):
        try:
            if os.path.exists(self.MEDIA_FILE):
                with open(self.MEDIA_FILE, 'r') as file:
                    media_list = json.load(file)
                
                # Remove the media from the list
                media_list = [media for media in media_list if media['mediaID'] != self.mediaID]
                
                with open(self.MEDIA_FILE, 'w') as file:
                    json.dump(media_list, file, indent=4)
            
            if os.path.exists(self.local_path):
                os.remove(self.local_path)
                print(f"Local file {self.local_path} deleted successfully")
            
            print(f"Media with ID: {self.mediaID} deleted successfully")
        except Exception as e:
            print(f"Error in deleteMedia: {e}")

    # -----------------------------------------------------------
    # uploads the media to the server, it doesnt work
    # -----------------------------------------------------------
    def uploadMedia(self):
        try:
            self.save_media()
            self.download_media()
            print(f"Media with ID: {self.mediaID} and URL: {self.url} uploaded successfully")
        except Exception as e:
            print(f"Error in uploadMedia: {e}")

if __name__ == "__main__":
    # Create a new media and test all the methods
    print("implementing this class completely requires a third party media server for uploading images and videos")