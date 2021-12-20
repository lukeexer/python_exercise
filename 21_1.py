MONTH_ENGLISH_01 = 1
MONTH_ENGLISH_02 = 2
MONTH_ENGLISH_03 = 3
MONTH_ENGLISH_04 = 4
MONTH_ENGLISH_05 = 5
MONTH_ENGLISH_06 = 6
MONTH_ENGLISH_07 = 7
MONTH_ENGLISH_08 = 8
MONTH_ENGLISH_09 = 9
MONTH_ENGLISH_10 = 10
MONTH_ENGLISH_11 = 11
MONTH_ENGLISH_12 = 12

def get_user_input():
    month = input('Please enter the number of the month: ') or '3'
    return validate_input(month)

def validate_input(month):
    try:
        month = int(str.strip(month))
    except:
        print('Please input a numeric value!')
        exit()

    if month <= 0 or month > 12:
        print('The valuse should between 1 to 12')
        exit()

    return month

def convert_to_english_month_name(month):
    converted_month = ''

    if month == MONTH_ENGLISH_01:
        converted_month = 'January'
    elif month == MONTH_ENGLISH_02:
        converted_month = 'February'
    elif month == MONTH_ENGLISH_03:
        converted_month = 'March'
    elif month == MONTH_ENGLISH_04:
        converted_month = 'Aprial'
    elif month == MONTH_ENGLISH_05:
        converted_month = 'May'
    elif month == MONTH_ENGLISH_06:
        converted_month = 'June'
    elif month == MONTH_ENGLISH_07:
        converted_month = 'July'
    elif month == MONTH_ENGLISH_08:
        converted_month = 'August'
    elif month == MONTH_ENGLISH_09:
        converted_month = 'September'
    elif month == MONTH_ENGLISH_10:
        converted_month = 'October'
    elif month == MONTH_ENGLISH_11:
        converted_month = 'November'
    elif month == MONTH_ENGLISH_12:
        converted_month = 'December'
    else:
        print('No matched value!')

    '''
    match (month):
        case (1):
            converted_month = 'January'
        case (2):
            converted_month = 'February'
        case (3):
            converted_month = 'March'
        case (4):
            converted_month = 'Aprial'
        case (5):
            converted_month = 'May'
        case (6):
            converted_month = 'June'
        case (7):
            converted_month = 'July'
        case (8):
            converted_month = 'August'
        case (9):
            converted_month = 'September'
        case (10):
            converted_month = 'October'
        case (11):
            converted_month = 'November'
        case (12):
            converted_month = 'December'
        case _:
            print('No matched value!')
    '''
    return converted_month

def display_output(month):
    print(f'The name of the month is {month}')

month = get_user_input()
converted_month = convert_to_english_month_name(month)
display_output(converted_month)

