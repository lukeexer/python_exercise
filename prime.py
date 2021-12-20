def create_prime_table():
    table = [True] * 10
    table[0] = False
    table[1] = False
    table[2] = True

    for i in range(2, 10):
        for j in range(2, i):
            if i % j == 0:
                table[i] = False
                break

    return table

print(create_prime_table())
