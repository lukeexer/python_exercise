import getpass

import scrypt

# The password is 'abc123'
PASSWORD = b'\x8a\xe5\xe6V\xef%\xc2\xe4\xebLc\x07\xe4\xf3\xf4\x19\x1b\x82(\xa5\xd2^B\xedJ_\x81\xbe\xff\x96\x86L\xf2\t\xaa\xe1\xd8\x92\x8f\xdaC\tu\x80\x19\xb1\xa6\xa5\xc3S\xe3\x12#\xea\x93\xb2\xbd\x80\xa2\xc8a\xe8\xb7\n'
SALT = b'salt'

def get_user_input():
    password = getpass.getpass('What is the password?') or 'abc123'
    return password

def authenticate(password):
    password = str.encode(password)
    password = scrypt.hash(password, SALT)

    if PASSWORD == password:
        return True

    return False

def display_output(is_ahthorized):
    if is_ahthorized:
        print('Welcome!')
    else:
        print('I don\'t know you')

def main():
    password = get_user_input()
    is_ahthorized = authenticate(password)
    display_output(is_ahthorized)

main()
