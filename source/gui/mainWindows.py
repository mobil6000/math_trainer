import wx
from . import defines
from .pages import *



class MainFrame1(wx.Frame):

	def __init__(self, title):
		wx.Frame.__init__(self, None, -1, title, defines.main_win_size)
		self.Centre(direction=wx.BOTH)
		self.initStatusBar()


	#interface: 
	def initStatusBar(self):
		self.statusBar = self.CreateStatusBar()
		self.statusBar.SetStatusWidths([-3])



class MainFrame2(wx.Frame):

	def __init__(self, title):
		wx.Frame.__init__(self, None, -1, title, defines.main_win_size)
		self.Centre(direction=wx.BOTH)
		self.initStatusBar()
		self.panel = TeacherMainPage(self)


	#interface: 
	def initStatusBar(self):
		self.statusBar = self.CreateStatusBar()
		self.statusBar.SetStatusWidths([-3])
