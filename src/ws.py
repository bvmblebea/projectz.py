# Author: github.com/Zakovskiy
import websocket
import ujson


class WebSocket:

    def __init__(self, client) -> None:
        self.client = client
        self.ws = websocket.WebSocket()
        self._ping_message = None

    def connect(self) -> None:
        self.client.generate_signature("/v1/chat/ws", {})
        self.ws.connect("wss://ws.projz.com/v1/chat/ws", header=self.client.headers)

    def send(self, *args, **kwargs) -> None:
        self.ws.send(*args, **kwargs)

    def ping_cycle(self) -> None:
        self.send(self._ping_message)

    def listen(self) -> None:
        self.ping_cycle()
        message = self.ws.recv()
        return message

    def send_json(self, entity: dict) -> dict:
        self.send(ujson.dumps(entity))
