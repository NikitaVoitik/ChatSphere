from django.utils import timezone
import cuid

def generate_default_chat_data():
    content = [{
        "type": "text",
        "text": "You're a helpful assistant"
    }]
    message = [{
        "id": cuid.cuid(),
        "role": "developer",
        "content": content,
        "timestamp": str(timezone.now())
    }]
    chat = {
        "messages": message,
        "name": "New Chat"
    }
    return chat
