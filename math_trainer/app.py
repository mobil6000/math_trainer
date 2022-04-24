from typing import final
import winsound

import gui
import wx



@final
class Application(wx.App):

    def OnInit(self) -> bool:
        winsound.PlaySound('math_trainer/sounds/run.wav', winsound.SND_ASYNC)
        self.app_local = wx.Locale()
        self.app_local.Init(wx.LANGUAGE_RUSSIAN)
        self.main_window = gui.MainFrame('Математический тренажёр')
        self.SetTopWindow(self.main_window)
        self.main_window.Show()
        return True



if __name__ == '__main__':
    app = Application()
    app.MainLoop()
