COST_PER_SQUARE_FEET = 350

def get_user_input():
    length = input('Please input legth:') or '40'
    width = input('Please input width:') or '9'
    return validate_input(length, width)

def validate_input(length, width):
    try:
        (length, width) = (float(length), float(width))
    except:
        print('Please input numeric values!')
        exit()

    return (length, width)

def calculate_consumption(length, width):
    gallon = length * width / COST_PER_SQUARE_FEET

    if length * width % COST_PER_SQUARE_FEET > 0:
        return gallon + 1
    else:
        return gallon

def display_output(length, width):
    print(f'You will need to purchase {calculate_consumption(length, width):.0f} gallons of paint to cover {length * width} square feet.')

(length, width) = get_user_input()
display_output(length, width)