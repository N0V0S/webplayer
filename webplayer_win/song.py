import win32api
import win32gui
import sys
import datetime
import time

class Song:

    hwcode1 = 42
    hwcode2 = 42
    hwcode3 = 42
    hwcode4 = 42
    hwcode5 = 42
    hwcode6 = 42
    hwcode7 = 42

    VK_VOLUME_MUTE =        0xAD
    VK_VOLUME_DOWN =        0xAE
    VK_VOLUME_UP =          0xAF
    VK_MEDIA_NEXT_TRACK =   0xB0
    VK_MEDIA_PREV_TRACK =   0xB1
    VK_MEDIA_STOP =         0xB2
    VK_MEDIA_PLAY_PAUSE =   0xB3

    # spotify Instance vars
    hwnd = None
    # spotify rect
    spotify_rect = None

    def __init__(self):

         ##--- Virtual Key Codes
        self.hwcode1 = win32api.MapVirtualKey(self.VK_MEDIA_NEXT_TRACK, 0)
        self.hwcode2 = win32api.MapVirtualKey(self.VK_MEDIA_PLAY_PAUSE, 0)
        self.hwcode3 = win32api.MapVirtualKey(self.VK_MEDIA_PREV_TRACK, 0)
        self.hwcode4 = win32api.MapVirtualKey(self.VK_MEDIA_STOP, 0)
        self.hwcode5 = win32api.MapVirtualKey(self.VK_VOLUME_UP, 0)
        self.hwcode6 = win32api.MapVirtualKey(self.VK_VOLUME_DOWN, 0)
        self.hwcode7 = win32api.MapVirtualKey(self.VK_VOLUME_MUTE, 0)
        

    def sendMessage(self, text):
        try:
            self.hwnd = win32gui.FindWindow("SpotifyMainWindow", None)
            self.spotify_rect = win32gui.GetWindowRect(self.hwnd)
        except Exception as exce:
            print("spotify not running")
            return
        
        if('next' in text):
            win32api.keybd_event(self.VK_MEDIA_NEXT_TRACK, self.hwcode1)
        if ('prev' in text):
            win32api.keybd_event(self.VK_MEDIA_PREV_TRACK, self.hwcode3)
        if ('pause' in text):
            win32api.keybd_event(self.VK_MEDIA_PLAY_PAUSE, self.hwcode2)
        if ('stop' in text):
             win32api.keybd_event(self.VK_MEDIA_STOP, self.hwcode4)
        if ('volup' in text):
            for i in range(0,25):
                win32api.keybd_event(self.VK_VOLUME_UP, self.hwcode5)
                x = i
        if ('voldown' in text):
            for i in range(0,25):
                win32api.keybd_event(self.VK_VOLUME_DOWN, self.hwcode6)
                x = i
        if ('mute' in text):
            win32api.keybd_event(self.VK_VOLUME_MUTE, self.hwcode7)
        time.sleep(.3)
        trackinfo = win32gui.GetWindowText(self.hwnd).split(" - ")
        print( text + "<br>" + 'Artist: ' +  trackinfo[0] + '   Track: ' + trackinfo[1] + "<br>")


def main():
    song = Song()
    song.sendMessage(str(sys.argv[1] + " " + sys.argv[2] + " " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

if __name__ == '__main__':
    main()
