def loginRun():
    from Calc import calcRun

    from Hangman import HangRun

    from os import system
    counter = 0
        

    class User: 

        def __init__(self, username, password, accountType): 
            self.username = username 
            self.password = password
            self.lockCount = 0
            self.accountType = accountType 

        
    box = []

    zeeshan = User('Zeeshan', '1234', 'admin')
    sam = User('Sam', '1234', 'standard')
    bob = User('Bob', '1234', 'standard')
    drake = User('Drake', '1234', 'standard')



    box.append(zeeshan)
    box.append(sam)
    box.append(bob)
    box.append(drake)

    import threading
    
    # creating and starting a timer
    def lockoutTimer():
        timer = threading.Timer(3.0, Unlock)
        timer.start() 

    #prints "account is unlocked"
    def Unlock():
        print('\nAccount is now unlocked')


    # incrementing counter by 1. Accepted argument (a) from call which represented current value of counter.
    def GlobalLock(a):
        a+=1
        print(a)
        return a

    #determined account type based on current object's account type value. 
    def UserAccountTypeCheck():
        if x.accountType == 'admin': 
            ChooseApp()
        else: 
            HangRun()

    # allows user to choose application type based on user input. 
    def ChooseApp():
        inputCheck = 0

        # This loop will run until inputCheck is changed to anything other than zero. 
        while inputCheck == 0:
            print('\nChoose App: 1 = Calculator and 2 = Hangman\n ')
            AppInput1 = input('\nChoice #: ')


            # if true, run the calculator app
            if AppInput1 == '1': 
                inputCheck = 1
                calcRun()


            # if true, run the hangman game
            elif AppInput1 == '2':
                inputCheck = 1
                HangRun()

            # user entered value other than '1' or '2'
            else: 
                system('clear')
                print('Input Incorrect')
            
    # imported getpass function so we can collect password from user. 
    import getpass
    inputCheck = 1

    # while loop runs and checks to see if user supplied credentials match objects stored in box array
    while inputCheck == 1:
        # gathering user input for username
        userInput1 = input('\nUsername: ')
        
        # gathering user input for password
        try: 
            p = getpass.getpass(prompt = "Password: ")
        except Exception as error: 
            print('ERROR', error)   
        




        # comparing objects stored in box (x) to the user input
        for x in box:
            if x.username == userInput1:
                
                
                # true side clears screen and prints welcome. Then calls UserAccountTypeCheck to check user accnt type.
                if x.password == p:
                    system('clear')
                    print('\nWelcome, {}\n'.format(x.username))
                    #inputCheck = 0
                    UserAccountTypeCheck()

                    break

                # if password is incorrect, increments lockcount on object then clears screen and prints remaining tries
                else:                   
                    x.lockCount+=1
                    system('clear')
                    print('\nPassword Incorrect for User: {0}. Attempts Remaining: {1}'.format(x.username, (3 - x.lockCount)))
                    
                    # if lockcount exceeds 3 attempts, displays "Locked Out", resets object lockcount to zero.
                    if x.lockCount == 3:
                        print('\nLocked Out')
                        x.lockCount = 0

       # Keeps track of number of login attempts. After 10 attempts, program exits.                
        counter+=1
        if counter == 10:
            print('\nExceeded Attempt Limit - Exiting Program\n')
            break

        # Allows user to exit login program by typing 'exit'
        if userInput1 == 'exit':
            break 
        