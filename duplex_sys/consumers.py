import json
import random

from channels.generic.websocket import WebsocketConsumer

from duplex_sys.process_to_sort import rearrange_array
from ws_imp_dj.settings import cipher_suite


class ArraySort(WebsocketConsumer):

    def connect(self):
        self.scope["session"]["seed"] = random.randint(1, 1000)
        self.accept()

    def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data = cipher_suite.decrypt(str.encode(text_data))
        text_data_json = json.loads(text_data)
        array = text_data_json['array']

        rearrange_array(array)
        result_string = json.dumps({
            'sorted_array': array
        })
        self.send(text_data=cipher_suite.encrypt(str.encode(result_string)).decode("utf-8"))
