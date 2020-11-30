
def binary_search(arr,target):

    mid = len(arr)//2

    try:
        if arr[mid] > target:
            return binary_search(arr[:mid], target)

        elif arr[mid] < target:
            return binary_search(arr[mid+1:], target)

        elif arr[mid] == target:
            return arr[mid]
    except IndexError as err:
        pass

        print("Value: %d is not in array" % target)

def main():
    arr = [1,2,3,4,5,6,7,8,9,10, 1000000]
    for value in range(1, 11):
        print(binary_search(arr, value))
    binary_search(arr, 0)
    binary_search(arr, 11)
    binary_search(arr, 12)
    binary_search(arr, 6)
    binary_search(arr, -5)
    binary_search(arr, 1000000)


main()
