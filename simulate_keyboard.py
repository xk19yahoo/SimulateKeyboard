#coding=cp936
import win32gui,win32api,win32con
import time
import threading

def key():
    interval = 0.3
    while True:
        time.sleep(interval )

        win32api.keybd_event(65,0,0,0) #a键位码是86
        win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)


t = threading.Thread(target=key)
t.start()
