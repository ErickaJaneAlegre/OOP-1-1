from tkinter import *
window = Tk()

window.geometry("500x500+30+30")
window.title("Midterm in OOP")

#Add Label Widget

lbl = Label(window, text = "Enter Your Full Name:", fg = "Red")
lbl.place(x = 30, y = 150)

#Add Text Field Widget

txtfld = Entry(window, bd = 4, font = ("Arial", 16))
txtfld.place(x = 230, y = 150)

txtfld1 = Entry(window, bd = 4, font = ("Arial", 16))
txtfld1.place(x = 230, y = 300)

def Button_Command():
  txtfld1.insert(END, str(txtfld.get()))


#Add Button Widget

btn = Button(window, text = "Click to display your Fullname", fg = "Red", command = Button_Command)
btn.place(x = 30, y = 300)

window.mainloop()