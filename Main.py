##############################
# import
##############################
import wx

import GUI_Main
import win32api,win32con


##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Main.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Main.Main.__init__(self, parent)

		self.SetDoubleBuffered(True) # 双缓冲

		self.SetTitle('RBS_WALP') # 设置窗口标题
		
		self.Move(0,0)

		screen_Size_X = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
		screen_Size_Y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

		print(screen_Size_X,screen_Size_Y) # 获取GUI大小
		
		self.SetSize(screen_Size_X, screen_Size_Y)

		self.i = 1


	def MainOnEraseBackground(self, event):
		pass
	
	def MainOnPaint(self, event):
		pass

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

if __name__ == "__main__":
	main()

