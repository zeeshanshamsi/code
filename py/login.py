from os import system
 
    
class User: 

    def __init__(self, username, password): 
        self.username = username 
        self.password = password
        self.lockCount = 0

    
box = []

zeeshan = User('Zeeshan', '4321')
sam = User('Sam', '1234')

box.append(zeeshan)
box.append(sam)


import threading
def lockoutTimer():
    timer = threading.Timer(3.0, Unlock)
    timer.start() 

def Unlock():
    print('\nAccount is now unlocked')

import getpass
inputCheck = 1


while inputCheck == 1:
    userInput1 = input('\nUsername: ')
    

    try: 
	    p = getpass.getpass(prompt = "Password: ")
    except Exception as error: 
	    print('ERROR', error)   
    

    for x in box:
#        print('{0} is the username, {1} is the password'.format(x.username, x.password))
        if x.username == userInput1:

            if x.password == p:
                system('clear')
                print('\nWelcome, {}'.format(x.username))
                inputCheck = 0

            else: 
                
                x.lockCount+=1
                system('clear')
                if x.lockCount == 3:
                    print('\nLocked Out')
                    x.lockCount = 0
                    inputCheck = 0
                    lockoutTimer()
                print('\nPassword Incorrect. Please Try Again. Attempts Remaining: {}'.format((3 - x.lockCount)))



            

#           print('Username Not Found: {}'.format(userInput1))

#        print('Incorrect Password - this is attempt: ' + str(counter))
#            print('\nIncorrect Password - Attempt Number: {}'.format(counter))