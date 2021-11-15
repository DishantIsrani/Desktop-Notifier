from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time


t = Tk()
t.title('Dishant-Notifier-app')
t.geometry('500x400')
img = Image.open("notify.png")
tkimage = ImageTk.PhotoImage(img)

def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()

    if get_title == "" or get_msg == "" or get_time =="":
        messagebox.showerror('Alert', "All fields are required / Enter a valid input")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo('Notifier set', ' notification set')
        t.destroy()
        time.sleep(min_to_sec)
        
        notification.notify(
            title= get_title,
            message = get_msg,
            app_name = ' Notifier',
            timeout = 10
        )

img_label = Label(t, image=tkimage).grid()

t_label = Label(t, text="Title to Notify",font=("sans-serif", 10))
t_label.place(x=12, y=70)

title = Entry(t, width="25",font=("sans-serif", 13), bg='grey')
title.place(x=123, y=70)


m_label = Label(t, text="Display Message", font=("sans-serif", 10))
m_label.place(x=12, y=120)

msg = Entry(t, width="25", font=("sans-serif", 13), bg='grey')
msg.place(x=123,height=30, y=120)


time_label = Label(t, text="Set Time", font=("sans-serif", 10))
time_label.place(x=12, y=175)

time1 = Entry(t, width="25", font=("sans-serif", 13), bg='grey')
time1.place(x=123, y=175)


time_min_label = Label(t, text="min", font=("sans-serif", 10), bg='grey')
time_min_label.place(x=355, y=175)


but = Button(t, text="SET NOTIFICATION", font=("sans-serif", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",command=get_details)
but.place(x=170, y=230)

t.resizable(0,0)
t.mainloop()