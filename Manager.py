##############################
# import
##############################
import wx
import win32gui
import os
import cv2
import shutil

import GUI_Manager
import Main

import windows_API



##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Manager.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Manager.Main.__init__(self, parent)

		self.i = 1

	def Close(self, event):
		self.Timer.Stop()
		self.Destroy()
		Frame_Main.Destroy()

	
	def OnFileChanged(self, event):
		path = self.filePicker.GetPath()
		imgPath = './Cache/'

		if os.path.splitext(path)[-1] == '.mp4':

			if not os.path.exists(imgPath):
				os.mkdir(imgPath)
			else:
				shutil.rmtree(imgPath)
				os.mkdir(imgPath)

			self.Guage.Pulse()
			self.Video2Pic(videoPath=path,imgPath=imgPath)
			self.T_Size.SetLabel(str(self.x) + 'X' + str(self.y))


	def Time_Tick(self, event):
		path = './Cache/' + str(self.i).zfill(4) +  '.jpg'
		##print(path)

		if os.path.exists(path):
			##print(1)
			dc = wx.ClientDC(Frame_Main)
			dc.DrawBitmap(wx.Bitmap(path), 0, 0)
			Frame_Main.Refresh()

			self.i = self.i + 1

		else:
			print('到达播放终点-<')
			self.i = 1
			##self.Timer.Stop()
	#----------------------------------------------------------------
			
	def Video2Pic(self,videoPath,imgPath):
		##videoPath = "youvideoPath"  # 读取视频路径
		##imgPath = "youimgPath"  # 保存图片路径
	
		cap = cv2.VideoCapture(videoPath)

		fps = cap.get(cv2.CAP_PROP_FPS)  # 获取帧率
		self.fps = fps

		width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽度
		self.x = width

		height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取高度
		self.y = height

		print('视频帧率：',fps,'画幅：',width,height)

		suc = cap.isOpened()  # 是否成功打开
		frame_count = 0
		try:
			while suc:
				frame_count += 1
				suc, frame = cap.read()
				path = imgPath + str(frame_count).zfill(4) + '.jpg'
				cv2.imwrite(path, frame)
				cv2.waitKey(1)
				print(path)
		except:
			cap.release()
			self.Guage.SetValue(0)
			self.Timer.Start(10)
			print("视频转图片结束！--错误")
		else:
			cap.release()
			self.Guage.SetValue(0)
			self.Timer.Start(10)
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

