def get_user_input():
    price1 = input('Enter the price of item 1:') or 25
    quantity1 = input('Enter the quantity of item 1:') or 2
    price2 = input('Enter the price of item 2:') or 10
    quantity2 = input('Enter the quantity of item 2:') or 1
    price3 = input('Enter the price of item 3:') or 4
    quantity3 = input('Enter the quantity of item 3:') or 1

    return validate_input(price1, quantity1, price2, quantity2, price3, quantity3)

def validate_input(price1, quantity1, price2, quantity2, price3, quantity3):
    try:
        (price1, price2, price3) = (float(price1), float(price2), float(price3))
    except:
        print('Please input numeric value for item price!')
        exit()

    try:
        (quantity1, quantity2, quantity3) = (int(quantity1), int(quantity2), int(quantity3))
    except:
        print('Please input numeric value for item quantity!')
        exit()

    return (price1, quantity1, price2, quantity2, price3, quantity3)

def calculate_order(price1, quantity1, price2, quantity2, price3, quantity3):
    subtotal = price1 * quantity1 + price2 * quantity2 + price3 * quantity3
    tax = subtotal * 5.5 / 100
    total = subtotal + tax

    return (subtotal, tax, total)

def display_output(subtotal, tax, total):
    print(f'Subtotal: {subtotal}')
    print(f'Tax: {tax}')
    print(f'Total: {total}')

(price1, quantity1, price2, quantity2, price3, quantity3) = get_user_input()
(subtotal, tax, total) = calculate_order(price1, quantity1, price2, quantity2, price3, quantity3)
display_output(subtotal, tax, total)