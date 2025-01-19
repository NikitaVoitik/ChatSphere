import json
from openai import AsyncOpenAI

from model_interface import ModelInterface


class OpenAIInterface(ModelInterface):
    def __init__(self, chat_history, api_key):
        super().__init__(chat_history, api_key)
        self._client = AsyncOpenAI(api_key=self._api_key)

    async def stream(self, model_name):
        self.format()
        thread = await self._client.beta.threads.create()

        for message in self._messages:
            await self._client.beta.threads.messages.create(
                thread_id=thread.id,
                role=message.get('role', 'user'),
                content=message['content']
            )


    def format_text(self, message: dict):
        pass

    def format_image(self, message: dict):
        content = message.get('content')[0]
        content['image_url'] = {
            'url': content['image_url']
        }


file = 0
with open('../../chat.work.json', 'r+') as f:
    file = f.read()
# print(json.loads(file))
# client.chat_completions(file)
# print(client.openAI.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "developer", "content": "You are a helpful assistant."},
#         {
#             "role": "developer",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "You're a really good assistant."
#                 }
#             ]
#         }
#     ]
# ))

# print(client.openAI.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "developer", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "What's on the pictures?"
#                 },
#
#             ],
#         },
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": "data:image/jpeg;base64,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"
#                     }
#                 }
#             ]
#         },
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg"
#                     }
#                 }
#             ]
#         },
#
#     ]
# ))
