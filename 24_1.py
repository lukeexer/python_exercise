def get_user_input():
    print('Enter two strings and I\'ll Tell you if tye are anagrams: ')
    first = input('Enter the first string: ') or 'note'
    second = input('Enter the second string: ') or 'tone'
    return validate_input(first, second)

def validate_input(first, second):
    first = str.strip(first)
    second = str.strip(second)
    if len(first) != len(second):
        print('The length of the two input strings should be the same!')
        exit()

    return (first, second)

def is_anagram(first, second):
    if first == second:
        return False
    else:
        return True

def display_output(first, second, is_anagram):
    if is_anagram:
        print(f'{first} and {second} are anagram.')
    else:
        print(f'{first} and {second} are not anagram.')

(first, second) = get_user_input()
is_anagram = is_anagram(first, second)
display_output(first, second, is_anagram)