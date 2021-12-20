WI_TAX_RATE = 0.055

def get_user_input():
    amount = input('What is the order amount?') or 10
    state = input('What is the state?') or 'WI'

    return validate_input(amount, state)

def validate_input(amount, state):
    try:
        amount = int(amount)
    except:
        print('Please input a valid numeric value!')
        exit()

    state = state.upper()

    if state != 'WI' and state != 'MN':
        print('Please input WI or MN for state!')
        exit()

    return (amount, state)

def calculate_total_and_tax(amount, state):
    total = amount
    tax = 0

    if state == 'WI':
        tax = total * WI_TAX_RATE

    total = total + tax

    return (total, tax)

def display_output(amount, tax, total, state):
    if state == 'WI':
        print(f'The subtotal is ${amount}.')
        print(f'The tax is ${tax}.')

    print(f'The total is ${total}.')

(amount, state) = get_user_input()
(total, tax) = calculate_total_and_tax(amount, state)
display_output(amount, tax, total, state)