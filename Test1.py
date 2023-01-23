#coding:utf-8
 
import sys
import threading
import time
 
import wx
from wx.lib.pubsub import pub
 
class MyWindow():
 
    def __init__(self):
        self.app = None
        self.frame = None
        self.logObj = None
        self.main()
 
    def main(self):
        self.app = wx.App()
        self.frame = wx.Frame(None, -1, title='线程安全测试', size=wx.Size(1100, 700))
        self.createMainPanel()
 
    def show(self):
        self.frame.Show()
        self.app.MainLoop()
 
    def createMainPanel(self):
        mainPanel = wx.Panel(self.frame)
        startButton = wx.Button(mainPanel, label="启动", pos=(5, 5))
        openLogButton = wx.Button(mainPanel, label="开启日志", pos=(95, 5))
        closeLogButton = wx.Button(mainPanel, label="关闭日志", pos=(180, 5))
 
        self.logTextCtr = wx.TextCtrl(mainPanel, size=wx.Size(1000, 500), pos=(5,50),style=wx.TE_MULTILINE)
 
        self.frame.Bind(wx.EVT_BUTTON, lambda evt, textArea=self.logTextCtr: self.startBut(evt,self.logTextCtr),
                        startButton)
        self.frame.Bind(wx.EVT_BUTTON, lambda evt: self.startLog(evt),
                        openLogButton)
        self.frame.Bind(wx.EVT_BUTTON, lambda evt: self.closeLog(evt),
                        closeLogButton)
        pub.subscribe(self.updateDisplay, "update")
 
    def startBut(self,evt,textArea):
        self.logObj = LogPrint()
 
    def startLog(self,evt):
        threadObj = threading.Thread(target=self.dolog, args=())
        threadObj.start()
    def dolog(self):
        self.logObj.toPrint()
    def updateDisplay(self, msg):
        t = msg
        self.logTextCtr.WriteText(t + "\n")
    def closeLog(self,evt):
        self.logObj.setIsPrint(0)
 
 
class LogPrint():
    def __init__(self):
        self.isPrint = 0
 
    def toPrint(self):
        self.isPrint = 1
        i = 0
        while self.isPrint == 1:
            j = str(i) + " this is log!"
            wx.CallAfter(pub.sendMessage, "update", msg=j)
            print(j)
            i = i + 1
            time.sleep(1)
            
    def setIsPrint(self,data):
        self.isPrint = data
 
if __name__ == "__main__":
    MyWindow().show()
 