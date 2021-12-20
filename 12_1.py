def get_user_input():
    principal = input('Enter the principal: ') or 1500
    interest_rate = input('Enter the rate of interest: ') or 4.3
    years = input('Enter the number of years: ') or 4

    return validate_input(principal, interest_rate, years)

def validate_input(principal, interest_rate, years):
    try:
        (principal, interest_rate, years) = (float(principal), float(interest_rate), int(years))
    except:
        print('Please input a numeric value!')
        exit()

    return (principal, interest_rate, years)

def calculate_accrued_amount(principal, interest_rate, years):
    accrued_amount = round(principal * (1 + interest_rate / 100 * years), 2)
    return accrued_amount


def print_output(years, interest_rate, accrued_amount):
    print(f'After {years} years at {interest_rate}%, the investment will be worth ${accrued_amount}.')

(principal, interest_rate, years) = get_user_input()
accrued_amount = calculate_accrued_amount(principal, interest_rate, years)
print_output(years, interest_rate, accrued_amount)