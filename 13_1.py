def get_user_input():
    principal = input('Enter the principal: ') or 1500
    interest_rate = input('Enter the rate of interest: ') or 4.3
    years = input('Enter the number of years: ') or 6
    times_per_year = input('Enter the number of times the interest is compounded per year: ') or 4

    return validate_input(principal, interest_rate, years, times_per_year)

def validate_input(principal, interest_rate, years, times_per_year):
    try:
        (principal, interest_rate, years, times_per_year) = (float(principal), float(interest_rate), int(years), int(times_per_year))
    except:
        print('Please input a numeric value!')
        exit()

    return (principal, interest_rate, years, times_per_year)

def calculate_accrued_amount(principal, interest_rate, years, times_per_year):
    accrued_amount = principal * (1 + (interest_rate / 100) / times_per_year) ** (times_per_year * years)
    accrued_amount = round(accrued_amount, 2)
    return accrued_amount

def print_output(principal, years, interest_rate, times_per_year, accrued_amount):
    print(f'${principal} invested at {interest_rate}% for {years} years compounded {times_per_year} times per year is ${accrued_amount}.')

(principal, interest_rate, years, times_per_year) = get_user_input()
accrued_amount = calculate_accrued_amount(principal, interest_rate, years, times_per_year)
print_output(principal, years, interest_rate, times_per_year, accrued_amount)