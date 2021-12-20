def sqrt_ternary_search(n):
    ans = 0

    for i in range(1, 11):
        for j in range(1, 11):
            if i == 1:
                tmp = j
            else:
                tmp = j / (10 ** (i - 1))

            tmp = ans + tmp

            if tmp * tmp > n:
                if i == 1:
                    ans = j - 1
                else:
                    ans = ans + (j - 1) / (10 ** (i - 1))

                break

    return ans

def main():
    answer = sqrt_ternary_search(10)
    print(f'The answer is {answer}.')

main()
