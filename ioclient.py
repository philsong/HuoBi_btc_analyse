"""
A socket io client class
"""
from socketIO_client import SocketIO
from enum import Enum
import json

class HuobiWS(SocketIO):
    def __init__(self,host,port):
        # isConnected:
        # 0: initial not connected
        # 1: emit connect request
        # 2: disconnect
        self.isConnected = 0

    def on_connect(self):
        pass
    def on_connect(self):
        pass
    def on_connect(self):
        pass
    def on_connect(self):
        pass
