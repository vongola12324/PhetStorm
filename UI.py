from tkinter import *


class window:
    def __init__(self, Title="PhetStorm", Width=600, Height=800, resizeable=False, staFunc=bool, stoFunc=bool):
        self.width = Width
        self.height = Height
        self.title = Title
        self.resizeable = resizeable
        self.staFunc = staFunc
        self.stpFunc = stoFunc

        self.root = Tk(className=Title)

    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws / 2) - (self.height / 2))
        y = int((hs / 2) - (self.width/ 2))
        self.root.geometry('{}x{}+{}+{}'.format(self.height, self.width, x, y))

    def loop(self):
        # 禁止修改窗口大小
        self.root.resizable(False, False)
        # 窗口置中
        self.center()
        self.root.mainloop()