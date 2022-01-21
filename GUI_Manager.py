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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"RBS_WALP_Manager", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"RBS_WALP Engine", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.S_Volume = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,40 ), wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		bSizer3.Add( self.S_Volume, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Volume", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer1.Add( bSizer3, 0, 0, 5 )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.filePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"mp4 文件 (*.mp4)|*.mp4|mov 文件 (*.mov)|*.mov", wx.DefaultPosition, wx.Size( -1,40 ), wx.FLP_DEFAULT_STYLE )
		bSizer31.Add( self.filePicker, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Locate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer31.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer1.Add( bSizer31, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.T_BestSize = wx.StaticText( self, wx.ID_ANY, u"000 X 000", wx.DefaultPosition, wx.Size( 80,40 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.T_BestSize.Wrap( -1 )

		bSizer4.Add( self.T_BestSize, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Best size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer4.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.T_Length = wx.StaticText( self, wx.ID_ANY, u"00:00", wx.DefaultPosition, wx.Size( 80,40 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.T_Length.Wrap( -1 )

		bSizer41.Add( self.T_Length, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		bSizer41.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer1.Add( bSizer41, 1, wx.EXPAND, 5 )

		bSizer411 = wx.BoxSizer( wx.VERTICAL )

		self.T_Tell = wx.StaticText( self, wx.ID_ANY, u"00:00", wx.DefaultPosition, wx.Size( 80,40 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.T_Tell.Wrap( -1 )

		bSizer411.Add( self.T_Tell, 0, wx.ALL, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Tell", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		bSizer411.Add( self.m_staticText511, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer1.Add( bSizer411, 1, wx.EXPAND, 5 )


		bSizer2.Add( wSizer1, 0, 0, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.gauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 600,-1 ), wx.GA_HORIZONTAL )
		self.gauge.SetValue( 0 )
		bSizer2.Add( self.gauge, 0, wx.ALL, 5 )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.m_button3, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.Timer = wx.Timer()
		self.Timer.SetOwner( self, wx.ID_ANY )
		self.Timer.Start( 100 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.S_Volume.Bind( wx.EVT_SCROLL, self.Change_Volume )
		self.filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChanged )
		self.Bind( wx.EVT_TIMER, self.TimerOnTimer, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def Change_Volume( self, event ):
		event.Skip()

	def OnFileChanged( self, event ):
		event.Skip()

	def TimerOnTimer( self, event ):
		event.Skip()


