from typing import Callable, Optional

from core.task_generators import MathTask
import wx

from . import defines



class Workspace(wx.Panel):

    def __init__(self, parent: wx.Window, header: str, task_factory: Callable) -> None:
        self.__task_factory = task_factory
        self.__current_task: Optional[MathTask] = None
        wx.Panel.__init__(self, parent, -1, size=defines.panel_size)
        self.SetBackgroundColour('white')


        self.tLabel = wx.StaticText(self, -1, header)
        self.task = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(360, 100))
        self.aLabel = wx.StaticText(self, -1, 'Ваш ответ',)
        self.answer = wx.TextCtrl(self, -1, style=wx.TE_PROCESS_ENTER, size=(200, 30))
        self.answer.Bind(wx.EVT_KEY_DOWN, self.OnKeyPress)

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


    def __generate_new_exercise(self):
        task = self.__task_factory()
        self.task.AppendText(task.expression)
        self.task.SetFocus()
