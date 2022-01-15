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

	def Close(self, event):
		self.Destroy()
		Frame_Main.T_Check.Stop()
		Frame_Main.Destroy()

	def Change_Volume(self, event):
		Frame_Main.Vedio.SetVolume(self.S_Volume.GetValue())
		print("Volume",self.S_Volume.GetValue())


##############################
# 主函数
##############################


def main():
	global app
	
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)

	global Frame_Main
	Frame_Main = Main.CalcFrame(None)
	Frame_Main.Show()

	# windows api creature
	windows_API.RUN(player_window_handel=win32gui.FindWindow(None, "RBS_WALP"))

	app.MainLoop()
	
	
if __name__ == "__main__":
	main()

