def get_max_element(arr):
    curr_val = arr[0]
    index = 0

    for i, _ in enumerate(arr):
        if arr[i] > curr_val:
            curr_val = arr[i]
            index = i

    return arr.pop(index)

def selection_sort(arr):
    result_arr = []

    for _ in range(0, len(arr)):
        result_arr.append(get_max_element(arr))

    return result_arr

def main():
    print(selection_sort([5, 2, 3, 2, 6, 2, 10]))

main()
    