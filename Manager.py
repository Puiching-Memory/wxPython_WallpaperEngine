##############################
# import
##############################
import wx

import GUI_Manager
import Main

import windows_API
import win32gui

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Manager.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Manager.Main.__init__(self, parent)

		self.T_BestSize.SetLabel(str(Frame_Main.Vedio.GetBestSize()))

	def Close(self, event):
		self.Timer.Stop()
		self.Destroy()
		Frame_Main.Destroy()

	def Change_Volume(self, event):
		Frame_Main.Vedio.SetVolume(self.S_Volume.GetValue() / 100)
		print("Volume",self.S_Volume.GetValue(), '%')

	def OnFileChanged(self, event):
		Frame_Main.Vedio.Stop()
		Frame_Main.Vedio.Load(self.filePicker.GetPath())
		self.T_BestSize.SetLabel(str(Frame_Main.Vedio.GetBestSize()))
		self.T_Length.SetLabel(str(Frame_Main.Vedio.Length()))

	def TimerOnTimer(self, event):
		self.T_Length.SetLabel(str(Frame_Main.Vedio.Length()))
		self.T_Tell.SetLabel(str(Frame_Main.Vedio.Tell()))
		##print(Frame_Main.Vedio.Tell() / Frame_Main.Vedio.Length())
		if Frame_Main.Vedio.Length() != 0:
			self.gauge.SetValue(int(Frame_Main.Vedio.Tell() / Frame_Main.Vedio.Length() * 100))

			if int(Frame_Main.Vedio.Tell() / Frame_Main.Vedio.Length() * 100) > 99:
				Frame_Main.Vedio.Pause()
				Frame_Main.Vedio.Stop()

			print(int(Frame_Main.Vedio.Tell() / Frame_Main.Vedio.Length() * 100))
		##print('Timer RUN')


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
	
	
if __name__ == "__main__":
	main()

