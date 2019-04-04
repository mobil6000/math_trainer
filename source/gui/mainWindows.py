import wx
from . import defines



class MainFrame1(wx.Frame):

	def __init__(self, title):
		wx.Frame.__init__(self, None, -1, title, defines.main_win_size)
		self.Centre(direction=wx.BOTH)
		self.initStatusBar()


	#interface: 
	def initStatusBar(self):
		self.statusBar = self.CreateStatusBar()
		self.statusBar.SetFieldsCount(3)
		self.statusBar.SetStatusWidths([-1, -2, -3])



class MainFrame2(wx.Frame):

	def __init__(self, title):
		wx.Frame.__init__(self, None, -1, title, defines.main_win_size)
		self.Centre(direction=wx.BOTH)
		self.initStatusBar()


	#interface: 
	def initStatusBar(self):
		self.statusBar = self.CreateStatusBar()
		self.statusBar.SetFieldsCount(3)
		self.statusBar.SetStatusWidths([-1, -2, -3])
