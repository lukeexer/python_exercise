PW_VERY_WEAK = 1
PW_WEAK = 2
PW_STRONG = 3
PW_VERY_STRONG = 4

def get_user_input():
    password = input('Enter password: ') or '12345'
    #password = input('Enter password: ') or 'abcdef'
    #password = input('Enter password: ') or 'abc123xyz'
    #password = input('Enter password: ') or '1337h@xor!'

    return validate_input(password)

def validate_input(password):
    password = str.strip(password)
    return password

def password_validator(password):
    if check_very_strong_pw(password) is True:
        return PW_VERY_STRONG

    if check_strong_pw(password) is True:
        return PW_STRONG

    if check_weak_pw(password) is True:
        return PW_WEAK

    if check_very_weak_pw(password) is True:
        return PW_VERY_WEAK

def check_very_weak_pw(password):
    length = len(password)
    all_digits = password.isdigit()

    if length < 8 and all_digits is True:
        return True
 
    return False
        
def check_weak_pw(password):
    length = len(password)
    all_digits = password.isdigit()

    if length < 8 and all_digits is False:
        return True
 
    return False

def check_strong_pw(password):
    length = len(password)
    all_digits = password.isdigit()
    has_a_digit = any(c.isdigit() for c in password)
    
    if length >= 8 and all_digits is False and has_a_digit is True:
        return True

    return False

def check_very_strong_pw(password):
    length = len(password)
    all_digits = password.isdigit()
    has_a_digit = any(c.isdigit() for c in password)
    has_a_special_char = any(not c.isalnum() for c in password)
    
    if length >= 8 and all_digits is False and has_a_digit is True and has_a_special_char is True:
        return True

    return False

def display_output(password, level):
    print(f'The password {password} is a ', end='')
    if level == PW_VERY_WEAK:
        print('very weak password.')
    elif level == PW_WEAK:
        print('weak password.')
    elif level == PW_STRONG:
        print('strong password.')
    elif level == PW_VERY_STRONG:
        print('very strong password.')

password = get_user_input()
level = password_validator(password)
display_output(password, level)