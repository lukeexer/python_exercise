def pascal_triangle(n):
    # arr = [[0] * n] * n # Wrong!! You will get n copies of an one dimentional arraies
    arr = [[0 for x in range(n)] for y in range(n)]

    for i in range(0, n):
        arr[i][0] = 1

    for i in range(0, n):
        arr[i][i] = 1

    for i in range(1, n):
        for j in range(1, i + 1):
            if j != 0 and i != j:
                arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]

    return arr

def print_pascal_triangle(arr, n):
    for i in range(0, n):
        for j in range(0, n):
            print(f'{arr[i][j]} ', end='')

        print('\n')

def main():
    n = 10
    arr = pascal_triangle(n)
    print_pascal_triangle(arr, n)

main()
