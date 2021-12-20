def even_element_list():
    return [1, 2, 3, 4, 5, 6, 7, 8]

def odd_element_list():
    return [1, 1, 2, 3, 4, 5, 6, 6, 7]

def get_user_input():
    target = int(input('Enter search target: ') or '5')
    return target

def binary_search(num_list, target):
    high = len(num_list) -1
    low = 0
    while low <= high:
        mid = int((high + low) / 2)
        guess = num_list[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        if guess < target:
            low = mid + 1

    return None

def display_output(num_list, index):
    if index is None:
        print('Not found!')
    else:
        print(f'The index is {index}. The value is {num_list[index]}')

def main():
    num_list = odd_element_list()
    target = get_user_input()
    index = binary_search(num_list, target)
    display_output(num_list, index)

main()
