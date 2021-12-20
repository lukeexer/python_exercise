STATE_WISONSIN = 'WISCONSIN'
STATE_ABBR_WISONSIN = 'WI'
STATE_ILLINOIS = 'ILLINOIS'
STATE_ABBR_ILLINOIS = 'IL'

COUNTY_EAU_CLAIRE = 'EAU CLAIRE'
COUNTY_DUNN = 'DUNN'

def get_user_input():
    amount = input('What is the order amount?') or '10'
    state = input('What state do you live in?') or 'Wisconsin'
    county = ''

    state = validate_state(state)

    if state == STATE_WISONSIN or state == STATE_ABBR_WISONSIN:
        county = input('What county do you live in?') or 'Eau Claire'
        county = validate_county(county)

    amount = validate_input(amount)

    return (amount, state, county)

def validate_state(state):
    state = str.strip(state.upper())
    return state

def validate_county(county):
    county = str.strip(county.upper())
    return county

def validate_input(amount):
    try:
        amount = int(str.strip(amount))
    except:
        print('Please input a numeric value for amount!')
        exit()

    return amount

def calculate(amount, state, county):
    tax = 0
    total = amount

    if state == STATE_WISONSIN or state == STATE_ABBR_WISONSIN:
        if county == COUNTY_EAU_CLAIRE:
            tax = amount * 0.05
        elif county == COUNTY_DUNN:
            tax = amount * 0.04
    elif state == STATE_ILLINOIS or state == STATE_ABBR_ILLINOIS:
            tax = amount * 0.08

    total = total + tax

    return (tax, total)

def display_output(tax, total, state):
    print(state)
    if state == STATE_WISONSIN or state == STATE_ABBR_WISONSIN:
        print(f'The tax is ${tax}.')
    elif state == STATE_ILLINOIS or state == STATE_ABBR_ILLINOIS:
        print(f'The tax is ${tax}.')
    
    print(f'The total is ${total}.')

(amount, state, county) = get_user_input()
print((amount, state, county))
(tax, total) = calculate(amount, state, county)
display_output(tax, total, state)