import socket
import sys
import threading
import os

class chatClient:
    @classmethod
    def __init__(self):
        # create socket
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # set broad cast option
        self.socket_.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    @classmethod
    def start_(self, inetmask, port):
        """
        socket client start
        """
        self.socket_.bind(('', port))
        while True:
            message = input('> ')
            if message == ':quit':
                self.socket_.sendto( bytearray('quit', 'UTF-8'), (inetmask, 6081) )
                self._close()
                sys.exit(0)
            elif message == ':help':
                print('chat tool version 0.1')
                print('---------------------')
                print('type => :quit display')
                print('        exit display')
                print('type => :help')
                print('        display help')
                print('type => :help')
                print('        display help')
            else:
                self.socket_.sendto( bytearray(message, 'UTF-8'), (inetmask, 6081) )

    @classmethod
    def _close(self):
        self.socket_.close()

class chatDisplay:
    @classmethod
    def __init__(self, password_):
        # shutdown password
        self.password = password_
        # create socket
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    @classmethod
    def start_(self, inetmask, port):
        shutdownSignal = 0
        self.socket_.bind(('', port))
        while True: 
            message, ip_address = self.socket_.recvfrom(4096)
            decode_message = message.decode('UTF-8')
            if decode_message == ':quit display':
                shutdownSignal=1
                print('please input startup password.')
            elif shutdownSignal:
                if (self.password == decode_message):
                    print('display is shutdown')
                    self.socket_.close()
                    sys.exit()
                else:
                    print('password is not match.')
            else:
                print( '[%s] %s' % (ip_address[0], decode_message) )
        sys.exit()