from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumers(WebsocketConsumer):
    
    
    # room ---- jb do log aps me koi room bnate hai in short pubg room
    # group jb hme kabhi multiple logo ko kuch bhejna hota hai
    # ws://
    def connect(self):
        self.room_name = 'test_consumer'
        self.room_group_name = 'test_consumer_group'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, 
            self.channel_name
        )
        
        self.accept()
        self.send(text_data=json.dumps({'status':'connected'}))
    def recieve(self):
        pass
    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )