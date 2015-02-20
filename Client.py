#!/usr/bin/python
import socket
import sys
import datetime

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
            self.s.send(bytes(nachricht))
            while(True):
                receivedMessage = self.s.recv(1024).decode("utf-8")
                if receivedMessage:
                    print(receivedMessage + "<br>")
                    break;
        finally:
            self.s.close()

def main():
    client = Client()
    client.connect()
    client.sendMessage(str(sys.argv[1] + " " + sys.argv[2] + " \n" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    main()


