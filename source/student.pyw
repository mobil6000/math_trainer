import wx
from gui import MainFrame1



class Application(wx.App):

	def OnInit(self):
		self.app_local = wx.Locale()
		self.app_local.Init(wx.LANGUAGE_RUSSIAN)
		self.main_window = MainFrame1('заголовок1')
		self.SetTopWindow(self.main_window)
		self.main_window.Show()
		return True



if __name__ == '__main__':  
	student = Application()
	student.MainLoop()
