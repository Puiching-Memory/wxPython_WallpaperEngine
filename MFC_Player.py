"""
针对MFPlay计的播放窗口
MFPlay属于windows media foundation的子项目
---
继承关系:Manager.py <- MFC_Player.py <- GUI_MFC.py <- GUI_MFC.fbp
数据关系:Manager.py(URL) -> MFC_Player.py -> MFPCreateMediaPlayer()
"""

##############################
# import
##############################

import wx

import GUI_MFC

import win32api
import win32con
import win32gui
import win32print

import ctypes

##############################
# GUI
##############################


class CalcFrame(GUI_MFC.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_MFC.Main.__init__(self, parent)

		self.SetDoubleBuffered(True)  # 双缓冲
		self.SetTitle("RBS_WALP_MFC")  # 设置窗口标题

		self.SetSize(get_real_resolution())
		self.Move(0, 0)

	def MainOnEraseBackground(self, event):
		event.Skip()

	def MainOnPaint(self, event):
		event.Skip()

	def Close(self, event):
		self.Destroy()

	# ------------------------------------------------------

	def Play(self, url: str, hwnd: int):
		try:
			MFPlay = ctypes.WinDLL("MFPlay.dll")
		except Exception as error:
			print(error)
			return -1

		if url == "" or url == None:
			print("Value error:url")
			return -1

		g_pPlayer = ctypes.c_char_p()

		##CMPFUNC = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_int))
		##cb = CMPFUNC(REA)
		
		re = MFPlay.MFPCreateMediaPlayer(
			url,
			True,  # 是否自动播放
			0,  # Flags -> https://learn.microsoft.com/zh-cn/windows/win32/api/mfplay/ne-mfplay-_mfp_creation_options
			None,  # 在此提供回调函数
			hwnd,
			ctypes.byref(g_pPlayer),  # 接收 指向IMFPMediaPlayer接口的指针
		)
		
		print("g_pPlayer.value:" ,g_pPlayer.value,g_pPlayer)
		print("re:",re)
		
class IMFPMediaPlayer():
	def __init__(self, number):
		self._as_parameter_ = number

##############################
# 主函数
##############################


def main():
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


def REA():
	print('call-----------')
	return 0


if __name__ == "__main__":
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	frame.Play('src/bg.mp4',frame.GetHandle())
	app.MainLoop()
