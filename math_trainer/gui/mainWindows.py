import wx

from . import defines
from . import uiHelper



class MainFrame1(wx.Frame):

    def __init__(self, title: str) -> None:
        wx.Frame.__init__(self, None, -1, title, defines.main_win_size)
        self.Centre(direction=wx.BOTH)
        self.initStatusBar()
        self.menuBar = wx.MenuBar()
        menu = uiHelper.create_menu(None, defines.main_menu)
        self.menuBar.Append(menu, 'Главное меню')
        self.SetMenuBar(self.menuBar)


    def initStatusBar(self) -> None:
        self.statusBar = self.CreateStatusBar()
        self.statusBar.SetStatusWidths([-3])
