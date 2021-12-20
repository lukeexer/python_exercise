
def sum_arr(arr):
    if len(arr) == 0:
        return 0
    else:
        element =  arr.pop(0)
        return element + sum(arr)

def main():
    #print(sum([1, 2, 3, 4]))
    print(sum([1]))
    print(sum([]))

main()
