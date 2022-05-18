from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("400x300+20+10")

window.grid_columnconfigure(0, weight=1)

class MyWindow:
    def __init__(self,window):
        self.lbl1 = Label(window, text="Standard Calculator")
        self.lbl1.grid(row = 0, columnspan = 5, pady = (5, 10))
        self.lbl2 = Label(window, text="Enter the 1st Number:")
        self.lbl2.grid(row = 1, column = 2)
        self.lbl3 = Label(window, text="Enter the 2nd Number:")
        self.lbl3.grid(row = 2, column = 2)

        self.txt1 = Entry(window, bd = 3)
        self.txt1.grid(row = 1, column = 3)
        self.txt2 = Entry(window, bd = 3)
        self.txt2.grid(row = 2, column = 3)

        self.btn1 = Button(window, text = "Addition", command = self.add)
        self.btn1.grid(row = 4, column = 1, pady = 20)
        self.btn2 = Button(window, text = "Subtraction", command = self.sub)
        self.btn2.grid(row = 4, column = 2, padx = (30, 15))
        self.btn3 = Button(window, text = "Multiplication", command = self.mul)
        self.btn3.grid(row = 4, column = 3)
        self.btn4 = Button(window, text = "Division", command = self.div)
        self.btn4.grid(row = 4, column = 4, padx = 15)

        self.lbl4 = Label(window, text="Result: ")
        self.lbl4.grid(row=5, column=2)

        self.txt3 = Entry(window, state="readonly")
        self.txt3.grid(row=5, column=3)

        self.btn_clr = Button(window, text="Clear", command = self.btnclr)
        self.btn_clr.grid(row=13, column=3, pady=5)

    def add(self):
        self.txt3.configure(state="normal")
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        ans = num1 + num2
        self.txt3.delete(0, END)
        self.txt3.insert(END, str(ans))
        self.txt3.configure(state="disabled")
        return

    def sub(self):
        self.txt3.configure(state="normal")
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        ans = num1 - num2
        self.txt3.delete(0, END)
        self.txt3.insert(END, str(ans))
        self.txt3.configure(state="disabled")
        return

    def mul(self):
        self.txt3.configure(state="normal")
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        ans = num1 * num2
        self.txt3.delete(0, END)
        self.txt3.insert(END, str(ans))
        self.txt3.configure(state="disabled")
        return

    def div(self):
        self.txt3.configure(state="normal")
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        ans = num1 / num2
        self.txt3.delete(0, END)
        self.txt3.insert(END, str(ans))
        self.txt3.configure(state="disabled")
        return

    def btnclr(self):
        self.txt3.configure(state="normal")
        self.txt3.delete(0, END)
        self.txt3.configure(state="disabled")
        return

mywin = MyWindow(window)

window.mainloop()