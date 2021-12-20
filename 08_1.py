def get_user_input():
    num_people = input('How many people?') or '8'
    num_pizza = input ('How many pizzas do you have?') or '2'
    return validate_input(num_people, num_pizza)

def validate_input(num_people, num_pizza):
    try:
        (num_people, num_pizza) = (int(num_people), int(num_pizza))
    except:
        print('Please input numeric values!')
        exit()

    return (num_people, num_pizza)

def calculate_pizza_per_person(num_people, num_pizza):
    return num_pizza * 8 / num_people

def calculate_pizza_leftover(num_people, num_pizza):
    return num_pizza * 8 % num_people

def display_output(num_people, num_pizza):
    print(f'{num_people} people with {num_pizza} pizzas')

    if calculate_pizza_per_person(num_people, num_pizza) > 1:
        print(f'Each person get {calculate_pizza_per_person(num_people, num_pizza):.0f} pieces of pizza.')
    else:
        print(f'Each person get {calculate_pizza_per_person(num_people, num_pizza):.0f} piece of pizza.')
    
    if calculate_pizza_leftover(num_people, num_pizza) > 1:
        print(f'There are {calculate_pizza_leftover(num_people, num_pizza)} leftover pieces.')
    else:
        print(f'There is {calculate_pizza_leftover(num_people, num_pizza)} leftover piece.')


(num_people, num_pizza) = get_user_input()
display_output(num_people, num_pizza)