import random
import string

def get_user_input():
    min_len = int(input('What\'s the minimum length? ') or '8')
    special_cahr_num = int(input('How many special characters? ') or '2')
    numbers_num = int(input('How many numbers? ') or '2')

    return (min_len, special_cahr_num, numbers_num)

def generate_non_repeat_int_list(num, min_len):
    tmp_list = []
    while True:
        tmp = random.randint(0, min_len - 1)

        is_duplicate = tmp in tmp_list

        if is_duplicate is True:
            continue

        tmp_list.append(tmp)

        num = num - 1

        if num == 0:
            break

    print(tmp_list)
    return tmp_list

def generate_password(min_len, special_cahr_num, numbers_num):
    char_list = []
    for _ in range(min_len):
        char_list.append(random.choice(string.ascii_letters))

    pos_list = generate_non_repeat_int_list(special_cahr_num + numbers_num, min_len)

    for i in range(numbers_num):
        index = pos_list[i]
        char_list[index] = random.choice(string.digits)

    for i in range(special_cahr_num):
        index = pos_list[i + numbers_num]
        char_list[index] = random.choice(string.punctuation)

    password = ''
    password = password.join(char_list)

    return password

def display_output(password):
    print('Your password is')
    print(password)

def main():
    (min_len, special_cahr_num, numbers_num) = get_user_input()
    password = generate_password(min_len, special_cahr_num, numbers_num)
    display_output(password)

main()
