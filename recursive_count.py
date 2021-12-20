def count_arr(arr):
    if len(arr) == 0:
        return 0
    else:
        arr.pop(0)
        return 1 + count_arr(arr)

def main():
    #print(count_arr([1, 2, 3, 4]))
    print(count_arr([1]))
    #print(count_arr([]))

main()
