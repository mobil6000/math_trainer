import wx
import wx.html2 as html



def create_menu(parent, menuData):
	menu = wx.Menu()
	for item in menuData:
		menu_item = menu.Append(-1, item)
		handler = getattr(parent, menuData[item])
		menu.Bind(wx.EVT_MENU, handler, menu_item)
	return menu


def create_html_ctrl(parent, html_file, size, context_menu = False):
	ctrl = html.WebView.New(parent, size)
	ctrl.EnableContextMenu(context_menu)
	with open(html_file, 'r') as f:
		content = f.read()
	ctrl.SetPage(content, '')
	return ctrl
