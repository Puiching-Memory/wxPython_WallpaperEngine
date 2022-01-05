import API
import win32gui
import M_Vedio
import wx

#查找任何窗口,将其放在桌面背景上层,桌面图标下层
app = wx.App(False)
Frame = M_Vedio.CalcFrame(None)
Frame.Show()

API.RUN(player_window_handel=win32gui.FindWindow(None, "RBS_WALP"))

app.MainLoop()