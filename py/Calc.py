def calcRun():

    # so function runs indefinitely 
    while True: 

        print('\nWelcome to the calculator! Please select what you would like to do: \n')
        action = input('Add = 1 Subtract = 2 Multiply = 3 Divide = 4: ')

        if action == '1' or action == '2' or action == '3' or action == '4':
            
            inputCheck = 1
            while inputCheck == 1:
                userInput1 = input('\nPlease enter in a number 1: ')
                
                # Exception handling to make sure input is a number
                if userInput1.isnumeric():
                    userInput1 = int(userInput1)
                    inputCheck = 0
                else:
                    print('Enter a real number!')

                # Exception handling to make sure input is a number
            inputCheck = 1

            # Allows function to run indefinitely
            while True:
                userInput2 = input('Please enter in a number 2: ')
                
                # Exception handling to make sure input is a number
                if userInput2.isnumeric():
                    userInput2 = int(userInput2)
                    break
                else:
                    print('Enter a real number!')

            # strings of arithmetic are used to help display 'Answer:' on screen based on action value.
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
        
        # Exception handling to make sure input is '1', '2', '3', or '4'.
        else:
            print('Input Wrong')

        # After calculation, prompt is displayed and requests user input. 
        launchInput = input('Continue = 1 Exit = 2: ')

        # Comparing the launchInput variable to determine if the calculator will run again. 
        if launchInput == '1' or launchInput == '2':

            if launchInput == '1':
                print('\n')
            else:
                print('\nExiting Calculator')
                break 