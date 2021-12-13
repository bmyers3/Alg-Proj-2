# Algorithms Project 2
# Joshua Barber
# Braeden Myers
# Ian McGinnes

import random
import time

def main():
    # gets length of array from user
    k = int(input("Enter the length of the randomly generated array: "))
    if k > 1000:
        print('\n\tSelection and Bubble sort might take a little bit...\n')
    # initializes arrays
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    # generates a random array length k and copies it to 3 others
    for i in range(k):
        arr1.append(random.randint(1, 2*k))
        arr2.append(random.randint(1, 2*k))
        arr3.append(random.randint(1, 2*k))
        arr4.append(random.randint(1, 2*k))
    # records time for merge sort
    t3 = time.perf_counter()
    sortedList = merge_sort(arr2)
    t4 = time.perf_counter()
    print('Merge sort', k, 'items costs', t4-t3, 'seconds.')
    # records time for quick sort
    t5 = time.perf_counter()
    sortedList = quick_sort(arr3)
    t6 = time.perf_counter()
    print('Quick sort', k, 'items costs', t6-t5, 'seconds.')
    # records time for selection sort
    t7 = time.perf_counter()
    sortedList = selection_sort(arr4)
    t8 = time.perf_counter()
    print('Selection sort', k, 'items costs', t8-t7, 'seconds.')
    # records time for bubble sort (put at the end because it usually takes the longest)
    t1 = time.perf_counter()
    sortedList = bubbleSort(arr1)
    t2 = time.perf_counter()
    print('Bubble sort', k, 'items costs', t2-t1, 'seconds.\n')
    # recalls main for user to run again with a different k value
    main()
if __name__ == '__main__':
    main()

# Bubble Sort Algorithm
def bubbleSort(myList):
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j+1] = \
                    myList[j + 1], myList[j]
    return myList

# Merge Sort Algorithm
def merge_sort(m):
    if len(m) <= 1:
        return m
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

# Used in merge sort
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

# Used in quick sort
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

# Used in quick sort
def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

# Quick sort Algorithm
def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    return quick_sort_recursion(array, begin, end)

# Selection Sort Algorithm
def selection_sort(arr):        
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr
