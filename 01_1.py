def get_name_input():
    return input('What\'s your name?')

def concatenate(name):
    return f'Hello {name} nice to meet you!'

def output(str):
    print(str)

name = get_name_input()
display_str = concatenate(name)
output(display_str)