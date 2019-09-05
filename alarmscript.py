import time
import datetime as dt
import os
import winsound
from tkinter import messagebox




#vars

frequency = 3000  # Set Frequency To 2500 Hertz  
duration = 200  # Set Duration To 100 ms 


def Clock(minute,hour):
     
    print("\033[H\033[J")
    hours= hour #int(input("Insert the hour(1-24 | 00 format): "))
    minutes= minute #int(input("Insert the minutes(1-59 | 00 format): "))
    rep= 5 # int(input("Number of times sound repeat ( 0 for no sound): "))
    repc=0 #counter
    print("\033[H\033[J")
    print("TIK TOK")
    print("ctrl+c to terminate")
    
    while True:
        try: 
            if dt.datetime.now().hour==hour and dt.datetime.now().minute==minute : #c
            
                    
                while True: #Alarm Sound with windows
                    repc+=1
                    winsound.Beep(frequency, duration) 
                    time.sleep(1)
                    print("ALARM")
                    if(repc>=rep):
                        time.sleep(2)
                        break
                break
                
                
            
        except ValueError:
            messagebox.showerror("Error","Insert a valid value")
        except Exception as e:
            messagebox.showerror("Error ", str(e))
            print("Error: " + str(e))
            
   
    


