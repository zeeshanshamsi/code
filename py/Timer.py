# Program to demonstrate 
# timer objects in python 

import threading 
def success(): 
    print("Success!\n")

def startFirstTimer():
    timer = threading.Timer(3.0, startSecondTimer)
    timer.start() 
    print("Timer1 Start\n")

def startSecondTimer():
    userinput2 = input('Enter Number to Start Timer 2: ')
    
    if userinput2.isnumeric():
        timer = threading.Timer(3.0, startThirdTimer)
        timer.start()
        print("Timer2 Start\n")
    else: print('Enter a real number!')

def startThirdTimer():
    userinput3 = input('Enter Number to Start Timer 3: ')

    if userinput3.isnumeric():
        timer = threading.Timer(3.0, success)
        timer.start()
        print("Timer3 Start\n")
    else: print('Enter a real number!')

userInput1 = input('Enter Number to Start Timer: ')

if userInput1.isnumeric(): 
    startFirstTimer()
else: print('Enter a real number!')