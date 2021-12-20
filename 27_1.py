def get_user_input():
    # first_name = input('Enter the first name: ') or 'Jimmy'
    # last_name = input('Enter the last name: ') or 'James'
    # zip_code = input('Enter the ZIP code: ') or '55555'
    # employee_id = input('Enter an employee ID: ') or 'TK-4213'
    first_name = input('Enter the first name: ') or 'J'
    last_name = input('Enter the last name: ') or ''
    zip_code = input('Enter the ZIP code: ') or 'ABCDE'
    employee_id = input('Enter an employee ID: ') or 'A12-1234'
    return validate_input(first_name, last_name, zip_code, employee_id)

def validate_input(first_name, last_name, zip_code, employee_id):
    has_error = False
    message = ''

    (has_error, message) = validate_first_name(has_error, message, first_name)
    (has_error, message) = validate_last_name(has_error, message, last_name)
    (has_error, message) = validate_zip_code(has_error, message, zip_code)
    (has_error, message) = validate_employee_id(has_error, message, employee_id)

    if has_error is False:
        message = 'There were no errors found.'

    print(message)

def validate_first_name(has_error, message, first_name):
    first_name = str.strip(first_name)

    if first_name == '':
        message += 'The first name must be filled in.\n'
        has_error = True
        return (has_error, message)

    if len(first_name) < 2:
        message += f'{first_name} is not a valid first name. It is too short.\n'
        has_error = True
        return (has_error, message)

    return (has_error, message)

def validate_last_name(has_error, message, last_name):
    last_name = str.strip(last_name)

    if last_name == '':
        message += 'The last_name must be filled in.\n'
        has_error = True
        return (has_error, message)

    if len(last_name) < 2:
        message += f'{last_name} is not a valid last name. It is too short.\n'
        has_error = True
        return (has_error, message)
    
    return (has_error, message)

def validate_zip_code(has_error, message, zip_code):
    zip_code = str.strip(zip_code)

    try:
        int(zip_code)
    except:
        message += 'The ZIP code must be a numeric.\n'
        has_error = True

    return (has_error, message)

def validate_employee_id(has_error, message, employee_id):
    employee_id = str.strip(employee_id)

    if employee_id[2] != '-':
        message += f'{employee_id} is not a valid ID.\n'
        has_error = True
        return (has_error, message)

    if str.isdigit(employee_id[3:]) is False:
        message += f'{employee_id} is not a valid ID.\n'
        has_error = True
        return (has_error, message)

    if str.isalpha(employee_id[:2]) is False:
        message += f'{employee_id} is not a valid ID.\n'
        has_error = True
        return (has_error, message)

    return (has_error, message)

get_user_input()