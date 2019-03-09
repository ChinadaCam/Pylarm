import time
import datetime as dt
import os
import winsound


def main():
    
    #vars
    x=0
    frequency = 2500  # Set Frequency To 2500 Hertz  
    duration = 100  # Set Duration To 100 ms 

    def Start():
        os.system('cls')
        print(" ALARM BY FAUSTINO\n")
        print("==================\n")
        print("||              ||\n")
        print("|| 1. Set Alarm ||\n")
        print("|| 2. Quit      ||\n")
        print("||              ||\n")
        print("==================\n")
        try:
            escolha = int(input("Choose: "))
            if (escolha ==1):
                Clock()
                
                os.system('cls')
            elif(escolha ==2):
                os.system('cls')
                exit()
               
        except ValueError:
            print("Not a valid value")
            time.sleep(5)
            Start()
        
    

    def Clock():
         
        print("\033[H\033[J")
        hour= int(input("Insert the hour(1-24 | 00 format): "))
        minute=int(input("Insert the minutes(1-59 | 00 format): "))
        rep=int(input("Number of times sound repeat ( 0 for no sound): "))
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
                            Start()
                            break
                    break
                    
                    
                

            except ValueError:
                print("Not a valid time")
                Start()
            except KeyboardInterrupt:
                print("Interrupted")
                Start()

        
    Start()
  


if __name__=='__main__':
    main()