def validate_user_input(input_str):
    if len(input_str) == 0:
        print('Please input a string!')

        return get_user_input()
    else:
        return input_str

def get_user_input():
    return validate_user_input(input('What\'s the input string?'))

def show_result(input_str):
    print(f'{input_str} has {len(input_str)} characters.')

input_str = get_user_input()
show_result(input_str)
    