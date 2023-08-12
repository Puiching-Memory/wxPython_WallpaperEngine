
##############################
# import
##############################
import wx

import GUI_TEST1

from OpenGL.GL import *
from OpenGL.GLUT import *

import wx.glcanvas

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_TEST1.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_TEST1.Main.__init__(self, parent)

		#self.SetDoubleBuffered(True)  # 双缓冲

		canvas = CubeCanvas(parent=self)
		context = wx.glcanvas.GLContext(canvas)

		self.SetTitle('RBS_WALP')  # 设置窗口标题

	def MainOnEraseBackground(self, event):
		pass
		##event.Skip()

	def MainOnPaint(self, event):
		event.Skip()

	def Close(self, event):
		self.Destroy()


class MyCanvasBase(wx.glcanvas.GLCanvas):
	def __init__(self, parent):
		wx.glcanvas.GLCanvas.__init__(self, parent, -1)
		self.init = False
		self.context = wx.glcanvas.GLContext(self)
		
		# initial mouse position
		self.lastx = self.x = 30
		self.lasty = self.y = 30
		self.size = None
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
		self.Bind(wx.EVT_SIZE, self.OnSize)
		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
		self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
		self.Bind(wx.EVT_MOTION, self.OnMouseMotion)


	def OnEraseBackground(self, event):
		pass # Do nothing, to avoid flashing on MSW.


	def OnSize(self, event):
		wx.CallAfter(self.DoSetViewport)
		event.Skip()

	def DoSetViewport(self):
		size = self.size = self.GetClientSize()
		self.SetCurrent(self.context)
		glViewport(0, 0, size.width, size.height)
		


	def OnPaint(self, event):
		dc = wx.PaintDC(self)
		self.SetCurrent(self.context)
		if not self.init:
			self.InitGL()
			self.init = True
		self.OnDraw()


	def OnMouseDown(self, evt):
		self.CaptureMouse()
		self.x, self.y = self.lastx, self.lasty = evt.GetPosition()


	def OnMouseUp(self, evt):
		self.ReleaseMouse()


	def OnMouseMotion(self, evt):
		if evt.Dragging() and evt.LeftIsDown():
			self.lastx, self.lasty = self.x, self.y
			self.x, self.y = evt.GetPosition()
			self.Refresh(False)




class CubeCanvas(MyCanvasBase):
	def InitGL(self):
		with open('./Shader.vsh', 'r', encoding='utf-8') as f:
			vertex_shader_src = f.read()

		vertex_shader = glCreateShader(GL_VERTEX_SHADER)
		glShaderSource(vertex_shader, vertex_shader_src)
		glCompileShader(vertex_shader)

		self.program = glCreateProgram()
		glAttachShader(self.program, vertex_shader)
		glDeleteShader(vertex_shader)

		glLinkProgram(self.program)
		

	def OnDraw(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glBegin(GL_QUADS)

		glUseProgram(self.program)
		
		glEnd()
		
		self.SwapBuffers()



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
