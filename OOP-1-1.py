from tkinter import *
window = Tk()

window.geometry("600x600+30+20")
window.title("Welcome to Python Programming")

#Add Button Widget

btn = Button(window, text = "Click To Add Name", fg = "Blue")
btn.place(x = 70, y = 100)

#Add Label Widget

lbl = Label(window, text = "Student Personal Information", fg = "White", bg = "Red")
lbl.place(x = 300, y = 50, anchor = 'center')
lbl2 = Label(window, text = "Gender", fg = "Red")
lbl2.place(x = 70, y = 160)

#Add Text Field Widget

txtfld = Entry(window, bd = 3, font = ("verdana", 16))
txtfld.place(x=190, y=100)

#Add Ratio Button

v1 = StringVar()
v2 = StringVar
v1.set(1)

r1 = Radiobutton(window, text = "Male", value = v1)
r1.place(x = 80, y = 200)

r2=Radiobutton(window, text = "Female", value = v2)
r2.place(x = 200, y = 200)

lbl3 = Label(window, text = "Sports", fg = "Red")
lbl3.place(x = 70, y = 250)

v3 = IntVar()
v4 = IntVar()
v5 = IntVar()

chkbox = Checkbutton(window, text = "Basketall", variable=v3)
chkbox2 = Checkbutton(window, text = "Tennis", variable=v4)
chkbox3 = Checkbutton(window, text = "Badminton", variable=v5)

chkbox.place(x = 80, y = 300)
chkbox2.place(x = 200, y = 300)
chkbox3.place(x = 320, y = 300)

lbl4 = Label(window, text = "Subjects", fg = "Red")
lbl4.place(x = 70, y = 360)

var = StringVar()
var.set("Mathematics Subjects")
data1 = "Calculus"
data2 = "Discrete Mathematics"
data3 = "Differential Equation"
lstbox = Listbox(window, height=7, selectmode = 'multiple')
lstbox.insert(END, data1, data2, data3)
lstbox.place(x = 80, y = 400)

window.mainloop()