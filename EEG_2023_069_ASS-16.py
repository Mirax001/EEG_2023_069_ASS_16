# IMPORTS
import random
import time

# GENERATE SENSOR-LIKE DATA
sensor_data = [random.randint(1, 10000) for _ in range(1000)]

# ------------------ SEARCHING ALGORITHMS ------------------ #

# 1. LINEAR SEARCH (Algorithm 1)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 2. BINARY SEARCH (Algorithm 2) - works only on sorted lists
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ------------------ SORTING ALGORITHMS ------------------ #

# 3. BUBBLE SORT (Algorithm 3)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 4. MERGE SORT (Algorithm 4)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# 5. QUICK SORT (Algorithm 5)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# ------------------ TESTING ------------------ #

# Copy sensor data for sorting (to avoid modifying the original list)
import copy

# Sort using each method and time them
for name, sort_func in [
    ("Bubble Sort", bubble_sort),
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort)
]:
    test_data = copy.deepcopy(sensor_data)
    start = time.time()
    sorted_data = sort_func(test_data)
    end = time.time()
    print(f"{name} took {end - start:.5f} seconds")

# Test searches
sorted_sensor_data = sorted(sensor_data)  # for binary search

print("\nSearch Results:")
print("Linear Search Result:", linear_search(sensor_data, sensor_data[500]))
print("Binary Search Result:", binary_search(sorted_sensor_data, sensor_data[500]))