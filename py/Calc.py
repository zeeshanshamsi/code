def calcRun():



    while True: 










        print('\nWelcome to the calculator! Please select what you would like to do: \n')
        action = input('Add = 1 Subtract = 2 Multiply = 3 Divide = 4: ')

        if action == '1' or action == '2' or action == '3' or action == '4':
            inputCheck = 1


            while inputCheck == 1:
                userInput1 = input('\nPlease enter in a number 1: ')
                
                if userInput1.isnumeric():
                    userInput1 = int(userInput1)
                    inputCheck = 0
                else:
                    print('Enter a real number!')


            inputCheck = 1
            while inputCheck == 1:
                userInput2 = input('Please enter in a number 2: ')
                
                if userInput2.isnumeric():
                    userInput2 = int(userInput2)
                    inputCheck = 0
                else:
                    print('Enter a real number!')


            if action == '1':
                print('\nAnswer = ' + str((userInput1 + userInput2)))

            elif action == '2':
                print('\nAnswer = ' + str((userInput1 - userInput2)))

            elif action == '3':
                print('\nAnswer = ' + str((userInput1 * userInput2)))

            elif action == '4':
                print('\nAnswer = ' + str((userInput1 // userInput2)))
            else:
                print('Everything was false!')
        else:
            print('Input Wrong')

        
        
        
        
        
        
        launchInput = input('Continue = 1 Exit = 2: ')

        if launchInput == '1' or launchInput == '2':

            if launchInput == '1':
                print('Hello')
            else:
                print('\nExiting Program')
                break 







    