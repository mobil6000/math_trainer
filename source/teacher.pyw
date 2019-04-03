import wx



class Application(wx.App):

	def OnInit(self):
		self.app_local = wx.Locale()
		self.app_local.Init(wx.LANGUAGE_RUSSIAN)
		return True



if __name__ == '__main__':  
	student = Application()
	student.MainLoop()
