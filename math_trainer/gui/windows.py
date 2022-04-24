from typing import Final as Constant
from typing import final
import winsound

from core import ArithmeticTask, QuadraticEquationTask, TrainingSession
from core.session import make_report
import wx

from .ui_helpers import create_menu, ReportDialog, use_selection_dialog



main_win_size: Constant = (980, 670)
panel_size: Constant = (main_win_size[0] - 20, main_win_size[1] - 30)



@final
class Workspace(wx.Panel):

    def __init__(self, parent: wx.Window, header: str, session_object) -> None:
        self.__session = session_object
        wx.Panel.__init__(self, parent, -1, size=panel_size)
        self.SetBackgroundColour('white')
        self.Bind(wx.EVT_CLOSE, self.on_close)

        self.tLabel = wx.StaticText(self, -1, header)
        self.task = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(360, 100))
        self.aLabel = wx.StaticText(self, -1, 'Ваш ответ',)
        self.answer = wx.TextCtrl(self, -1, style=wx.TE_PROCESS_ENTER, size=(200, 30))
        self.answer.Bind(wx.EVT_KEY_DOWN, self.OnKeyPress)
        self.answer.Bind(wx.EVT_TEXT_ENTER, self.on_text_enter)

        self.sizer = wx.FlexGridSizer(rows=2, cols=2, hgap=6, vgap=6)
        self.sizer.Add(self.tLabel, 0, wx.ALIGN_RIGHT)
        self.sizer.Add(self.task, 0, wx.EXPAND)
        self.sizer.Add(self.aLabel, 0, wx.ALIGN_RIGHT)
        self.sizer.Add(self.answer, 0, wx.EXPAND)
        self.sizer.AddGrowableCol(1)
        self.SetSizer(self.sizer)
        self.Layout()
        self.__generate_new_exercise()


    def OnKeyPress(self, event: wx.Event) -> None:
        if event.GetKeyCode() == wx.WXK_TAB:
            self.task.SetFocus()
        else:
            event.Skip()


    def on_text_enter(self, event: wx.Event) -> None:
        if self.answer.GetValue() == '':
            pass
        result = self.__session.check_task_result(self.answer.GetValue())
        self.__react_to_result(result)
        self.answer.Clear()
        self.task.Clear()
        self.__generate_new_exercise()


    def on_close(self, event: wx.Event) -> None:
        report = make_report(self.__session.results)
        dialog = ReportDialog(self, main_win_size, 'flf', report)
        dialog.ShowModal()
        self.Destroy()


    def __generate_new_exercise(self) -> None:
        try:
            expression = self.__session.generate_task()
        except StopIteration:
            self.Close()
            return
        self.task.AppendText(expression)
        self.task.SetFocus()


    def __react_to_result(self, flag: bool) -> None:
        if flag:
            winsound.PlaySound('math_trainer/sounds/rightAnswer.wav', winsound.SND_ASYNC)
        else:
            winsound.PlaySound('math_trainer/sounds/wrongAnswer.wav', winsound.SND_ASYNC)



@final
class MainFrame(wx.Frame):

    def __init__(self, title: str) -> None:
        wx.Frame.__init__(self, None, -1, title, main_win_size)
        self.Centre(direction=wx.BOTH)
        self.init_statusBar()
        self.init_menubar()


    def init_statusBar(self) -> None:
        self.statusBar = self.CreateStatusBar()
        self.statusBar.SetStatusWidths([-3])


    def init_menubar(self) -> None:
        self.menuBar = wx.MenuBar()
        menu = create_menu(self)
        self.menuBar.Append(menu, 'Главное меню')
        self.SetMenuBar(self.menuBar)


    def on_click_menu_for_arithmetic(self, event: wx.Event) -> None:
        title = 'Выберете тип чисел:'
        number_type_choices = ('integer', 'decimal')
        selection = use_selection_dialog(self, title, ('Целые числа', 'Десятичные дроби'))
        if selection is not None:
            params = {'numberType': number_type_choices[selection]}
            session = TrainingSession(ArithmeticTask, params)
        else:
            session = TrainingSession(ArithmeticTask)
        Workspace(self, 'Вычислите арифметическое выражение:', session)


    def on_click_menu_for_equation(self, event: wx.Event) -> None:
        session = TrainingSession(QuadraticEquationTask)
        Workspace(self, 'Решите квадратное уравнение:', session)
