import time
import datetime as dt
import os
import winsound
import json


#open config file
with open('config.json') as config_file:
    setting = json.load(config_file)

frequency = 2500  # Set Frequency To 2500 Hertz
 
duration = setting['beep_duration'] # Default 300 ms 



def Start():
    escolha =""
    os.system('cls')
    print(" ALARM BY FAUSTINO\n")
    print("==================\n")
    print("||              ||\n")
    print("|| 1. Set Alarm ||\n")
    print("|| 2. Credits ||\n")
    print("|| 3. Quit      ||\n")
    print("||              ||\n")
    print("==================\n")
   
    try:
        escolha = int(input("Choose: "))
        if (escolha ==1):
            Clock()

            os.system('cls')
        elif(escolha==2):
            Credits()
        else:
            os.system('cls')
            exit()
            
           
    except ValueError:
        print("Not a valid value")
        time.sleep(5)
        Start()
    except Exception as e:
        print(str(e))
        Start()


def Credits():
    print("============================\n")
    print("||                        ||\n")
    print("|| Made by Tiago Faustino ||\n")
    print("|| github.com/ChinadaCam  ||\n")
    print("|| 1. Quit                ||\n")
    print("||                        ||\n")
    print("============================\n")

    try:
        escolha = int(input("Choose: "))
        if (escolha ==1):
            Start()

            os.system('cls')
            
           
    except ValueError:
        print("Not a valid value")
        time.sleep(5)
        Start()
    except Exception as e:
        print(str(e))
        Start()


def Clock():
     
    print("\033[H\033[J")
    hours= int(input("Insert the hour(1-24 | 00 format): "))
    minutes= int(input("Insert the minutes(1-59 | 00 format): "))
    rep= setting['beep_repeat'] # int(input("Number of times sound repeat ( 0 for no sound): "))
    repc=0 #counter
    print("\033[H\033[J")
    print("TIK TOK")
    print("ctrl+c to terminate the program")
    
    


    while True:
        try: 

            if dt.datetime.now().hour==hours and dt.datetime.now().minute==minutes : #c
            
                    
                while True: #Alarm Sound with windows
                    repc+=1
                    winsound.Beep(frequency, duration) 
                    time.sleep(1)
                    print("ALARM")
                    if(repc>=rep):
                        time.sleep(2)
                        break
                break
                
        except KeyboardInterrupt:
            Start()
                
        except Exception as e:
            print("Error: " + str(e))
            

if __name__=='__main__':
    Start()