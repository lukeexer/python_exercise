def arr_max(arr):
    if len(arr) == 1:
        return arr[0]
        
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    else:
        tmp_val = arr_max(arr[1:])

        if arr[0] > tmp_val:
            return arr[0]
        else:
            return tmp_val

def main():
    print(arr_max([4, 8, 10, 3]))
    #print(arr_max([4]))
    #print(arr_max([]))

main()
