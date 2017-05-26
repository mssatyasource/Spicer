import os
from LogiDialog import LoginDialog
import wx
import bootstarp
from DockerHub import DockerHub





def validateLoginDialog():
    try:
        dlg = LoginDialog()
        #dlg.Show()
        dlg.ShowModal()
    except Exception as Error:
        print(str(Error))


def CheckDockerLogin():
    d = DockerHub()
    d.Login('mssatya','4Getme2')












if __name__ == '__main__':
    bootstarp.InitalizeApplication()
    app = wx.App()
    app.MainLoop()
    CheckDockerLogin()
    #validateLoginDialog()