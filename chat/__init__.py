import socket
import sys
import threading
import os

class chatUtilityClass:

    def __init__(self):
        self.socket_ = None

class chatClientClass:
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
                self.close_()
                sys.exit(0)
            elif message == ':help':
                print('chat tool version 0.1')
                print('---------------------')
                print('type => :quit')
                print('        exit chat')
                print('type => :help')
                print('        display help')
            else:
                self.socket_.sendto( bytearray(message, 'UTF-8'), (inetmask, port) )

    @classmethod
    def close_(self):
        self.socket_.close()

class chatServerClass:
    
    @classmethod
    def create_socket_for_udp(self, ip='', port=6080):
        print('')
