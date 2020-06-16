# TO-DO: Complete the selection_sort() function below
# O(n^2) runtime | O(1) space
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        while cur_index < len(arr):
            if arr[cur_index] < arr[smallest_index]:
                smallest_index = cur_index
            cur_index += 1

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below
# average O(n^2) runtime | O(1) space
def bubble_sort(arr):
    swapped = True
    iterations = 0
    while swapped:
        swapped = False
        for i in range(1, len(arr) - iterations):
            current = arr[i]
            prev = arr[i - 1]
            if current < prev:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        iterations += 1
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# O(n + m) runtime | O(m) space
# where n is the size of arr, and
# where m is the max num in arr
def counting_sort(arr, maximum=None):
    if not arr: return arr

    buckets = [0] * (max(arr) + 1)

    while len(arr):
        next_num = arr.pop()
        if next_num < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        buckets[next_num] += 1

    for i in range(len(buckets)):
        while buckets[i] > 0:
            buckets[i] -= 1
            arr.append(i)

    return arr
