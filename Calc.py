from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.screen = Text(master, state='disabled', width=30, height=3, background="green", foreground="white")

        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.screen.configure(state='normal')

        self.equation = ''

        button1 = self.createbutton(7)
        button2 = self.createbutton(8)
        button3 = self.createbutton(9)
        button4 = self.createbutton(u"\u232B", None)
        button5 = self.createbutton(4)
        button6 = self.createbutton(5)
        button7 = self.createbutton(6)
        button8 = self.createbutton(u"\u00F7")
        button9 = self.createbutton(1)
        button10 = self.createbutton(2)
        button11 = self.createbutton(3)
        button12 = self.createbutton('*')
        button13 = self.createbutton('.')
        button14 = self.createbutton(0)
        button15 = self.createbutton('+')
        button16 = self.createbutton('-')
        button17 = self.createbutton('=', None)

        buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
                   button12, button13, button14, button15, button16, button17]

        count = 0
        for row in range(1, 5):
            for column in range(4):
                buttons[count].grid(row=row, column=column)
                count += 1
        buttons[16].grid(row=5, column=0, columnspan=4)

    def createbutton(self, val, write=True, width=7):
        return Button(self.master, text=val, command=lambda: self.click(val, write), width=width)

    def click(self, text, write):
        if write == None:
            if text == '=' and self.equation:
                self.equation = re.sub(u"\u00F7", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline=True)
            elif text == u"\u232B":
                self.clear_screen()

        else:
            self.insert_screen(text)

    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END, value)
        self.equation += str(value)
        self.screen.configure(state='disabled')


root = Tk()
my_gui = Calculator(root)
root.mainloop()