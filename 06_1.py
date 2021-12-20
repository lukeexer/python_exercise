import datetime

def get_user_input():
    age = input('What is your current age?') or '25'
    retire_age = input('At what age would you like to retire?') or '65'
    return validate_user_input(age, retire_age)

def validate_user_input(age, retire_age):
    try:
        (age, retire_age) = (int(age), int(retire_age))
    except:
        print('All the input ages must be numbers!')
        get_user_input()

    if retire_age - age > 0:
        return (age, retire_age)
    else:
        print('You have already retired.')
        exit()

def calculate_years_left(age, retire_age):
    return retire_age - age

def display_result(age, retire_age):
    now = datetime.datetime.now()

    print(f'You have {calculate_years_left(age, retire_age)} years left until you can retire.')
    print(f'It\'s {now.year}, so you can retire in {now.year + calculate_years_left(age, retire_age)}.')

(age, retire_age) = get_user_input()
display_result(age, retire_age)