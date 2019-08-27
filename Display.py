from tkinter import *
from tkinter import messagebox
from alarmscript import *

window = Tk()
 
window.title("Pylarm")
window.geometry("400x300")

lbl_setalarm = Label(window,text="Set alarm")
lbl_setalarm.grid(column=6, row=1)



lbl_hour = Label(window,text="Hours")
lbl_hour.grid(column=4, row=2)
lbl_minute = Label(window,text="Minutes")
lbl_minute.grid(column=5, row=2)

spin_hour = Spinbox(window, from_=1, to=24, width=5)
spin_hour.grid(column=4,row=3)
spin_minute = Spinbox(window, from_=1, to=24, width=5)
spin_minute.grid(column=5,row=6)
 

btn_start = Button(window,text="Start",command=Clock(spin_minute.getint,spin_hour.getint))
btn_start.wait_variable
btn_start.grid(column=3,row=7)




window.mainloop()