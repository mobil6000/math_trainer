import winsound

from core.session import make_report
import wx


from . import defines



class ReportDialog(wx.Dialog):

    def __init__(self, parent: wx.Window, title: str, report: str) -> None:
        wx.Dialog.__init__(self, parent, -1, title, size=defines.main_win_size)

        text_ctrl_style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2
        self.text = wx.TextCtrl(self, -1, style=text_ctrl_style, size=(680, 150))
        self.text.AppendText(report)
        self.text.SetInsertionPoint(0)
        self.btClose = wx.Button(self, -1, 'Закрыть отчёт', size=(70, 70))
        self.btClose.Bind(wx.EVT_BUTTON, self.on_close)

        self.buttonSizer = wx.StdDialogButtonSizer()
        self.buttonSizer.AddButton(self.btClose)
        self.buttonSizer.Realize()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.text, 0, wx.ALL, 5)
        self.sizer.Add(self.buttonSizer, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(self.sizer)
        self.sizer.Fit(self)


    def on_close(self, event):
        self.Destroy()



class Workspace(wx.Panel):

    def __init__(self, parent: wx.Window, header: str, session_object) -> None:
        self.__session = session_object
        wx.Panel.__init__(self, parent, -1, size=defines.panel_size)
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


    def OnKeyPress(self, event):
        if event.GetKeyCode() == wx.WXK_TAB:
            self.task.SetFocus()
        else:
            event.Skip()


    def on_text_enter(self, event):
        if self.answer.GetValue() == '':
            pass
        result = self.__session.check_task_result(self.answer.GetValue())
        self.__react_to_result(result)
        self.answer.Clear()
        self.task.Clear()
        self.__generate_new_exercise()


    def on_close(self, event):
        report = make_report(self.__session.results)
        dialog = ReportDialog(self, 'flf', report)
        dialog.ShowModal()
        self.Destroy()


    def __generate_new_exercise(self):
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
