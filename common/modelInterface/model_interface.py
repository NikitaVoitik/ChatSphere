from abc import ABC, abstractmethod


class ModelInterface(ABC):
    def __init__(self, chat_history: dict, api_key: str):
        self._chat_history: dict = chat_history
        self._api_key = api_key
        self._messages: list[dict] = self._chat_history.get('messages', [])
        if not self._messages:
            raise ValueError("The 'messages' field is missing or empty in the chat history.")

    def find_message(self, message_id: str) -> dict:
        for message in self._messages:
            if message.get('id') == message_id:
                return message

    def format(self):
        for message in self._messages:
            content = message.get('content')[0]
            type = content.get('type')
            if type == "text":
                self.format_text(message)
            elif type == "image_url":
                self.format_image(message)

    @abstractmethod
    def stream(self, model_name):
        pass

    @abstractmethod
    def format_text(self, message: dict):
        """
        Format a text message based on the model-specific requirements.
        """
        pass

    @abstractmethod
    def format_image(self, message: dict):
        """
        Format an image message based on the model-specific requirements.
        """
        pass
