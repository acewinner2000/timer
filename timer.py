from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("500x200")
win.title("تايمر شمارش معکوس")
win.config(bg="#3399ac")

time = 0

def set():
    global time
    time += int(entry.get())
    return time

def reset():
    global time
    time = 0
    label.config(text = '')
    btn.config(state = NORMAL)
    btn2.config(state = NORMAL)
    entry.delete(0,END)
    label3.config(text='')
def countdown():
    
    global time
    if time > 0:
        
        btn.config(state = DISABLED)
        btn2.config(state = DISABLED)
        label.config(text = time)
        label3.config(text=' زمان باقیمانده')
        time -= 1
        label.after(1000,countdown)
        if time == 0:
            messagebox.showinfo("شمارش معکوس", "زمان به اتمام رسيد")
            btn.config(state = NORMAL)
            btn2.config(state = NORMAL)
            reset()
        



label = Label(win, font = "Tahoma 45 bold", bg = '#3399ac', fg = '#999900')
label.place(x = 150, y = 70)



entry_label = Label(win, text = "زمان را بر حسب ثانيه وارد کنيد", font = "arial 15 bold",bg="#3399ac")
entry_label.place(x = 10, y = 10)



entry = Entry(win, font = "Tahoma 10 bold", width = 15)
entry.place(x = 230, y = 15)


label3=Label(win,font="arial 15 bold",bg='#3399ac')
label3.place(x=50,y=100)

btn = Button(win, text = "تنظيم زمان", font = "Tahoma 10 bold", bg = "orange", fg = "black",
             width = 10, command = set)
btn.place(x = 400, y = 10)


btn2 = Button(win, text = "شروع", font = "Tahoma 10 bold", bg = "orange", fg = "black",
              width = 10, command = countdown)
btn2.place(x = 400, y = 40)


btn3 = Button(win, text = "تنظيم مجدد", font = "Tahoma 10 bold", bg = "orange", fg = "black",
              width = 10, command = reset)
btn3.place(x = 400, y = 70)




win.mainloop()