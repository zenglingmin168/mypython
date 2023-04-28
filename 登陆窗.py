#coding: utf-8
import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title='用户登陆',size=(400,200))

if __name__ == '__main__':
    app=wx.App()
    frame=MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()