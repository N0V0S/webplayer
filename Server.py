import socket
import threading
import win32api
from pytify import Spotify
import traceback, sys
import time

class Server:
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    serverlistener = []
    nachrichten = []


    def __init__(self):
        self.s.bind((self.host, self.port))
        self.s.listen(5)

    def run(self):
        while True:
            c, addr = self.s.accept()
            print('Got connection from', addr)

            self.serverlistener.append(ServerListen(c).start())

    @staticmethod
    def getnachrichten(self):
        return self.nachrichten


class ServerListen(threading.Thread):

    c = None
    hwcode1 = 27
    hwcode2 = 27
    hwcode3 = 27
    hwcode4 = 27
    hwcode5 = 27
    hwcode6 = 27
    hwcode7 = 27

    VK_VOLUME_MUTE = 0xAD
    VK_VOLUME_DOWN = 0xAE
    VK_VOLUME_UP = 0xAF
    VK_MEDIA_NEXT_TRACK = 0xB0
    VK_MEDIA_PREV_TRACK = 0xB1
    VK_MEDIA_STOP = 0xB2
    VK_MEDIA_PLAY_PAUSE = 0xB3

    
    def __init__(self, connection):
        threading.Thread.__init__(self)
        print("new thread")
        self.c = connection

        ##--- Virtual Key Codes
        hwcode1 = win32api.MapVirtualKey(self.VK_MEDIA_NEXT_TRACK, 0)
        hwcode2 = win32api.MapVirtualKey(self.VK_MEDIA_PLAY_PAUSE, 0)
        hwcode3 = win32api.MapVirtualKey(self.VK_MEDIA_PREV_TRACK, 0)
        hwcode4 = win32api.MapVirtualKey(self.VK_MEDIA_STOP, 0)
        hwcode5 = win32api.MapVirtualKey(self.VK_VOLUME_UP, 0)
        hwcode6 = win32api.MapVirtualKey(self.VK_VOLUME_DOWN, 0)
        hwcode7 = win32api.MapVirtualKey(self.VK_VOLUME_MUTE, 0)

    def run(self):
        while True:
            try:
                receivedMessage = self.c.recv(1024).decode("utf-8")
                print(receivedMessage + "\n")
                if receivedMessage:
                    Server.getnachrichten(Server).append(receivedMessage)        
                    if ('next' in receivedMessage):
                        win32api.keybd_event(self.VK_MEDIA_NEXT_TRACK, self.hwcode1)
                    if ('prev' in receivedMessage):
                        win32api.keybd_event(self.VK_MEDIA_PREV_TRACK, self.hwcode3)
                    if ('pause' in receivedMessage):
                        win32api.keybd_event(self.VK_MEDIA_PLAY_PAUSE, self.hwcode2)
                    if ('stop' in receivedMessage):
                        win32api.keybd_event(self.VK_MEDIA_STOP, self.hwcode4)
                    if ('volup' in receivedMessage):
                        for i in range(0,15):
                            win32api.keybd_event(self.VK_VOLUME_UP, self.hwcode5)
                            x = i
                    if ('voldown' in receivedMessage):
                        for i in range(0,15):
                            win32api.keybd_event(self.VK_VOLUME_DOWN, self.hwcode6)
                            x = i
                    if ('mute' in receivedMessage):
                        win32api.keybd_event(self.VK_VOLUME_MUTE, self.hwcode7)
                    time.sleep(0.5)
                    spotify = Spotify()
                    songInfo = spotify.getCurrentTrack()
                    if songInfo:
                        songInfo += ', Artist: ' + spotify.getCurrentArtist()
                        print(songInfo + "\n")
                        self.c.send(bytes(songInfo))
                        break;
                    self.c.send(bytes('Error gettin SongInfo'))
                    break;
            except Exception:
                traceback.print_exc(file=sys.stdout)
                break;


server = Server()
print("renn Server renn")
server.run()

