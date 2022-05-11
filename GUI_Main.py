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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"RBS_WALP", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.FRAME_SHAPED|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.Timer = wx.Timer()
		self.Timer.SetOwner( self, wx.ID_ANY )
		self.Timer.Start( 10 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Bind( wx.EVT_ERASE_BACKGROUND, self.MainOnEraseBackground )
		self.Bind( wx.EVT_PAINT, self.MainOnPaint )
		self.Bind( wx.EVT_TIMER, self.Time_Tick, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def MainOnEraseBackground( self, event ):
		event.Skip()

	def MainOnPaint( self, event ):
		event.Skip()

	def Time_Tick( self, event ):
		event.Skip()


