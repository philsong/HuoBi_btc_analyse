"""
A socket_IO client
"""
from time import sleep
from socketIO_client import SocketIO
import json

requestIndex = '1404103038520'

strMsg = {"symbolList":{"lastTimeLine":[{"symbolId":"btccny","pushType":"pushLong"}]},"version":1,"msgType":"reqMsgSubscribe","requestIndex":requestIndex}
                        #"lastKLine":[{"symbolId":"btccny","pushType":"pushLong","period":"1min"},{"symbolId":"btccny","pushType":"pushLong","period":"5min"},{"symbolId":"btccny","pushType":"pushLong","period":"15min"},{"symbolId":"btccny","pushType":"pushLong","period":"30min"},{"symbolId":"btccny","pushType":"pushLong","period":"60min"},{"symbolId":"btccny","pushType":"pushLong","period":"1day"},{"symbolId":"btccny","pushType":"pushLong","period":"1week"},{"symbolId":"btccny","pushType":"pushLong","period":"1mon"},{"symbolId":"btccny","pushType":"pushLong","period":"1year"}],"marketDepthDiff":[{"symbolId":"btccny","pushType":"pushLong","percent":"10"},{"symbolId":"btccny","pushType":"pushLong","percent":"20"},{"symbolId":"btccny","pushType":"pushLong","percent":"50"},{"symbolId":"btccny","pushType":"pushLong","percent":"80"},{"symbolId":"btccny","pushType":"pushLong","percent":"100"}],"marketDepthTopDiff":[{"symbolId":"btccny","pushType":"pushLong"}],"marketDetail":[{"symbolId":"btccny","pushType":"pushLong"}],"tradeDetail":[{"symbolId":"btccny","pushType":"pushLong"}],"marketOverview":[{"symbolId":"btccny","pushType":"pushLong"}]},

g_isConnect = 0
options = {'force new connection':True,'reconnection':True}

def on_connect():
    g_isConnect = 1
    socket.emit('request',strMsg)
    print('websocket connect')

def on_disconnect():
    g_isConnect = 2
    print('ws disconnect')

def on_reconnect():
    g_isConnect = 1
    print('reconnect')

def on_message(data):
    #requestIndex = data[0]['_id']
    #print(requestIndex)
    print(data)

def on_request(data):
    #print(data)
    pass


socket = SocketIO('hq.huobi.com',80)
socket.on('connect',on_connect)
socket.on('disconnect',on_disconnect)
socket.on('reconnect',on_reconnect)
socket.on('message',on_message)
socket.on('request',on_request)

while True:
    sleep(1.5)
    #print('requestIndex:{0}'.format(strMsg['requestIndex']))
    try:
        strMsg['requestIndex'] = requestIndex
        socket.emit('request',strMsg)
        socket.wait(1)
    except Exception,e:
        print(e)
