def get_user_input():
    euros_from = input('How many euros are you exchanging?') or 81
    exchasnge_rate = input('what is the exchange rate?') or 137.51

    return validate_input(euros_from, exchasnge_rate)

def validate_input():
    

def display_output(euro_from, exchange_rate, dollar_to):
    print(f'{euro_from} euros at an exchange rate of {exchange_rate} is\n {dollar_to} U.S. dollars.')

get_user_input()
display_output()