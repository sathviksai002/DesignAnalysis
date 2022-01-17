def merge_sort(arr):
    left_array = arr[:len(arr)//2]
    right_array = arr[len(arr)//2:]

    i = 0     # index for left array left element
    j = 0     # index for right array left element
    k = 0     # index for merged array elements

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1
    while i < len(left_array):
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        arr[k] = right_array[j]
        j += 1
        k += 1


print("Enter the list of elements: ")
arr1 = [int(x) for x in input().split()]
merge_sort(arr1)
print("The sorted array is: ", arr1)