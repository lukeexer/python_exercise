CONSTANT = 0.09290304

def get_user_input():
    length = input('What is the length of the room in feet?') or '15'
    width = input('What is the width of the room in feet?') or '20'
    return validate_input(length, width)

def validate_input(length, width):
    try:
        (length, width) = (int(length), int(width))
    except:
        print('Please input numeric values!')
        exit()

    return (length, width)

def calculate_square_feet(length, width):
    return length * width;

def calculate_square_meter(length, width):
    square_feet = calculate_square_feet(length, width)
    return square_feet * CONSTANT

def display_output(length, width):
    print(f'You entered dimensions of {length} feet by {width} feet.')
    print('The area is')
    print(f'{calculate_square_feet(length, width)} square feet')
    print(f'{calculate_square_meter(length, width):.3f} square meters')

(length, width) = get_user_input()
display_output(length, width)