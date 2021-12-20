def get_user_input():
    has_error = True
    rate = 0

    while has_error is True:
        rate = input('What is the rate of return? ')
        (has_error, rate) = validate_input(rate)
        if has_error is True:
            print('Sorry. That\'s not a valid input.')

    return rate

def validate_input(rate):
    rate = str.strip(rate)

    try:
        rate = float(rate)
    except:
        return (True. rate)

    if rate <= 0:
        return (True, rate)
    
    return (False, rate)

def calculate_years_to_double_investment(rate):
    years = 72 / rate
    return years

def display_output(years):
    print(f'It will take {int(years)} years to double your initial investment.')

rate = get_user_input()
years = calculate_years_to_double_investment(rate)
display_output(years)