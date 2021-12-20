def is_employee_exist(emp_list, emp_name):
    for name in emp_list:
        if name == emp_name:
            return True

    return False

def generate_employee_list():
    emp_list = []
    emp_list.append('John Smith')
    emp_list.append('Jackie Jackson')
    emp_list.append('Chris Jones')
    emp_list.append('Amanda Cullen')
    emp_list.append('Jeremy Goodwin')

    return emp_list

def display_employee_list(emp_list):
    print(f'There are {len(emp_list)} employees.')

    for i in emp_list:
        print(i)

def delete_employee(emp_list, emp_name):
    index = 0

    for i, name in enumerate(emp_list):
        if name == emp_name:
            index = i

    del emp_list[index]

def main():
    emp_list = generate_employee_list()

    while True:
        display_employee_list(emp_list)

        emp_name = input('Enter an employee name to remove: ')

        is_valid = is_employee_exist(emp_list, emp_name)

        if is_valid is False:
            print('Employee not found!')
            continue

        delete_employee(emp_list, emp_name)

main()
