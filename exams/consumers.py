import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MinimalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Define a group name that will include all connected clients.
        self.group_name = "group_chat"

        # Add this WebSocket connection to the group.
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # Accept the connection.
        await self.accept()

    async def disconnect(self, close_code):
        # Remove this WebSocket connection from the group.
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Parse the received JSON data.
        data = json.loads(text_data)
        message = data.get("message", "")
        username = data.get("username", "Anonymous")

        # Broadcast the message to all group members.
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_message",  # This tells Channels to call the method named `chat_message`.
                "message": message,
                "username": username,
            }
        )

    async def chat_message(self, event):
        # This method is called when a message is sent to the group.
        message = event["message"]
        username = event["username"]

        # Send the message to the WebSocket client.
        await self.send(text_data=json.dumps({
            "message": message,
            "username": username,
        }))
