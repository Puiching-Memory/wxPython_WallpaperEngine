##############################
# import
##############################
import wx,wx.media

import GUI_Manager
import Main

import windows_API
import win32gui
import webview

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Manager.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Manager.Main.__init__(self, parent)

		self.T_BestSize.SetLabel(str(Frame_Main.Vedio.GetBestSize()))

		Frame_Main.Vedio.Bind(wx.media.EVT_MEDIA_FINISHED, self.Restart)
		Frame_Main.Vedio.Bind(wx.media.EVT_MEDIA_LOADED, self.Loaded)
		Frame_Main.Vedio.Bind(wx.media.EVT_MEDIA_STOP, self.stop)

	def Close(self, event):
		self.Timer.Stop()
		self.Destroy()
		Frame_Main.Destroy()

	def Change_Volume(self, event):
		Frame_Main.Vedio.SetVolume(self.S_Volume.GetValue() / 100)
		print("Volume",self.S_Volume.GetValue(), '%')

	
	def OnFileChanged(self, event):
		if '.html' in self.filePicker.GetPath():
			Frame_Main.Vedio.Stop()
			Frame_Main.Destroy()
			self.Timer.Stop()
			self.Hide()

			window = webview.create_window('RBS_WALP_HTML', self.filePicker.GetPath())
			webview.start(html_boost, window)
		else:
			Frame_Main.Vedio.Stop()
			Frame_Main.Vedio.Load(self.filePicker.GetPath())
			self.T_BestSize.SetLabel(str(Frame_Main.Vedio.GetBestSize()))
			self.T_Length.SetLabel(str(Frame_Main.Vedio.Length()))

	def TimerOnTimer(self, event):
		self.T_Length.SetLabel(str(Frame_Main.Vedio.Length() / 1000) + 's')
		self.T_Tell.SetLabel(str(Frame_Main.Vedio.Tell() / 1000) + 's')
		if Frame_Main.Vedio.Length() != 0:
			self.GUIDE.SetValue(int(Frame_Main.Vedio.Tell() / Frame_Main.Vedio.Length() * 100))

	def Control_MOnButtonClick(self, event):
		print(Frame_Main.Vedio.GetState())
		if Frame_Main.Vedio.GetState() == 2:
			self.Control_M.SetLabel('start')
			Frame_Main.Vedio.Pause()
		else:
			self.Control_M.SetLabel('pause')
			Frame_Main.Vedio.Play()

	def Change_Rate(self, event):
		rate = self.S_Rate.GetValue() / 100
		Frame_Main.Vedio.SetPlaybackRate(rate)

	def Restart(self, event):
		Frame_Main.Vedio.Play()
		print('Replay')

	def Loaded(self, event):
		print('loading complete')
		Frame_Main.Vedio.Play()

	def stop(self, event):
		print(1)


##############################
# 主函数
##############################


def main():
	global app
	global Frame_Main

	app = wx.App(False)
	Frame_Main = Main.CalcFrame(None)
	frame = CalcFrame(None)
	frame.Show(True)

	Frame_Main.Show()

	# windows api creature
	windows_API.RUN(player_window_handel=win32gui.FindWindow(None, "RBS_WALP"))

	app.MainLoop()
	
def html_boost(window):
	window.toggle_fullscreen()
	windows_API.RUN(player_window_handel=win32gui.FindWindow(None, "RBS_WALP_HTML"))
	
if __name__ == "__main__":
	main()

