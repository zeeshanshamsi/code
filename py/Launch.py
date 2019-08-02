from login import loginRun
inputCheck = 0


while inputCheck == 0:
            print('\nWould you like to launch? 1 = yes, 2 = exit')
            AppInput1 = input('\nAnswer: ')

            if AppInput1 == '1': 
                inputCheck = 1
                loginRun()
                
                
            
            if AppInput1 == '2':
                break

            else: 
                print('Input Incorrect')


