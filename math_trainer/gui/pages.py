from typing import Callable, Optional

from core.task_generators import MathTask
import wx

from . import defines



class Workspace(wx.Panel):

    def __init__(self, parent: wx.Window, header: str, session_object) -> None:
        self.__session = session_object
        wx.Panel.__init__(self, parent, -1, size=defines.panel_size)
        self.SetBackgroundColour('white')


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
        self.answer.Clear()
        self.task.Clear()
        self.__generate_new_exercise()


    def __generate_new_exercise(self):
        expression = next(self.__session.generate_task())
        self.task.AppendText(expression)
        self.task.SetFocus()

