import socket
import sys
import os
import threading

class chatClient:
    @classmethod
    def __init__(self):
        # create socket
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # set broad cast option
        self.socket_.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket_.bind(('', 6080))
    
    @classmethod
    def start_(self, inetmask, port):
        message = input('')
        if message == ':quit':
            self.socket_.sendto( bytearray(':quit', 'UTF-8'), (inetmask, 6081) )
            self._close()
        elif message == ':help':
            print('chat tool version 0.2')
            print('---------------------')
            print('type => :quit')
            print('        exit client.py')
            print('type => :help')
            print('        display help')
        else:
            self.socket_.sendto( bytearray(message, 'UTF-8'), (inetmask, 6081) )
        self.start_(inetmask=inetmask, port=port)

    @classmethod
    def _close(self):
        self.socket_.close()
        sys.exit()

class chatDisplay:
    @classmethod
    def __init__(self):
        # shutdown password
        # create socket
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_.bind(('', 6081))

    @classmethod
    def start_(self, inetmask, port):
        thread = threading.Thread(target=self.thread_waiting, name='th_waiting')
        thread.start()
    
    @classmethod
    def thread_waiting(self):
        message, ip_address = self.socket_.recvfrom(4096)
        decode_message = message.decode('UTF-8')
        if decode_message == ':quit':
            self.socket_.close()
            sys.exit()
        elif decode_message == '':
            self.thread_waiting()
        else:
            print( '[%s] %s' % (ip_address[0], decode_message), sep='\n', end='\n')
            self.thread_waiting()
