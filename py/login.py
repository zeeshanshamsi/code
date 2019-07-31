from os import system
counter = 0
    
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



def GlobalLock(a):
    a+=1
    print(a)
    return a




import getpass
inputCheck = 1


while inputCheck == 1:
    userInput1 = input('\nUsername: ')
    

    try: 
	    p = getpass.getpass(prompt = "Password: ")
    except Exception as error: 
	    print('ERROR', error)   
    

    for x in box:

        if x.username == userInput1:

            if x.password == p:
                system('clear')
                print('\nWelcome, {}\n'.format(x.username))
                inputCheck = 0
                break

            else: 
                
                x.lockCount+=1
                system('clear')
                
                
                print('\nPassword Incorrect for User: {0}. Attempts Remaining: {1}'.format(x.username, (3 - x.lockCount)))

                if x.lockCount == 3:
                    print('\nLocked Out')
                    x.lockCount = 0
                    #lockoutTimer()
    

    counter+=1
    if counter == 10:
        print('\nExceeded Attempt Limit - Exiting Program\n')
        break

    if userInput1 == 'exit':
        break 
    