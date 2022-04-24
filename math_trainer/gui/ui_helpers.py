from typing import Optional

import wx



main_menu_struct = {
    'Арифметика': 'on_click_menu_for_arithmetic',
    'Квадратные уровнения': 'on_click_menu_for_equation',
    'выход': None
}


def create_menu(parent: wx.Window) -> wx.Menu:
    menu = wx.Menu()
    for item in main_menu_struct:
        menu_item = menu.Append(-1, item)
        tmp = main_menu_struct[item]
        if tmp is not None:
            handler = getattr(parent, tmp)
            menu.Bind(wx.EVT_MENU, handler, menu_item)
    return menu


def use_selection_dialog(
    parent: wx.Window,
    title: str,
    choices: tuple[str, ...],
    label: str=''
) -> Optional[int]:
    dialog = wx.SingleChoiceDialog(parent, label, title, choices)
    dialog.SetSelection(0)
    if dialog.ShowModal() == wx.ID_OK:
        return dialog.GetSelection()
    dialog.Destroy()
    return None



class ReportDialog(wx.Dialog):

    def __init__(
        self,
        parent: wx.Window,
        win_size: tuple[int, int],
        title: str,
        report: str
    ) -> None:
        wx.Dialog.__init__(self, parent, -1, title, size=win_size)

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
