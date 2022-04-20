import gui
import wx



class Application(wx.App):

    def OnInit(self) -> bool:
        self.app_local = wx.Locale()
        self.app_local.Init(wx.LANGUAGE_RUSSIAN)
        self.main_window = gui.MainFrame1('Тренажёр')
        self.SetTopWindow(self.main_window)
        self.main_window.Show()
        return True



if __name__ == '__main__':
    student = Application()
    student.MainLoop()
