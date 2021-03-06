def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[: len(arr)//2]   # we are slicing the list from beginning to the mid element
        right_arr = arr[len(arr)//2:]   # we are slicing the right array from middle to end of the element

        # call merge sort recursively
        merge_sort(left_arr)
        merge_sort(right_arr)

        # sort the array
        i = 0      # to keep the track of left most element in left array
        j = 0     # to keep the track of the left most element in right array
        k = 0     # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1      # it gets incremented for every while operation
        while i < len(left_arr):        # we only write these two methods because maybe i or j is completed and left ele
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


print("Enter the list of elements: ")
arr1 = [int(x) for x in input().split()]
merge_sort(arr1)
print("The sorted Array: ", arr1)
