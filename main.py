import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from untitled import Ui_Form
import pythoncom
import PyHook3
import win32api
import win32con
from pathlib import Path

global keyMap
keyMap = {
    '装备栏1': '', '装备栏2': '',
    '装备栏3': '', '装备栏4': '',
    '装备栏5': '', '装备栏6': '',
}
data = []
flag = 0
class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)
        global data
        cfg = Path("./config.ini")
        if cfg.exists():        #如果config文件存在
            for line in open("config.ini", "r"):  # 设置文件对象并读取每一行文件
                line=line[:-1] #删除末尾换行符
                data.append(line)  # 将每一行文件加入到list中
            if len(data)==6:  #如果数据是完整的 读入数据
                self.text1.setText(data[0])
                self.text2.setText(data[1])
                self.text3.setText(data[2])
                self.text4.setText(data[3])
                self.text5.setText(data[4])
                self.text6.setText(data[5])

        self.mythread = MyThread()  # 实例化自己建立的任务线程类
        self.mythread.signal.connect(self.RUN_click)  # 设置任务线程发射信号触发的函数

    def RUN_click(self):
        global keyMap
        global flag
        keyMap[0] = self.text1.text()
        keyMap[1] = self.text2.text()
        keyMap[2] = self.text3.text()
        keyMap[3] = self.text4.text()
        keyMap[4] = self.text5.text()
        keyMap[5] = self.text6.text()

        f = open("config.ini", "w+")    #写入config文件存档
        for i in range(0,6):
            f.write(keyMap[i])
            f.write("\n")
        f.close()

        if flag==0:
            flag=1
            self.pushButton.setText("Listening")
            self.mythread.start()
        else:
            flag=0
            self.pushButton.setText("RUN")

    def Save_click(self):
        return


class MyThread(QThread): # 建立一个任务线程类
    signal = pyqtSignal(str) #设置触发信号传递的参数数据类型,这里是字符串
    def __init__(self):
        super(MyThread, self).__init__()

    def onKeyboardEvent(self,event):
        global keyMap
        global flag
        listK=[keyMap[0],keyMap[1],keyMap[2],keyMap[3],keyMap[4],keyMap[5]]
        if flag==1:
            if str(event.Key).lower() == listK[0].lower():
                win32api.keybd_event(103, 0, 0, 0)  # 对应小键盘7
                win32api.keybd_event(103, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(8, 0, 0, 0)  # 对应backspace删除映射输出
                win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif str(event.Key).lower() == keyMap[2].lower():
                win32api.keybd_event(100, 0, 0, 0)  # 对应小键盘4
                win32api.keybd_event(100, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(8, 0, 0, 0)  # 对应backspace删除映射输出
                win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif str(event.Key).lower() == keyMap[4].lower():
                win32api.keybd_event(97, 0, 0, 0)  # 对应小键盘1
                win32api.keybd_event(97, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(8, 0, 0, 0)  # 对应backspace删除映射输出
                win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif str(event.Key).lower() == keyMap[1].lower():
                win32api.keybd_event(104, 0, 0, 0)  # 对应小键盘8
                win32api.keybd_event(104, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(8, 0, 0, 0)  # 对应backspace删除映射输出
                win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif str(event.Key).lower() == keyMap[3].lower():
                win32api.keybd_event(101, 0, 0, 0)  # 对应小键盘5
                win32api.keybd_event(101, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(8, 0, 0, 0)  # 对应backspace删除映射输出
                win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif str(event.Key).lower() == keyMap[5].lower():
                win32api.keybd_event(98, 0, 0, 0)  # 对应小键盘2
                win32api.keybd_event(98, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(8, 0, 0, 0)  # 对应backspace删除映射输出
                win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
        else:
            pass
        return True

    def run(self): # 在启动线程后任务从这个函数里面开始执行
            # 创建一个“钩子”管理对象
        hm = PyHook3.HookManager()
            # 监听所有键盘事件
        hm.KeyDown = self.onKeyboardEvent
            # 设置键盘“钩子”
        hm.HookKeyboard()
            # 进入循环，如不手动关闭，程序将一直处于监听状态
        pythoncom.PumpMessages()





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())