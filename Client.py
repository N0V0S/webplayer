#!/usr/bin/python
import socket
import sys

class Client:
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    ip = '192.168.0.103'

    def __init__(self):
        return

    def connect(self):
        self.s.connect((self.ip, self.port))

    def sendMessage(self, text):
        try:
            nachricht = text
            print(nachricht)
            self.s.send(bytes(nachricht))
        finally:
            self.s.close()

def main():
    client = Client()
    client.connect()
    client.sendMessage("next")

if __name__ == '__main__':
    main()
