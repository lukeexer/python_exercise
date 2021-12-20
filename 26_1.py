import math

def get_user_input():
    daily_rate = input('What is your balance?') or '5000'
    balance = input('What is the APR on the card (as a percent)?') or '12'
    monthly_payment = input('What is the monthly payment you can make?') or '100'
    return validate_input(daily_rate, balance, monthly_payment)

def validate_input(daily_rate, balance, monthly_payment):
    try:
        (daily_rate, balance, monthly_payment) = (float(str.strip(daily_rate)), float(str.strip(balance)), float(str.strip(monthly_payment)))
    except:
        print('Please input a numeric value!')
        exit()
    return (daily_rate, balance, monthly_payment)

def calculate_months_until_paid_off(daily_rate, balance, monthly_payment):
    daily_rate = daily_rate / 365
    months_until_apid_off = 0

    # a = math.log(1 + (balance / monthly_payment) * (1 - (1 + daily_rate) ** 30))
    # print(a)
    # b = math.log(1 + daily_rate)
    # print(b)
    
    months_until_apid_off = (-1/30) * math.log(1 + (balance / monthly_payment) * (1 - (1 + daily_rate) ** 30)) / math.log(1 + daily_rate)
    return months_until_apid_off

def display_output(months_until_apid_off):
    print(f'It will takes you {months_until_apid_off} months to pay off this card.')

(daily_rate, balance, monthly_payment) = get_user_input()
months_until_apid_off = calculate_months_until_paid_off(daily_rate, balance, monthly_payment)
display_output(months_until_apid_off)