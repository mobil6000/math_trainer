from core import ArithmeticTask, QuadraticEquationTask, TrainingSession
import wx

from . import defines
from . import pages
from . import uiHelper



class MainFrame1(wx.Frame):

    def __init__(self, title: str) -> None:
        wx.Frame.__init__(self, None, -1, title, defines.main_win_size)
        self.Centre(direction=wx.BOTH)
        self.init_statusBar()
        self.init_menubar()


    def init_statusBar(self) -> None:
        self.statusBar = self.CreateStatusBar()
        self.statusBar.SetStatusWidths([-3])


    def init_menubar(self) -> None:
        self.menuBar = wx.MenuBar()
        menu = uiHelper.create_menu(self, defines.main_menu)
        self.menuBar.Append(menu, 'Главное меню')
        self.SetMenuBar(self.menuBar)


    def on_click_menu_for_arithmetic(self, event):
        title = 'Выберете тип чисел:'
        number_type_choices = ('integer', 'decimal')
        selection = uiHelper.use_selection_dialog(self, title, ('Целые числа', 'Десятичные дроби'))
        if selection is not None:
            params = {'numberType': number_type_choices[int(selection)]}
            session = TrainingSession(ArithmeticTask, params)
        else:
            session = TrainingSession(ArithmeticTask)
        pages.Workspace(self, 'Вычислите арифметическое выражение:', session)


    def on_click_menu_for_equation(self, event):
        session = TrainingSession(QuadraticEquationTask)
        pages.Workspace(self, 'Решите квадратное уравнение:', session)
