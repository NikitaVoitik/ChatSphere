import json

from channels.consumer import AsyncConsumer

class ChatConsumer(AsyncConsumer):
    def connect(self):
        self.chat_id = self.scope['path'].split("/")[3]

        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))