def get_user_input():
    # You have to input manually to prevent error messages!
    num_string = input('Enter a list of numbers, separated by spaces: ') or '1 2 3 4 5 6 7 8'

    return num_string

def convert_num_string_to_list(num_string):
    num_list = []
    for c in num_string:
        if c == ' ':
            continue

        num_list.append(int(c))

    return num_list

def filter_even_numbers(num_list):
    even_list = []
    for n in num_list:
        if n % 2 == 0:
            even_list.append(n)

    return even_list

def display_output(even_list):
    print('The even numbers are: ')
    print(even_list)

def main():
    num_string = get_user_input()
    num_list = convert_num_string_to_list(num_string)
    even_list = filter_even_numbers(num_list)
    display_output(even_list)

main()
