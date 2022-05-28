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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"wxPython_WallpaperEngine_Manager", pos = wx.DefaultPosition, size = wx.Size( 730,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.NoteBook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.A = wx.Panel( self.NoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.A_B_File = wx.Button( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,35 ), wx.BORDER_NONE )
		self.A_B_File.SetBackgroundColour( wx.Colour( 192, 192, 192 ) )

		wSizer3.Add( self.A_B_File, 0, wx.RIGHT|wx.LEFT, 5 )

		self.A_B_Foler = wx.Button( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,35 ), wx.BORDER_NONE )
		self.A_B_Foler.SetBackgroundColour( wx.Colour( 192, 192, 192 ) )
		self.A_B_Foler.Enable( False )

		wSizer3.Add( self.A_B_Foler, 0, wx.RIGHT|wx.LEFT, 5 )

		self.A_B_Refresh = wx.Button( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,35 ), wx.BORDER_NONE )
		self.A_B_Refresh.SetBackgroundColour( wx.Colour( 192, 192, 192 ) )

		wSizer3.Add( self.A_B_Refresh, 0, wx.RIGHT|wx.LEFT, 5 )

		self.T_Analysis_Text = wx.StaticText( self.A, wx.ID_ANY, u">>>000X.xxx || 000%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_Analysis_Text.Wrap( -1 )

		wSizer3.Add( self.T_Analysis_Text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer10.Add( wSizer3, 0, 0, 5 )

		self.Guage = wx.Gauge( self.A, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 700,5 ), wx.GA_HORIZONTAL )
		self.Guage.SetValue( 0 )
		bSizer10.Add( self.Guage, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		wSizer31 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.A_Thumbnail_ListCtrl = wx.ListCtrl( self.A, wx.ID_ANY, wx.DefaultPosition, wx.Size( 570,400 ), wx.LC_ICON )
		wSizer31.Add( self.A_Thumbnail_ListCtrl, 0, wx.ALL, 5 )

		A_PlayListChoices = []
		self.A_PlayList = wx.ListBox( self.A, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,400 ), A_PlayListChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.LB_SINGLE )
		wSizer31.Add( self.A_PlayList, 0, wx.ALL, 5 )


		bSizer10.Add( wSizer31, 1, wx.EXPAND, 5 )


		self.A.SetSizer( bSizer10 )
		self.A.Layout()
		bSizer10.Fit( self.A )
		self.NoteBook.AddPage( self.A, u"资源", False )
		self.B = wx.Panel( self.NoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.S_Volume = wx.Slider( self.B, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,40 ), wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		bSizer3.Add( self.S_Volume, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText2 = wx.StaticText( self.B, wx.ID_ANY, u"Volume", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer1.Add( bSizer3, 0, 0, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.T_Size = wx.StaticText( self.B, wx.ID_ANY, u"000,000", wx.DefaultPosition, wx.Size( 80,40 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.T_Size.Wrap( -1 )

		bSizer4.Add( self.T_Size, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self.B, wx.ID_ANY, u"分辨率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer4.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.T_Length = wx.StaticText( self.B, wx.ID_ANY, u"000F", wx.DefaultPosition, wx.Size( 80,40 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.T_Length.Wrap( -1 )

		bSizer41.Add( self.T_Length, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self.B, wx.ID_ANY, u"帧总数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		bSizer41.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer1.Add( bSizer41, 1, wx.EXPAND, 5 )

		bSizer411 = wx.BoxSizer( wx.VERTICAL )

		self.T_Tell = wx.StaticText( self.B, wx.ID_ANY, u"000F", wx.DefaultPosition, wx.Size( 80,40 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.T_Tell.Wrap( -1 )

		bSizer411.Add( self.T_Tell, 0, wx.ALL, 5 )

		self.m_staticText511 = wx.StaticText( self.B, wx.ID_ANY, u"当前播放帧", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		bSizer411.Add( self.m_staticText511, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer1.Add( bSizer411, 1, wx.EXPAND, 5 )

		bSizer412 = wx.BoxSizer( wx.VERTICAL )

		self.T_FPS = wx.StaticText( self.B, wx.ID_ANY, u"25F/S\n25(t)F/S", wx.DefaultPosition, wx.Size( 80,40 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.T_FPS.Wrap( -1 )

		bSizer412.Add( self.T_FPS, 0, wx.ALL, 5 )

		self.m_staticText512 = wx.StaticText( self.B, wx.ID_ANY, u"帧率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText512.Wrap( -1 )

		bSizer412.Add( self.m_staticText512, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer1.Add( bSizer412, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.S_Rate = wx.Slider( self.B, wx.ID_ANY, 100, 25, 200, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		bSizer12.Add( self.S_Rate, 0, wx.ALL, 5 )

		self.T_Rate = wx.StaticText( self.B, wx.ID_ANY, u"播放速率", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.T_Rate.Wrap( -1 )

		bSizer12.Add( self.T_Rate, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer1.Add( bSizer12, 1, wx.EXPAND, 5 )


		bSizer8.Add( wSizer1, 0, 0, 5 )

		self.m_staticline3 = wx.StaticLine( self.B, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer8.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.UpOne = wx.Button( self.B, wx.ID_ANY, u"◀", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.UpOne, 0, wx.ALL, 5 )

		self.PS_Control = wx.Button( self.B, wx.ID_ANY, u"▶", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.PS_Control, 0, wx.ALL, 5 )

		self.DownOne = wx.Button( self.B, wx.ID_ANY, u"▶", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.DownOne, 0, wx.ALL, 5 )


		bSizer8.Add( wSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.B_Tell_Control = wx.Slider( self.B, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.Size( 700,-1 ), wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_LABELS )
		self.B_Tell_Control.Enable( False )

		bSizer8.Add( self.B_Tell_Control, 0, wx.ALL, 5 )


		self.B.SetSizer( bSizer8 )
		self.B.Layout()
		bSizer8.Fit( self.B )
		self.NoteBook.AddPage( self.B, u"控制", True )

		bSizer2.Add( self.NoteBook, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.Timer = wx.Timer()
		self.Timer.SetOwner( self, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Bind( wx.EVT_SIZE, self.MainOnSize )
		self.A_B_File.Bind( wx.EVT_BUTTON, self.Select_File )
		self.A_B_Refresh.Bind( wx.EVT_BUTTON, self.Thumbnail_Refresh )
		self.A_Thumbnail_ListCtrl.Bind( wx.EVT_LIST_BEGIN_DRAG, self.A_Thumbnail_ListCtrlOnListBeginDrag )
		self.A_Thumbnail_ListCtrl.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.A_Thumbnail_ListCtrlOnListItemActivated )
		self.S_Volume.Bind( wx.EVT_SCROLL, self.Change_Volume )
		self.S_Rate.Bind( wx.EVT_SCROLL, self.Change_Rate )
		self.T_Rate.Bind( wx.EVT_LEFT_DCLICK, self.T_RateOnLeftDClick )
		self.PS_Control.Bind( wx.EVT_BUTTON, self.PorS )
		self.B_Tell_Control.Bind( wx.EVT_SCROLL, self.B_Tell_ControlOnScroll )
		self.B_Tell_Control.Bind( wx.EVT_SCROLL_CHANGED, self.B_Tell_ControlOnScrollChanged )
		self.Bind( wx.EVT_TIMER, self.Time_Tick, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def MainOnSize( self, event ):
		event.Skip()

	def Select_File( self, event ):
		event.Skip()

	def Thumbnail_Refresh( self, event ):
		event.Skip()

	def A_Thumbnail_ListCtrlOnListBeginDrag( self, event ):
		event.Skip()

	def A_Thumbnail_ListCtrlOnListItemActivated( self, event ):
		event.Skip()

	def Change_Volume( self, event ):
		event.Skip()

	def Change_Rate( self, event ):
		event.Skip()

	def T_RateOnLeftDClick( self, event ):
		event.Skip()

	def PorS( self, event ):
		event.Skip()

	def B_Tell_ControlOnScroll( self, event ):
		event.Skip()

	def B_Tell_ControlOnScrollChanged( self, event ):
		event.Skip()

	def Time_Tick( self, event ):
		event.Skip()


