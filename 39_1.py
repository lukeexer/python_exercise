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

def sort_by_last_name(emp_list):
    length = len(emp_list)
    for _ in range(length - 1):
        for j in range(length - 1):
            if emp_list[j]['last_name'] > emp_list[j + 1]['last_name']:
                tmp = emp_list[j]
                emp_list[j] = emp_list[j + 1]
                emp_list[j + 1] = tmp

    return emp_list

def display_output(sorted_list):
    print('Name\t\t\t| Position\t| Separation Date')
    print('----------------------------------------------------------')
    for emp in sorted_list:
        print(f"{emp['first_name']} {emp['last_name']}\t\t| {emp['position']}\t| \
            {emp['separation_date']}")

def main():
    emp_list = get_data()
    sorted_list = sort_by_last_name(emp_list)
    display_output(sorted_list)

main()
