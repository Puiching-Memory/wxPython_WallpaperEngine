"""
todo:将指定窗口放置于桌面层下,静态壁纸层上
in:hwnd
out:None
"""

import win32gui
import win32con


def _MyCallback(hwnd, extra):  # 遍历窗口函数的回调函数（提前return退出遍历会报错）
    # 当前窗口中查找图标窗口
    icon_window = win32gui.FindWindowEx(hwnd, None, "SHELLDLL_DefView", None)
    if(icon_window != 0):  # 当前窗口包含图标窗口
        # 查找静态壁纸窗口并保存
        extra[0] = win32gui.FindWindowEx(None, hwnd, "WorkerW", None)


def RUN(player_window_handel):
    # 查找桌面窗口
    desktop_window_handel = win32gui.FindWindow("Progman", "Program Manager")

    # 核心语句，向desktop_window发送0x52C启用Active Desktop
    win32gui.SendMessageTimeout(desktop_window_handel, 0x52C,
                                0, 0, win32con.SMTO_ABORTIFHUNG, 500)  # 如果报TimeOut,增加延时

    # 设置player_window为desktop_window的子窗口
    win32gui.SetParent(player_window_handel, desktop_window_handel)

    # 因为有两个同类同名的WorkerW窗口，所以遍历所以顶层窗口
    workerw = [0]
    win32gui.EnumWindows(_MyCallback, workerw)
    # 获取player_windows名称
    player_windows_name = win32gui.GetWindowText(player_window_handel)
    # 隐藏静态壁纸窗口
    win32gui.ShowWindow(workerw[0], win32con.SW_HIDE)

    # 判断player_window是否在desktop_window下
    player_under_desktop = win32gui.FindWindowEx(
        desktop_window_handel, None, "SDL_app", player_windows_name)
    if(player_under_desktop == 0):  # 如果player_window位置不正确
        # 将player_window设置为desktop_window的子窗口
        win32gui.SetParent(player_window_handel, desktop_window_handel)

    ##win32gui.ShowWindow(player_window_handel, win32con.SW_SHOWMAXIMIZED)
