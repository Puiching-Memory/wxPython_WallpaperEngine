'''
运行环境:python3.9.10
IDLE:vscode
作者：@DreamBack https://github.com/Puiching-Memory

项目描述:基于wxpython的动态壁纸引擎

##文件描述：控制中心/管理/时钟刻/设置/数据传输

'''

# import
import os
import shutil
import configparser

import win32gui
import win32api
import win32print
import win32con
import wx
import wx.svg 
import threading

import win32mica #win11云母实现

import GUI_Manager

import SPL_Player # 基于wx.DC的软件播放器
import MFC_Player # 基于MFPlay的windows media foundation架构播放器
import windows_API # 将窗口载入壁纸层

# GUI类继承
class CalcFrame(GUI_Manager.Main):
	def __init__(self, parent):
		GUI_Manager.Main.__init__(self, parent)

		self.fps = 25 # 视频帧率 n/s
		self.x = 0 # 视频宽 px
		self.y = 0 # 视频高 px
		self.sx ,self.sy= get_real_resolution() # 屏幕物理分辨率 px
		self.speed = 25 # 播放帧速率 n/s
		self.tick = 0 # 时钟间隔 ms
		self.length = 50 # 视频帧总数 f
		self.tell = 1 # 视频当前播放帧 f
		self.path = '' # 视频路径(文件夹路径) str
		self.list = [] # 视频播放列表(文件夹路径) list
		self.cfg = configparser.ConfigParser() # cfg设置

		#---GUI初始化部分
		self.NoteBook.SetSelection(0)
		self.A_Thumbnail_ListCtrl.SetDropTarget(FileDropTarget_Thumbnail(self))

		SVG_File = wx.svg.SVGimage.CreateFromFile('./icon/File.svg').ConvertToScaledBitmap(wx.Size(35, 35), self)
		SVG_Folder = wx.svg.SVGimage.CreateFromFile('./icon/Folder.svg').ConvertToScaledBitmap(wx.Size(35, 35), self)
		SVG_Refresh = wx.svg.SVGimage.CreateFromFile('./icon/Refresh.svg').ConvertToScaledBitmap(wx.Size(35, 35), self)

		self.A_B_File.SetBitmap(SVG_File)
		self.A_B_Foler.SetBitmap(SVG_Folder)
		self.A_B_Refresh.SetBitmap(SVG_Refresh)

		self.A_B_File.SetBackgroundColour('white')
		self.A_B_Foler.SetBackgroundColour('white')
		self.A_B_Refresh.SetBackgroundColour('white')
		
		self.Thumbnail_Refresh()

		self.Refresh_Size()

		mode = win32mica.MICAMODE.DARK  #为主窗口添加云母效果
		win32mica.ApplyMica(self.GetHandle(), mode)

	def Close(self, event):
		"""
		退出事件
		---
		停止计时器、销毁窗体
		"""

		self.Timer.Stop()
		self.Destroy()
		self.Disable()
		Frame_SPL.Destroy()

	def Thumbnail_Refresh(self, *event):
		"""
		刷新视频图表事件
		---
		扫描Cache文件夹,确认文件可用性,将首个图片作为缩略图使用

		step2-将记录加载入视频播放列表
		"""

		self.A_Thumbnail_ListCtrl.ClearAll()
		lmage_list = wx.ImageList(120, 80, mask=False, initialCount=1) # 初始化图像列表
		dir_name = [] # 文件夹名list

		for root, dirs, files in os.walk('./Cache/'):
			for name in dirs: # 遍历子文件夹(不包括子文件夹内文件)
				dir_path = os.path.join(root, name) # 文件夹路径str
				
				if len(os.listdir(dir_path)) != 0: # 排除空文件夹
					dir_name.append(name) # 文件夹名list
					thumbnail_path = dir_path + '/' + os.listdir(dir_path)[0] # 计算缩略图路径
					lmage_list.Add(wx.Bitmap(wx.Image(thumbnail_path).Scale(120,80,quality=wx.IMAGE_QUALITY_HIGH))) # 添加到图像列表

		self.A_Thumbnail_ListCtrl.AssignImageList(lmage_list,0) # 绑定图像列表

		for i in range(0, len(dir_name)):
			info = dir_name[i] # 提取文件夹名作为info
			self.A_Thumbnail_ListCtrl.InsertItem(self.A_Thumbnail_ListCtrl.GetItemCount(),info) # 插入最后端
			
			self.A_Thumbnail_ListCtrl.SetItemImage(i,i) # 将标签索引与图像列表索引绑定

	def A_Thumbnail_ListCtrlOnListItemActivated(self, event):
		"""
		视频图表双击任意标签事件
		---
		将该标签添加到播放列表,同时播放该标签对应的视频
		"""
		id = self.A_Thumbnail_ListCtrl.GetFocusedItem() # 选中标签的ID
		name = self.A_Thumbnail_ListCtrl.GetItemText(id) # 选中标签的文本

		if self.A_PlayList.FindString(name) == -1:
			self.A_PlayList.Append(name) # 添加入播放列表	

		self.path = './Cache/' + name + '/'

		self.list.clear()
		for i in range(0, self.A_PlayList.GetCount()):
			self.list.append('./Cache/' + self.A_PlayList.GetString(i) + '/')

		try:
			cfg = self.cfg
			cfg.read(self.path + 'cfg.cfg')

			self.fps = int(float(cfg.get('Vedio','fps'))) # 视频帧率 n/s
			self.x = int(cfg.get('Vedio','x')) # 视频宽 px
			self.y = int(cfg.get('Vedio','y')) # 视频高 px
			self.speed = self.fps # 播放帧速率 n/s
			self.length = int(cfg.get('Vedio','lenth')) # 视频帧总数 f
			self.tell = 1 # 视频当前播放帧 f
		except Exception as error:
			print('读取cfg时出现问题',error)

	def A_Thumbnail_ListCtrlOnListBeginDrag(self, event):
		"""
		视频图表左键拖动标签事件
		---
		如果拖动到播放列表上,则将其添加如播放列表,同时播放该标签对应的视频
		"""
		id = self.A_Thumbnail_ListCtrl.GetFocusedItem() # 选中标签的ID
		name = self.A_Thumbnail_ListCtrl.GetItemText(id) # 选中标签的文本
		dir_path = os.path.abspath(os.path.join('./Cache/', name)) # 选中标签的文件夹绝对路径

		data = wx.FileDataObject()
		data.AddFile(dir_path)

		dropSource = wx.DropSource()
		dropSource.SetData(data)
		result= dropSource.DoDragDrop()

	def Change_Rate(self, *event):
		"""
		调整播放速率事件
		---
		改变的是速率因数，依据帧速率计算计时器间隔
		"""

		self.speed = round(self.fps * (self.S_Rate.GetValue() / 100), 1)
		self.tick = int(1000 / self.speed)

		self.T_FPS.SetLabel(str(self.fps) + 'F/S' + '\n' +
							str(self.speed) + '(t)F/S')

		##print(self.speed, self.tick)

	def Select_File(self, event):
		"""
		选择文件事件
		---
		提供文件选择窗体->检查文件类型->对应处理
		"""

		wildcard = ('mp4 文件 (*.mp4)|*.mp4'
					+'|mov文件 (*.mov)|*.mov')
		
		with wx.FileDialog(self, "添加媒体文件...", wildcard=wildcard,
						style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return     # the user changed their mind

			# Proceed loading the file chosen by the user
			pathname = fileDialog.GetPath()

			try:
				self.Analysis(pathname)
			except IOError as error:
				wx.LogError('Cannot open file || 载入文件失败！' + '\n' 
							+ '错误捕获：' + str(error))


	def MainOnSize(self, event):
		"""
		主窗口调整大小事件
		---
		调整部分控件的大小以适应其变化
		"""
		print(self.GetSize())

		sizex, sizey = self.GetSize()

		self.A_Thumbnail_ListCtrl.SetMinSize(wx.Size(sizex - 160, sizey - 150))
		self.A_PlayList.SetMinSize(wx.Size(self.A_PlayList.GetSize()[0], sizey - 150))
		self.Guage.SetMinSize(wx.Size(sizex, 5))

		event.Skip()

	def Refresh_Size(self):
		"""
		利用更改大小时窗口的重新排列刷新控件位置
		---
		base on Setsize()
		"""
		self.SetSize(self.GetSize()[0] - 1, self.GetSize()[1])
		self.SetSize(self.GetSize()[0] + 1, self.GetSize()[1])

	def T_RateOnLeftDClick(self,event):
		"""
		鼠标左键双击播放速率文本事件
		---
		将视频播放速率拖动条控件恢复至默认值
		"""

		self.S_Rate.SetValue(100)
		self.Change_Rate()

	def B_Tell_ControlOnScroll(self, event):
		"""
		所有视频播放进度条控件事件
		---
		触发时暂停视频的播放
		"""
		if event.GetEventType() != wx.wxEVT_SCROLL_CHANGED: # 排除视频播放进度条控件结束事件
			self.Timer.Stop()
			print('stop!')

		event.Skip()

	def B_Tell_ControlOnScrollChanged(self, event):
		"""
		视频播放进度条控件结束事件
		---
		触发时重定位到目标帧并开始播放
		"""
		self.tell = round(self.B_Tell_Control.GetValue() / 100 * self.length)

		if self.tell == 0: # 因为帧序列从‘0001.xxx’开始,所以将0修改为1
			self.tell = 1

		self.Timer.Start(self.tick)
		print(self.tell)
		
		event.Skip()		

###########################################################################
# 文件拖入处理Class
# File Class
###########################################################################

class FileDropTarget_Thumbnail(wx.FileDropTarget):
	"""
	视频预览图窗口_文件拖动处理类
	---
	"""	
	def __init__(self, window:CalcFrame):

		wx.FileDropTarget.__init__(self)
		self.window = window # 继承自主GUI

	def OnDragOver(self, x, y, defResult):
		"""
		文件拖动进入目标窗口事件
		---
		更改GUI外观以提示
		"""
		return super().OnDragOver(x, y, defResult)

	def OnDropFiles(self, x, y, filenames):
		"""
		文件拖动完成事件
		---
		获取文件路径并进行处理
		"""
		##self.window.A_Thumbnail_ListCtrl.SetBackgroundColour('white')
		error_list = []

		for name in filenames:
			suffix = os.path.splitext(name)[-1] # 获取文件后缀名(包含'.')
			prefix = os.path.split(os.path.splitext(name)[0])[1] # 获取文件前缀名

			print(name, '文件类型:' + suffix)

			if suffix == '.mp4':
				wx.CallAfter(self.window.Analysis,name)
			elif suffix == '':
				pass
			else:
				error_list.append(name)

		Str = '加载以下文件时出现错误：'
		if len(error_list) != 0:
			for i in error_list:
				Str = Str + '\n' + i

			wx.CallAfter(wx.MessageBox, Str + '\n' + '错误原因：不支持的文件类型', caption='文件处理')

		return True


##############################
# 主函数
##############################


def main():
	global app
	global Frame_SPL

	app = wx.App(False)
	Frame_SPL = SPL_Player.CalcFrame(None)
	Frame_Manager = CalcFrame(None)
	
	Frame_SPL.Show()
	Frame_Manager.Show()

	windows_name = Frame_SPL.GetTitle()
	windows_API.RUN(player_window_handel=win32gui.FindWindow(None, windows_name))

	app.MainLoop()

def get_real_resolution():
	"""获取真实的分辨率"""
	hDC = win32gui.GetDC(0)
	# 横向分辨率
	w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
	# 纵向分辨率
	h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
	return w, h

if __name__ == "__main__":
	main()
