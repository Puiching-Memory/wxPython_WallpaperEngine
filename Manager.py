# import
import os
import shutil

import cv2
import win32gui
import wx
import wx.svg

import GUI_Manager
import Main
import windows_API

# GUI类继承
class CalcFrame(GUI_Manager.Main):
	def __init__(self, parent):
		GUI_Manager.Main.__init__(self, parent)

		self.i = 1 # 循环变量 .int
		self.fps = 25 # 帧率 n/s
		self.x = 0 # 宽 px
		self.y = 0 # 高 px
		self.speed = 0 # 播放帧速率 n/s
		self.tick = 0 # 时钟间隔 ms

		self.NoteBook.SetSelection(0)

		SVG_File = wx.svg.SVGimage.CreateFromFile('./icon/File.svg').ConvertToScaledBitmap(wx.Size(35, 35), self)
		SVG_Folder = wx.svg.SVGimage.CreateFromFile('./icon/Folder.svg').ConvertToScaledBitmap(wx.Size(35, 35), self)

		self.A_B_File.SetBitmap(SVG_File)
		self.A_B_Foler.SetBitmap(SVG_Folder)

		self.A_B_File.SetBackgroundColour('white')
		self.A_B_Foler.SetBackgroundColour('white')

	def Close(self, event):
		"""
		退出事件
		---
		停止计时器、销毁窗体
		"""

		self.Timer.Stop()
		self.Destroy()
		Frame_Main.Destroy()

	def Change_Rate(self, event):
		"""
		调整播放速率事件
		---
		改变的是速率因数，依据帧速率计算计时器间隔
		"""

		self.speed = round(self.fps * (self.S_Rate.GetValue() / 100), 1)
		self.tick = int(1000 / self.speed)

		##print(self.speed, self.tick)

	def Select_File(self, event):
		"""
		选择文件事件
		---
		提供文件选择窗体->检查文件类型->对应处理
		"""

		wildcard = "mp4 文件 (*.mp4)|*.mp4"
		with wx.FileDialog(self, "添加媒体文件...", wildcard=wildcard,
						style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return     # the user changed their mind

			# Proceed loading the file chosen by the user
			pathname = fileDialog.GetPath()
			try:
				with open(pathname, 'r') as file:
					path = pathname
					imgPath = './Cache/'

					if os.path.splitext(path)[-1] == '.mp4':

						if not os.path.exists(imgPath):
							os.mkdir(imgPath)
						else:
							shutil.rmtree(imgPath)
							os.mkdir(imgPath)

						self.Video2Pic(videoPath=path, imgPath=imgPath)
						self.T_Size.SetLabel(str(self.x) + 'X' + str(self.y))
						
			except IOError:
				wx.LogError('Cannot open file')

	def Time_Tick(self, event):
		"""
		计时器事件
		---
		循环下一张图片，并将其绘制到DC上
		"""
		if self.Timer.GetInterval() != self.tick:
			self.Timer.Stop()
			self.Timer.Start(self.tick)
			print('时钟间隔更改，正在重启')

		path = './Cache/' + str(self.i).zfill(4) + '.jpg'

		if os.path.exists(path):
			dc = wx.ClientDC(Frame_Main)
			dc.DrawBitmap(wx.Bitmap(path), 0, 0)
			Frame_Main.Refresh()

			self.i = self.i + 1

		else:
			print('到达播放终点-<')
			self.i = 1

	# ----------------------------------------------------------------

	def Video2Pic(self, videoPath, imgPath):
		##videoPath = "youvideoPath"  # 读取视频路径
		##imgPath = "youimgPath"  # 保存图片路径

		cap = cv2.VideoCapture(videoPath)

		fps = cap.get(cv2.CAP_PROP_FPS)  # 获取帧率
		self.fps = fps

		width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽度
		self.x = width

		height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取高度
		self.y = height

		print('视频帧率：', fps, '画幅：', width, height)

		suc = cap.isOpened()  # 是否成功打开
		frame_count = 0

		self.A_B_File.Disable()
		try:
			while suc:
				frame_count += 1
				suc, frame = cap.read()
				path = imgPath + str(frame_count).zfill(4) + '.jpg'
				cv2.imwrite(path, frame)
				cv2.waitKey(1)
				print(path,int(cap.get(1) / cap.get(7) * 100),'%')
				self.Guage.SetValue(int(cap.get(1) / cap.get(7) * 100))
		except:
			cap.release()
			self.Guage.SetValue(0)
			self.speed = round(self.fps * (self.S_Rate.GetValue() / 100), 1)
			self.tick = int(1000 / self.speed)
			self.Timer.Start(self.tick)
			self.A_B_File.Enable()
			print("视频转图片结束！")
		else:
			cap.release()
			self.Guage.SetValue(0)
			self.speed = round(self.fps * (self.S_Rate.GetValue() / 100), 1)
			self.tick = int(1000 / self.speed)
			self.Timer.Start(self.tick)
			self.A_B_File.Enable()
			print("视频转图片结束！")

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

	windows_name = Frame_Main.GetTitle()
	windows_API.RUN(player_window_handel=win32gui.FindWindow(None, windows_name))

	app.MainLoop()


if __name__ == "__main__":
	main()
