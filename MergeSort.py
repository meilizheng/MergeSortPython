import random

def main():
    # Creates a new integer array using the random_array method.
    test_array = random_array()
    print("Original array: ", end="")
    
    # Prints the original array.
    print_array(test_array)

    # Merge and sort the original array.
    merge_sort(test_array)
    print("\nSorted Array: ")

    # Print out the sorted array.
    print_array(test_array)

# Random Array Method
def random_array():
    # Generates a random integer array of size 10 with values between 0 and 100.
    min_num = 0
    max_num = 101
    size = 10
    arr = [random.randint(min_num, max_num) for _ in range(size)]
    return arr

# MergeSort Method with int[] array parameter
def merge_sort(arr):
    arr_length = len(arr)

    # Checks if the array is already sorted (length <= 1) and prints a message.
    if arr_length <= 1:
        print("Array already sorted.")
        return

    # Divides the array into left and right parts.
    middle_array = arr_length // 2
    left_array = arr[:middle_array]
    right_array = arr[middle_array:]

    # Print out the left and right array.
    print("Left Array:")
    print_array(left_array)
    print("Right Array:")
    print_array(right_array)

    # Recursively calls merge_sort on left and right parts.
    print("Sorting left array:")
    merge_sort(left_array)
    print("Sorting right array:")
    merge_sort(right_array)

    print("Merge Sorted Arrays:")
    # Merges and sorts the left and right arrays using the merge method.
    merge(arr, left_array, right_array)

# Merge and sort
def merge(arr, left_array, right_array):
    left_length = len(left_array)
    right_length = len(right_array)
    left_array_index = right_array_index = sorted_array_index = 0

    # Merges and sorts two arrays (left and right) into a single array.
    while left_array_index < left_length and right_array_index < right_length:
        if left_array[left_array_index] <= right_array[right_array_index]:
            arr[sorted_array_index] = left_array[left_array_index]
            left_array_index += 1
        else:
            arr[sorted_array_index] = right_array[right_array_index]
            right_array_index += 1
        sorted_array_index += 1

    # Uses indices to traverse through left, right, and sorted arrays.
    while left_array_index < left_length:
        arr[sorted_array_index] = left_array[left_array_index]
        left_array_index += 1
        sorted_array_index += 1

    while right_array_index < right_length:
        arr[sorted_array_index] = right_array[right_array_index]
        right_array_index += 1
        sorted_array_index += 1

# Print out the arr.
def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    main()
