def quicksort(arr, start, end):                 # to call the partition function to divide the array in half
    if start < end:                             # if the starting index and ending index until not same
        pIndex = partition(arr, start, end)       # getting index from half of the partition function
        quicksort(arr, start, pIndex-1)           # calling first half of the quick sort function
        quicksort(arr, pIndex+1, end)           # calling next half of the quick sort function


def partition(arr, start, end):           # calling to partition and sort the elements in the array
    pivot = arr[end]                 # storing the pivot element always as last element
    pIndex = start                 # partition index is always the starting index to iterate in loop

    for i in range(start, end):          # for index from starting to ending
        if arr[i] <= pivot:             # if the element at that place is less than the pivot element
            arr[i], arr[pIndex] = arr[pIndex], arr[i]       # if the condition is true then swap the element next to it
            pIndex += 1           # and increment the pindex to check with next number

    arr[pIndex], arr[end] = arr[end], arr[pIndex]        # at the end swap the pivot element and index where it stopped.
    return pIndex           # return the pivotindex to the quicksort function


a = [int(x) for x in input().split()]
quicksort(a, 0, len(a)-1)
print(a)
