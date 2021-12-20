def get_user_input():
    first = input('Enter the first number: ') or '1' 
    second = input('Enter the second number: ') or '51' 
    third = input('Enter the third number: ') or '2' 
    return validate_input(first, second, third)

def validate_input(first, second, third):
    try:
        (first, second, third) = (int(str.strip(first)), int(str.strip(second)), int(str.strip(third)))
    except:
        print('Please input a numeric values!')
        exit()

    if first == second or first == third or second == third:
        print('Duplicate value is detected!')
        exit()

    return (first, second, third)

def get_largest_number(first, second, third):
    max = first

    if second > max:
        max = second
    
    if third > max:
        max = third

    return max

def display_output(largest_num):
    print(f'The largest number is {largest_num}.')

(first, second, third) = get_user_input()
max = get_largest_number(first, second, third)
display_output(max)

