'''
Basic autobahn server
'''
# create the namespace for the messages

from autobahn.twisted.websocket import WebSocketServerProtocol
from autobahn.twisted.websocket import WebSocketServerFactory

# most of this came from the code in the tutorial found 
# here: https://github.com/crossbario/autobahn-python
class earEEGServerProtocol(WebSocketServerProtocol):
    def onOpen(self):
        self.factory.connect_client(self)

    def onConnect(self, request):
        print "Client Connecting: {}".format(request.peer)

    def onOpen(self):
        print "WebSocket connection open"

    def onMessage(self, json, isBinary):
        print(json)
        self.factory.broadcast(json)

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.disconnect_client(self)


class earEEGServerFactory(WebSocketServerFactory):
    def __init__(self, url):
        super(earEEGServerFactory, self).__init__(url)
        self.client_list = []

    def connect_client(self, client):
        if client not in self.client_list:
            self.client_list.append(client)
            print "Connected to client {}".format(client.peer)

    def disconnect_client(self, client):
        if client in self.client_list:
            print "Disconnected from client {}".format(client.peer)
            self.client_list.remove(client)

    def broadcast(self, msg):
        print "Sending message: {}".format(msg)
        for client in self.client_list:
            client.sendMessage(msg)

# Boilerplate to get this to run
if __name__ == '__main__':

   import sys

   from twisted.python import log
   from twisted.internet import reactor
   log.startLogging(sys.stdout)

   factory = earEEGServerFactory("ws://localhost:9000")
   factory.protocol = earEEGServerProtocol

   reactor.listenTCP(9000, factory)
   reactor.run()
