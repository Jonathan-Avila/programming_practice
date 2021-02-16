
def binary_search(arr,target, a_dict = {}):
    mid = len(arr)//2
    if a_dict == {}:
        for index, element in enumerate(arr):
            a_dict[element] = index
    try:
        if arr[mid] == target:
            return a_dict[target]

        elif arr[mid] > target:
            return binary_search(arr[:mid], target, a_dict)

        elif arr[mid] < target:
            return binary_search(arr[mid+1:], target, a_dict)

    except IndexError as err:
        pass

        #print("Value: %d is not in array" % target)
        return -1
def main():

    arr = [5]
    print(binary_search(arr, 5))
    '''
    arr = [1,2,3,4,5,6,7,8,9,10, 1000000]
    print(binary_search(arr, value))

    for value in range(1, 12):
        print(binary_search(arr, value))
    binary_search(arr, 0)
    binary_search(arr, 11)
    binary_search(arr, 12)
    binary_search(arr, 6)
    binary_search(arr, -5)
    binary_search(arr, 1000000)


    #binary_search(arr, 10)
    '''



main()
