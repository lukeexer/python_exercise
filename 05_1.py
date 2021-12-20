def get_user_input():
    num1 = input('What\'s the first number:') or '10'
    num2 = input('What\'s the second number:') or '5'
    return validate_input(num1, num2)

def validate_input(num1, num2):
    try:
        (num1, num2) = (float(num1), float(num2))
    except:
        print("All the input numbers should be integer!")
        get_user_input()

    if isinstance(num1, float) and isinstance(num2, float):
        if num1 >= 0 and num2 >= 0:
            return (num1, num2)
        else:
            print("All the input numbers should not be negative values!")
            get_user_input()

def display_output(num1, num2):
    print(f'{num1} + {num2} = {num1 + num2}\n' \
        f'{num1} - {num2} = {num1 - num2}\n' \
        f'{num1} * {num2} = {num1 * num2}\n' \
        f'{num1} / {num2} = {num1 / num2}')

(num1, num2) = get_user_input()
display_output(num1, num2)