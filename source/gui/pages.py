import wx
from . import defines



class TeacherMainPage(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent, -1, size = defines.main_win_size)
		self.SetBackgroundColour('white')
		self.titles = ['Дата', 'Количество заданий', 'Статус']
		self.rows = [
			['23.11.2014', '6', 'выполнено'], 
			['23.02.2014', '50', 'в процессе'], 
			['12.11.2012', '8', 'выполнено'],
		]


		self.popupmenu = wx.Menu()
		for text in defines.teacher_context_menu:
			item = self.popupmenu.Append(-1, text)
			self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)


		self.list = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER|wx.LC_HRULES|wx.LC_VRULES, size = (900, 160))
		self.init_list_control()
		self.list.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)
		self.button = wx.Button(self, -1, 'Добавить карточку', size = (180, 100))
		self.button.SetDefault()

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add(self.list, proportion = 1, flag = wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, border = 10)
		mainSizer.Add(self.button, proportion = 0, flag = wx.ALL|wx.CENTER, border = 5)
		self.SetSizer(mainSizer)
		self.Layout()


	def init_list_control(self):
		for text in self.titles:
			self.list.AppendColumn(text, wx.LIST_FORMAT_CENTRE, width = 300)

		for row in self.rows: 
			self.list.Append(row)


	def OnShowPopup(self, event):
		pos = event.GetPosition()
		position = self.ScreenToClient(pos)
		self.PopupMenu(self.popupmenu, position)


	def OnPopupItemSelected(self, event):
		item = self.popupmenu.FindItemById(event.GetId())
		text = item.GetText()
		wx.MessageBox("You selected item '%s'" % text)
