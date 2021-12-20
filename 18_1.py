CELSIUS_CHOICE = 'C'

def get_user_input():
    print('Press C to convert from Fahrenheit to Celsius.')
    print('Press F to convert from Celsius to Fahrenheit.')
    choice = input('Your choice: ') or CELSIUS_CHOICE

    choice = validate_choice_input(choice)
    
    temp = 0

    if choice == CELSIUS_CHOICE:
        temp = input('Please enter the temperature in Fahrenheit: ') or 32
    else:
        temp = input('Please enter the temperature in Celsius: ') or 32

    temp = validate_input(temp)

    return (choice, temp)

def validate_choice_input(choice):
    choice = choice.upper()

    if choice != 'C' and choice != 'F':
        print('Please input your choice with C or F!')
        exit() 
    return choice

def validate_input(temp):
    try:
        temp = float(temp)
    except:
        print('Please input a valide numeric value!')
        exit()
    return temp

def conduct_convert(choice, temp):
    converted_temp = 0
    if choice == CELSIUS_CHOICE:
        converted_temp = convert_to_celsius(temp)
    else:
        converted_temp = convert_to_fahrenheit(temp)
    return converted_temp

def convert_to_celsius(temp):
    print(temp)
    temp = (temp - 32) * 5 / 9
    return temp

def convert_to_fahrenheit(temp):
    temp = (temp * 9 / 5) + 32
    return temp

def display_output(choice, temp):
    if choice == CELSIUS_CHOICE:
        print(f'The temperature in Celsius is {temp}.')
    else:
        print(f'The temperature in Fahrenheit is {temp}.')

(choice, temp) = get_user_input()
converted_temp = conduct_convert(choice, temp)
display_output(choice, converted_temp)