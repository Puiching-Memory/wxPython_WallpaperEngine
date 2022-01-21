##############################
# import
##############################
import wx,wx.media

import GUI_Main
import win32api,win32con


##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Main.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Main.Main.__init__(self, parent)

		##self.ShowFullScreen(True) # 全屏
		self.SetDoubleBuffered(True) # 双缓冲

		self.SetTitle('RBS_WALP') # 设置窗口标题
		
		self.Move(0,0)

		screen_Size_X = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
		screen_Size_Y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

		print(screen_Size_X,screen_Size_Y) # 获取GUI大小
		
		#self.Vedio.SetSize(screen_Size_X, screen_Size_Y)
		self.SetSize(screen_Size_X, screen_Size_Y)
		#self.Vedio.Play()

		##self.Vedio.ShowPlayerControls() # 播放控件

		self.Vedio.Load( u"test_vedio.mp4" ) # 加载视频
		self.Vedio.Bind(wx.media.EVT_MEDIA_STOP, self.Restart)

		self.Vedio.Play()

	
	def Restart(self, event):
		self.Vedio.Play()
		print('Replay')
		

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

