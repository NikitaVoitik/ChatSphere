from django.utils import timezone
import cuid

def generate_default_chat_data():
    content = [{
        "type": "text",
        "text": "You're a helpful assistant"
    }]
    messages = [{
        "id": cuid.cuid(),
        "role": "developer",
        "content": content,
        "timestamp": str(timezone.now())
    }]
    chat = {
        "messages": messages,
        "name": "New Chat"
    }
    return chat
