# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SPL_Player", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = 0|wx.BORDER_NONE|wx.TRANSPARENT_WINDOW )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Bind( wx.EVT_ERASE_BACKGROUND, self.MainOnEraseBackground )
		self.Bind( wx.EVT_LEFT_DOWN, self.Close )
		self.Bind( wx.EVT_PAINT, self.MainOnPaint )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def MainOnEraseBackground( self, event ):
		event.Skip()


	def MainOnPaint( self, event ):
		event.Skip()


