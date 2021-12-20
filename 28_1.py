def get_user_input():
    num_list = []

    for i in range(5):
        num_list.append(input('Enter a number: '))

    return validate_input(num_list)

def validate_input(num_list):
    converted_num_list = []

    try:
        for i in num_list:
            converted_num_list.append(int(i))
    except:
        print('Please input numeric values!')
        exit()

    return converted_num_list

def calculate_total(num_list):
    total = 0

    for i in num_list:
        total += i

    return total

def display_output(total):
    print(f'The total is {total}.')

num_list = get_user_input()
total = calculate_total(num_list)
display_output(total)