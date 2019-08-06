#Zeeshan Shamsi
#8/5/2019
#This application runs a calculator and hangman app through a login system based on user account type. 

from login import loginRun

# keeps program running until user 
# chooses to exit
while True:

    AppInput1 = input('\nWould you like to launch? 1 = Yes, 2 = Exit: ')

    if AppInput1 == '1' or AppInput1 == '2':

        if AppInput1 == '1': 
            loginRun()
        
        # absolutely a '2'
        else: 
            print('\nExiting Program\n')
            break
    # For anything other than '1' or '2'
    else:
        print('\nInput Incorrect\n')