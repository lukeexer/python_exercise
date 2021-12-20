import sys

LEGAL_DRIVING_AGE = 16

def get_user_input():
    age = input('What\'s your age?') or 15
    return validate_input(age)

def validate_input(age):
    try:
        age = int(age)
    except:
        print('Plase input a numeric value!')
        sys.exit()

    if age <= 0:
        print('Please input a valid age!')
        sys.exit()

    return age

def check_legal_driver(age):
    is_legal_driver = True if age >= LEGAL_DRIVING_AGE else False
    return is_legal_driver

def display_output(is_legal_driver):
    if is_legal_driver:
        print('You are old enough to legally drive.')
    else:
        print('You are not old enough to legally drive.')

def main():
    age = get_user_input()
    is_legal_driver = check_legal_driver(age)
    display_output(is_legal_driver)

main()
