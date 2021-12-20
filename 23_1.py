ANS_Y = 'Y'
ANS_N = 'N'

def check_input(value):
    value = str.strip(value.upper())
    if value != 'Y' and value != 'N':
        print('Please input y or n!')
        exit()
    return value

def start():
    answer = check_input(input('Is the car silent when you turn the key?') or 'n')

    if answer == ANS_Y:
        answer = check_input(input('Are the battery terminals corroded?') or 'y')
        if answer == ANS_Y:
            print('Clean terminals and try starting again.')
        else:
            print('Replace cables and try again.')
    else:
        answer = check_input(input('Does the car make a clicking noise?') or 'n')
        if answer == ANS_Y:
            print('Replace the battery.')
        else:
            answer = check_input(input('Does the car crank up but fail to start?') or 'n')
            if answer == ANS_Y:
                print('Check spark plug connections.')
            else:
                answer = check_input(input('Does the engine start and then die?') or 'y')
                if answer == ANS_Y:
                    answer = check_input(input('Does your car have fuel injection?') or 'y')
                    if answer == ANS_Y:
                        print('Get it in for service.')
                    else:
                        print('Check to ensure the choke is opening and closing')
                else:
                    print('???')

start()