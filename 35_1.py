import random

def get_user_input():
    name_list = []

    while True:
        name = input('Enter a name: ')

        if name == '':
            break

        name_list.append(name)

    return name_list

def display_winner(name_list):
    index = random.randint(0, len(name_list) - 1)
    print(f'The winnner is... {name_list[index]}')

def main():
    name_list = get_user_input()
    display_winner(name_list)

main()
