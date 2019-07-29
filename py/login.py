
import threading
def lockoutTimer():
    timer = threading.Timer(3.0, Unlock)
    timer.start() 

def Unlock():
    print('\nAccount is now unlocked')

import getpass 
storedPassword = "Hello"
inputCheck = 1
    
counter=0
while inputCheck == 1:
    userInput1 = input('\nPlease Enter Username: ')
    counter+=1 
    try: 
	    p = getpass.getpass(prompt = "Password: ")
    except Exception as error: 
	    print('ERROR', error)   
    
    if p == storedPassword:
        print('\nWelcome!\n')
        inputCheck = 0
    else:
#        print('Incorrect Password - this is attempt: ' + str(counter))
        print('\nIncorrect Password - Attempt Number: {}'.format(counter))
        
        if counter == 3:
            print('\nLocked Out')
            inputCheck = 0
            lockoutTimer()

            
        
       
   
    
            