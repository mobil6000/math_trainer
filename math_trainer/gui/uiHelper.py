from typing import Optional

import wx
import wx.html2 as html

from . import defines



def create_menu(parent, menu_data):
    menu = wx.Menu()
    for item in menu_data:
        menu_item = menu.Append(-1, item)
        tmp = menu_data[item]
        if tmp is not None:
            handler = getattr(parent, tmp)
            menu.Bind(wx.EVT_MENU, handler, menu_item)
    return menu


def create_html_ctrl(parent, html_file, size, context_menu=False):
    ctrl = html.WebView.New(parent)
    ctrl.EnableContextMenu(context_menu)
    with open(html_file, 'r') as f:
        content = f.read()
    ctrl.SetPage(content, '')
    return ctrl


def use_selection_dialog(
    parent: wx.Window,
    title: str,
    choices: tuple[str, ...],
    label: str=''
) -> Optional[str]:
    dialog = wx.SingleChoiceDialog(parent, label, title, choices)
    dialog.SetSelection(0)
    if dialog.ShowModal() == wx.ID_OK:
        return dialog.GetSelection()
    dialog.Destroy()
    return None



class ReportDialog(wx.Dialog):

    def __init__(self, parent, title, text):
        wx.Dialog.__init__(self, parent, -1, title, size=defines.panel_size)
        self.text = wx.TextCtrl(
            self,
            -1,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2,
            size=(680, 150)
        )
        self.text.AppendText(text)
        self.text.SetInsertionPoint(0)
        self.btClose = wx.Button(self, -1, 'Закрыть', size=(70, 70))
        self.btClose.Bind(wx.EVT_BUTTON, self.OnClose)

        self.buttonSizer = wx.StdDialogButtonSizer()
        self.buttonSizer.AddButton(self.btClose)
        self.buttonSizer.Realize()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.text, 0, wx.ALL, 5)
        self.sizer.Add(self.buttonSizer, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(self.sizer)
        self.sizer.Fit(self)


    def OnClose(self, event):
        self.Destroy()
