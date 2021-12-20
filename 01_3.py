def get_name_input():
    return input('What\'s your name?')

def concatenate(name):
    return f'Hello {name} nice to meet you!'

def output(str):
    print(str)

output(concatenate(get_name_input()))