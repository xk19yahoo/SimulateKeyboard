#coding:cp936
import win32api, win32con
def click(x,y):
    #flags, hcursor, (x,y) = win32gui.GetCursorInfo()#返回光标所有信息
    #win32gui.GetCursorPos(point)#获取屏幕位置
    win32api.SetCursorPos((x,y))#设置位置
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)#按下动作
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)#松开动作
click(10,10)
