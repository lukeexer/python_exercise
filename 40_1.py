def get_data():
    emp_list = [{'first_name': 'John', 'last_name': 'Johnson',
                    'position': 'Manager', 'separation_date': '2016-12-31'},
                {'first_name': 'Tou', 'last_name': 'Xiong',
                    'position': 'Software Engineer', 'separation_date': '2016-10-05'},
                {'first_name': 'Michaela', 'last_name': 'Michaelson',
                    'position': 'District Manager', 'separation_date': '2015-12-19'},
                {'first_name': 'Jake', 'last_name': 'Jacobson',
                    'position': 'Programmer', 'separation_date': ''},
                {'first_name': 'Jacquelyn', 'last_name': 'Jackson',
                    'position': 'DBA', 'separation_date': ''},
                {'first_name': 'Sally', 'last_name': 'Weber',
                    'position': 'Web Developer', 'separation_date': '2015-12-18'}]
    return emp_list

def get_user_input():
    search_str = input('Enter a search string: ') or 'Jac'

    return search_str

def search_employee(emp_list, search_str):
    result_list = []
    for emp in emp_list:
        if search_str in emp['first_name'] or search_str in emp['last_name']:
            result_list.append(emp)

    return result_list

def display_output(result_list):
    print('Name\t\t\t| Position\t| Separation Date')
    print('----------------------------------------------------------')
    for emp in result_list:
        print(f"{emp['first_name']} {emp['last_name']}\t\t| {emp['position']}\t| \
            {emp['separation_date']}")

def main():
    emp_list = get_data()
    search_str = get_user_input()
    result_list = search_employee(emp_list, search_str)
    display_output(result_list)

main()
