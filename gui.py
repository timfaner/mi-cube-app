import tkinter as tk  # 使用Tkinter前需要先导入

class Gui():
    def __init__(self):
        self.window = tk.Tk()

        self.window.title('Cube Password')

        self.window.geometry('1500x400')

        self.lable = tk.Label(self.window, text="转动魔方以生成密码", fg = '#ffffff',bg='#5c58b6', font=('Arial', 120), width=30, height=20)

        self.lable.pack() 

    def start(self):
        self.window.mainloop()

    def updatetext(self,text):
        self.lable['text'] = text

def startgui():
    gui = Gui()

    gui.start()


if __name__ == "__main__":
    startgui()