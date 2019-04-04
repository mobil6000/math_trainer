import wx
from gui import MainFrame2



class Application(wx.App):

	def OnInit(self):
		self.app_local = wx.Locale()
		self.app_local.Init(wx.LANGUAGE_RUSSIAN)
		self.main_window = MainFrame2('заголовок2')
		self.SetTopWindow(self.main_window)
		self.main_window.Show()
		return True



if __name__ == '__main__':  
	teacher = Application()
	teacher.MainLoop()
