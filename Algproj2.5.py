# Algorithms Project 2
# Joshua Barber
# Braeden Myers
# Ian McGinnes

import random
import time

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
    
# initializes arrays
arr1 = []
arr2 = []
arr3 = []
arr4 = []

k = 1000
# generates a random array length k and copies it to 3 others
for i in range(k):
    arr1.append(random.randint(1, 2*k))
    arr2.append(random.randint(1, 2*k))
    arr3.append(random.randint(1, 2*k))



# Merge Sort Testing
MergeSortBest = 10
MergeSortWorst = 0
# runs through a for loop 20 times collecting times each time
# and comparing the best and worst time each iteration
for i in range(20):
    # makes a new randomized array b/c merge sort time is data dependent
    for i in range (k):
        arr4.append(random.randint(1, 2*k))
    t0 = time.perf_counter()
    sortedList = merge_sort(arr4)
    t1 = time.perf_counter()
    if MergeSortBest > (t1-t0):
        MergeSortBest = (t1-t0)
    if MergeSortWorst < (t1-t0):
        MergeSortWorst = (t1-t0)
# records average time for merge sort
t0 = time.perf_counter()
sortedList = merge_sort(arr1)
t1 = time.perf_counter()
print('Merge sort: ')
print('Best  Case:', round(MergeSortBest,7), 'seconds.')
print('Avg   Case:', round(t1-t0, 7), 'seconds.')
print('Worst Case:', round(MergeSortWorst,7), 'seconds.\n')



# Quick Sort Testing
QuickSortBest = 10
QuickSortWorst = 0
# runs through a for loop 20 times collecting times each time
# and comparing the best and worst time each iteration
for i in range(20):
    # makes a new randomized array b/c quick sort time is data dependent
    for i in range (k):
        arr4.append(random.randint(1, 2*k))
    t0 = time.perf_counter()
    sortedList = quick_sort(arr4)
    t1 = time.perf_counter()
    if QuickSortBest > (t1-t0):
        QuickSortBest = (t1-t0)
    if QuickSortWorst < (t1-t0):
        QuickSortWorst = (t1-t0)
# records average time for merge sort
t0 = time.perf_counter()
sortedList = quick_sort(arr2)
t1 = time.perf_counter()
print('Quick sort: ')
print('Best  Case:', round(QuickSortBest,7), 'seconds.')
print('Avg   Case:', round(t1-t0, 7), 'seconds.')
print('Worst Case:', round(QuickSortWorst,7), 'seconds.\n')



#print('Selection sort: (Worst case might take a minute')
# records time for selection sort
#t0 = time.perf_counter()
#sortedList = selection_sort(arr3)
#t1 = time.perf_counter()
#print('Best  Case:', d, 'items costs', round(t1-t0, 5), 'seconds.')



# creates arrays to test bubble sort
a = 100;
b = 1000;
c = 10000;
bubbleSortBest = []
bubbleSortAvg = []
bubbleSortWorst = []
for i in range(a):
    bubbleSortBest.append(random.randint(1, 2*a))
for i in range(b):
    bubbleSortAvg.append(random.randint(1, 2*b))
for i in range(c):
    bubbleSortWorst.append(random.randint(1, 2*c))
print('Bubble sort: (Worst case might take a minute')
# records time for bubble sort best case
t0 = time.perf_counter()
sortedList = bubbleSort(bubbleSortBest)
t1 = time.perf_counter()
print('Best  Case:', a, 'items costs', round(t1-t0, 5), 'seconds.')
# records time for bubble sort average case
t0 = time.perf_counter()
sortedList = bubbleSort(bubbleSortAvg)
t1 = time.perf_counter()
print('Avg   Case:', b, 'items costs', round(t1-t0, 5), 'seconds.')
# records time for bubble sort worst case
t0 = time.perf_counter()
sortedList = bubbleSort(bubbleSortWorst)
t1 = time.perf_counter()
print('Worst Case:', c, 'items costs', round(t1-t0, 5), 'seconds.\n')
