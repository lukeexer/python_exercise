import math

def get_user_input():
    num_list = []

    while True:
        tmp_val = input('Enter a number: ')

        if tmp_val == 'done':
            break

        num_list.append(int(tmp_val))

    return num_list

def cal_mean(num_list):
    tmp_sum = 0

    for num in num_list:
        tmp_sum += num

    mean = tmp_sum / len(num_list)

    return mean

def cal_max(num_list):
    tmp_val = num_list[0]

    for num in num_list:
        if num > tmp_val:
            tmp_val = num

    return tmp_val

def cal_min(num_list):
    tmp_val = num_list[0]

    for num in num_list:
        if num < tmp_val:
            tmp_val = num

    return tmp_val

def cal_standard_deviation(num_list):
    mean = cal_mean(num_list)

    dev_list = []
    for num in num_list:
        dev_list.append((num - mean) ** 2)

    dev_sum = 0
    for num in dev_list:
        dev_sum += num
    dev_mean = dev_sum / len(dev_list)

    std_dev = math.sqrt(dev_mean)

    return std_dev

def display_statistics(num_list):
    print('Numbers:', end='')
    for i, num in enumerate(num_list):
        if i == len(num_list) - 1:
            print(f' {num}')
        else:
            print(f' {num},', end='')

    print(f'The average is: {cal_mean(num_list)}')
    print(f'The maximun is: {cal_max(num_list)}')
    print(f'The minimun is: {cal_min(num_list)}')
    print(f'The standard deviation is: {cal_standard_deviation(num_list):.2f}')

def main():
    num_list = get_user_input()
    display_statistics(num_list)

main()
