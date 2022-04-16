import wx
from . import defines
from . import uiHelper



class ReportPage(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent, -1, size = defines.panel_size)
		self.SetBackgroundColour('white')
		self.parent = parent

		self.button = wx.Button(self, -1, 'Вернуться к списку карточек', size = (180, 100))
		self.button.SetDefault()
		self.button.Bind(wx.EVT_BUTTON, self.Back)

		self.html = uiHelper.create_html_ctrl(self, 'source/report.html', (700, 650))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add(self.html, proportion = 1, flag = wx.ALL|wx.EXPAND, border = 10)
		mainSizer.Add(self.button, proportion = 0, flag = wx.ALL|wx.CENTER, border = 5)
		self.SetSizer(mainSizer)
		self.Layout()


	def Back(self, event):
		self.parent.SwitchPanel()






class TeacherMainPage(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent, -1, size = defines.panel_size)
		self.SetBackgroundColour('white')
		self.__current_item = []
		self.parent = parent

		self.popup_menu = uiHelper.create_menu(self, defines.teacher_context_menu)

		self.list = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.SUNKEN_BORDER|wx.LC_HRULES|wx.LC_VRULES, size = (900, 160))
		self.init_list_control()
		self.list.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)
		self.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.ShowReport)

		self.button = wx.Button(self, -1, 'Добавить карточку', size = (180, 100))
		self.button.SetDefault()

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add(self.list, proportion = 1, flag = wx.ALL|wx.EXPAND, border = 10)
		mainSizer.Add(self.button, proportion = 0, flag = wx.ALL|wx.CENTER, border = 5)
		self.SetSizer(mainSizer)
		self.Layout()


	def init_list_control(self):
		for title in defines.table_titles:
			self.list.AppendColumn(title, wx.LIST_FORMAT_CENTRE, width = 300)
		for row in defines.table_content: 
			self.list.Append(row)


	def OnShowPopup(self, event):
		pos = event.GetPosition()
		position = self.ScreenToClient(pos)
		self.PopupMenu(self.popup_menu, position)


	def OnClearList(self, event):
		message = wx.MessageDialog(self, 'Вы действительно хотите очистить список Контрольных работ? ', 'Очистка', style = wx.YES_NO|wx.CANCEL|wx.ICON_QUESTION)
		if message.ShowModal() == wx.ID_YES:
			self.list.DeleteAllItems()


	def OnEditListItem(self, event):
		pass


	def OnDeleteListItem(self, event):
		pass

	def ShowReport(self, event):
		self.parent.SwitchPanel()


class Workspace1(wx.Panel):

	def __init__(self, parent, header, text):
		wx.Panel.__init__(self, parent, -1, size = defines.panel_size)
		self.SetBackgroundColour('white')

		self.tLabel = wx.StaticText(self, -1, header)
		self.task = wx.TextCtrl(self, -1, style = wx.TE_MULTILINE|wx.TE_READONLY, size = (360, 100))
		self.task.AppendText(text)
		self.aLabel = wx.StaticText(self, -1, 'Ваш ответ',)
		self.answer = wx.TextCtrl(self, -1, style =wx.TE_PROCESS_ENTER, size = (200, 30))
		self.answer.Bind(wx.EVT_KEY_DOWN, self.OnKeyPress)

		self.sizer = wx.FlexGridSizer(rows=2, cols=2, hgap=6, vgap=6)
		self.sizer.Add(self.tLabel, 0, wx.ALIGN_RIGHT)
		self.sizer.Add(self.task, 0, wx.EXPAND)
		self.sizer.Add(self.aLabel, 0, wx.ALIGN_RIGHT)
		self.sizer.Add(self.answer, 0, wx.EXPAND)
		self.sizer.AddGrowableCol(1)
		self.SetSizer(self.sizer)
		self.Layout()


	#event handlers:
	def OnKeyPress(self, event):
		if event.GetKeyCode() == wx.WXK_TAB:
			self.task.SetFocus()
		else:
			event.Skip()



class StudentPage(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent, -1, size = defines.panel_size)
		self.SetBackgroundColour('white')

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		btn1 = wx.Button(self, -1, 'Арифметические выражения', size = (260, 100))
		mainSizer.Add(btn1, proportion = 1, border = 10, flag = wx.EXPAND)
		btn2 = wx.Button(self, -1, 'Квадратные уравнения', size = (260, 100))
		mainSizer.Add(btn2, proportion = 1, border = 10, flag = wx.EXPAND)
		btn3 = wx.Button(self, -1, 'системы линейных уравнений', size = (260, 100))
		mainSizer.Add(btn3, proportion = 1, border = 10, flag = wx.EXPAND)
		btn4 = wx.Button(self, -1, 'переключиться в режим тестирования', size = (260, 100))
		mainSizer.Add(btn4, proportion = 0, flag = wx.ALL|wx.CENTER, border = 5)
		self.SetSizer(mainSizer)

