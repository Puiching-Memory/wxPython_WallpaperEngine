'''
针对wx.DC设计的播放窗口
---
主从关系:Manager.py -> SPL_Player.py <- GUI_SPL.py <- GUI_SPL.fbp
'''
##############################
# import
##############################
import wx

import GUI_SPL

import win32api
import win32con
import win32gui
import win32print

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_SPL.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_SPL.Main.__init__(self, parent)

        #self.SetDoubleBuffered(True)  # 双缓冲

        self.SetTitle('RBS_WALP')  # 设置窗口标题

        self.SetSize(get_real_resolution())

        self.Move(0, 0)

        self.i = 1
        
    def MainOnEraseBackground(self, event):
        event.Skip()

    def MainOnPaint(self, event):
        event.Skip()

    def Close(self, event):
        self.Destroy()


##############################
# 主函数
##############################


def main():
    global app
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    app.MainLoop()


def get_real_resolution():
    """获取真实的分辨率"""
    hDC = win32gui.GetDC(0)
    # 横向分辨率
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    # 纵向分辨率
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h


def get_screen_size():
    """获取缩放后的分辨率"""
    screen_Size_X = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_Size_Y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    return screen_Size_X, screen_Size_Y


if __name__ == "__main__":
    main()
