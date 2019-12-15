import wx
from . import defines
from .pages import *
from . import uiHelper



class MainFrame1(wx.Frame):

	def __init__(self, title):
		wx.Frame.__init__(self, None, -1, title, defines.main_win_size)
		self.Centre(direction=wx.BOTH)
		self.initStatusBar()
		self.menuBar = wx.MenuBar()
		menu = uiHelper.create_menu(None, defines.main_menu)
		self.menuBar.Append(menu, 'Главное меню')
		self.SetMenuBar(self.menuBar)

		self.panel = StudentPage(self)


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
		self.report_page = ReportPage(self)
		self.report_page.Hide()


	#interface: 
	def initStatusBar(self):
		self.statusBar = self.CreateStatusBar()
		self.statusBar.SetStatusWidths([-3])


	def SwitchPanel(self):
		if self.panel.IsShown():
			self.panel.Hide()
			self.report_page.Show()
			self.report_page.html.SetFocus()
		else:
			self.report_page.Hide()
			self.panel.Show()
			self.panel.SetFocus()
		print('\a')



class MainFrame3(wx.Frame):

	def __init__(self, title):
		wx.Frame.__init__(self, None, -1, title, defines.main_win_size)
		self.Centre(direction=wx.BOTH)
		self.initStatusBar()

		text = '''вы выполнили 20 заданий, 
у вас 14 правильных ответов, 
на выполнения всех заданий вы потратили 139 секунд, 
в среднем на выполнение каждого задания вы потратили около 10 секунд. '''
		self.window = uiHelper.ReportDialog(self, 'Ваши результаты', text)
		self.window.ShowModal()


	#interface: 
	def initStatusBar(self):
		self.statusBar = self.CreateStatusBar()
		self.statusBar.SetStatusWidths([-3])



class MainFrame4(wx.Frame):

	def __init__(self, title):
		wx.Frame.__init__(self, None, -1, title, defines.main_win_size)
		self.Centre(direction=wx.BOTH)
		self.initStatusBar()
		self.menuBar = wx.MenuBar()
		menu = uiHelper.create_menu(None, defines.main_menu)
		self.menuBar.Append(menu, 'Главное меню')
		self.SetMenuBar(self.menuBar)

		header = 'выполнить арифметическое выражение'
		text = ' 21 -3 +(18 ÷ 6) ='
		self.panel = Workspace1(self, header, text)


	#interface: 
	def initStatusBar(self):
		self.statusBar = self.CreateStatusBar()
		self.statusBar.SetStatusWidths([-3])

