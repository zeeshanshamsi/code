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
    def lockoutTimer():
        timer = threading.Timer(3.0, Unlock)
        timer.start() 

    def Unlock():
        print('\nAccount is now unlocked')



    def GlobalLock(a):
        a+=1
        print(a)
        return a

    def UserAccountTypeCheck():
        if x.accountType == 'admin': 
            ChooseApp()
        else: 
            HangRun()


    def ChooseApp():
        inputCheck = 0
        while inputCheck == 0:
            print('\nChoose App: 1 = Calculator and 2 = Hangman\n ')
            AppInput1 = input('\nChoice #: ')

            if AppInput1 == '1': 
                inputCheck = 1
                calcRun()
                
                
            
            elif AppInput1 == '2':
                inputCheck = 1
                HangRun()

            else: 
                system('clear')
                print('Input Incorrect')
            








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
                    #inputCheck = 0
                    UserAccountTypeCheck()
                    break

                else: 
                    
                    x.lockCount+=1
                    system('clear')
                    
                    
                    print('\nPassword Incorrect for User: {0}. Attempts Remaining: {1}'.format(x.username, (3 - x.lockCount)))





                    if x.lockCount == 3:
                        print('\nLocked Out')
                        x.lockCount = 0
                        #lockoutTimer()
            

    #            indexCheck = box.index(x)
    #            if len(box) == indexCheck + 1:
    #                clearIt = 1



        counter+=1
        if counter == 10:
            print('\nExceeded Attempt Limit - Exiting Program\n')
            break

        if userInput1 == 'exit':
            break 
        