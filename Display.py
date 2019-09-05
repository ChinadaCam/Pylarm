from tkinter import *
from tkinter import messagebox
from alarmscript import *

window = Tk()
 
window.title("Pylarm")
window.geometry("400x300")
window.wm_maxsize(width= 400, height= 300)
window.wm_minsize( width= 400, height= 300)


lbl_setalarm = Label(window,text="Pylarm")
lbl_setalarm.grid(column=6, row=1)



lbl_hour = Label(window,text="Hours")
lbl_hour.grid(column=4, row=2)
lbl_minute = Label(window,text="Minutes")
lbl_minute.grid(column=5, row=2)

spin_hour = Spinbox(window, from_=1, to=24, width=5)
spin_hour.grid(column=4,row=3)
spin_minute = Spinbox(window, from_=1, to=24, width=5)
spin_minute.grid(column=5,row=3)
print(spin_minute.index) 

try:
    
    btn_start = Button(window,text="Start",command=Clock( int(spin_minute.index),int(spin_hour.index)))
    btn_start.grid(column = 4, row= 10)
    btn_start.wait_variable
except Exception as e:
    print(str(e))
    messagebox.showerror("Error",str(e))



window.mainloop()