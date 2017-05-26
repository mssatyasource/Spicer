import wx


class LoginDialog(wx.Frame):
    def __init__(self, parent=None, title='Enter username password', size=(300, 300)):
        #super(LoginDialog, self).__init__(parent, title=title, size=(250, 150))
        #wx.Dialog.__init__(self, None, title='abcd', size=(300,300))
        wx.Frame.__init__(self, None, -1, 'Run ATE Manual mode', size=(400, 400))
        wx.Panel = wx.Panel(self)
        self.lbUserName = wx.StaticText(self.panel, label="UserId")
        self.tbUserName = wx.TextCtrl(self.panel, size=(400, -1))
        self.lbPassword = wx.StaticText(self.panel, label="Password")
        self.tbPassword = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD, size=(400, -1))
        self.btnLogin = wx.Button(self.panel, label="Login")
        self.Bind(wx.EVT_BUTTON, self.OnClickLogin, self.btnLogin)
        self.btnCancel = wx.Button(self.panel, label="Cancel")
        self.Bind(wx.EVT_BUTTON, self.OnClickCancel, self.btnCancel)

        # UI alignment
        gridXMax = 3
        gridYMax = 2
        gridIndex = 1

        # window sizer
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)
        self.sizer = wx.GridBagSizer(gridXMax, gridYMax)
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)
        # Use the sizers
        self.panel.SetSizerAndFit(self.border)

        self.sizer.Add(self.lbUserName, (gridIndex, 0))
        self.sizer.Add(self.tbUserName, (gridIndex, 1))
        gridIndex = gridIndex + 1
        self.sizer.Add(self.lbPassword, (gridIndex, 0))
        self.sizer.Add(self.tbPassword, (gridIndex, 1))
        gridIndex = gridIndex + 1
        self.sizer.Add(self.btnLogin, (gridIndex, 0))

        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)
        self.panel.SetBackgroundColour(wx.Colour(221, 227, 242))
        # sizer code end221
        self.Maximize(True)

        # class varibles
        self.UserId = None
        self.Password = None
        self.Iscancelled = False

        def OnClickLogin(self, event):
            try:
                self.UserId = self.tbUserName.GetValue()
                self.Password = self.tbPassword.GetValue()
                if not self.UserId:
                    wx.MessageBox('invalid Userid')
                    return
                if not self.Password:
                    wx.MessageBox('invalid password')
                    return
                self.close()
            except Exception as Error:
                print(str(Error))

        def OnClickCancel(self, event):
            self.Iscancelled = False
            self.Close()
