import tkinter as tk
import time
import datetime as dt
import winsound
import json


with open('config.json') as config_file:
    setting = json.load(config_file)

frequency = 2500  # Set Frequency To 2500 Hertz

duration = setting['beep_duration']  # Default 300 ms


def Clock(hours, minutes):
    if dt.datetime.now().hour == hours and dt.datetime.now().minute == minutes:  # c
                root = tk.Tk()
                mainapp = AlarmClock(master=root)
                mainapp.mainloop()


class AlarmClock(tk.Frame ):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        # self.clock()

    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.menu = tk.Button(self, text="Menu", command=self.mainmenu)
        self.menu.grid(row=0, column=0)
        self.quit.grid(row=0, column=1)
        tk.Label(self.master, text="ALARM!").grid(row=2, column=0)
        rep = setting['beep_repeat']
        repc = 0  # counter
        while True:  # Alarm Sound with windows
            repc += 1
            time.sleep(1)
            winsound.Beep(frequency, duration)
            if (repc >= rep):
                break
    def mainmenu(self):
        self.master.destroy()
        main()

class Credits(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.menu = tk.Button(self, text="Menu", command=self.mainmenu)
        self.quit.grid(row=0, column=1)
        self.menu.grid(row=0, column=0)
        tk.Label(self.master, text="Created by Tiago Faustino || github.com/ChinadaCam ").grid(row=1)
        tk.Label(self.master, text="Contributor: Catarina Bento || github.com/Catarinab ").grid(row=2)

    def mainmenu(self):
        self.master.destroy()
        main()


class Alarm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.hourentry = tk.Entry(self.master)

        self.minuteentry = tk.Entry(self.master)

        self.inputhour = tk.StringVar()
        self.inputhour.set(int(00))
        self.hourentry["textvariable"] = self.inputhour

        self.inputminute = tk.StringVar()
        self.inputminute.set(int(00))
        self.minuteentry["textvariable"] = self.inputminute

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.menu = tk.Button(self, text="Menu", command=self.mainmenu)

        self.save = tk.Button(self, text="Set Alarm", command=self.send_contents)

        self.hourentry.grid(row=1, column=1)
        self.minuteentry.grid(row=2, column=1)
        tk.Label(self.master, text="Hour:").grid(row=1)
        tk.Label(self.master, text="Minute:").grid(row=2)
        self.quit.grid(row=0, column=1)
        self.menu.grid(row=0, column=0)
        self.save.grid(row=0, column=2)

    def send_contents(self):
        self.master.destroy()
        Clock(int(self.inputhour.get()), int(self.inputminute.get()))

    def mainmenu(self):
        self.master.destroy()
        main()



class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    #start widgets
    def create_widgets(self):
        self.credits = tk.Button(self, text="See Credits", command=self.create_window_credits)
        self.alarm = tk.Button(self, text="Set Alarm", command=self.create_window_alarm)
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row=2, column=1)
        self.alarm.grid(row=0, column=1)
        self.credits.grid(row=1, column=1)


    def create_window_alarm(self):
        self.master.destroy()
        root = tk.Tk()
        alarm = Alarm(master=root)
        alarm.mainloop()

    def create_window_credits(self):
        self.master.destroy()
        root = tk.Tk()
        credits = Credits(master=root)
        credits.mainloop()



def main():
    root = tk.Tk()
    mainapp = MainMenu(master=root)
    mainapp.mainloop()



if __name__ == "__main__":
    main()