# MergeSortPython
 Use Python do Merge Sort

This program is a simple implementation of the merge sort algorithm to sort an array of integers. It generates a random array of size 10 with values between 0 and 100 using the random_array method. Then, it prints the original array, sorts it using the merge sort algorithm, and finally prints the sorted array.

Usage
To run the program, execute the Python script task_manager.py.

bash
Copy code
python task_manager.py
Methodology
main()
The main() function is the entry point of the program.
It creates a random array, prints it, sorts it using the merge sort algorithm, and then prints the sorted array.
random_array()
The random_array() function generates a random integer array of size 10 with values between 0 and 100.
merge_sort(arr)
The merge_sort(arr) function implements the merge sort algorithm to sort the given array arr.
It recursively divides the array into smaller subarrays, sorts them individually, and then merges them back together in sorted order.
merge(arr, left_array, right_array)
The merge(arr, left_array, right_array) function merges two sorted arrays (left_array and right_array) into a single sorted array (arr).
print_array(arr)
The print_array(arr) function prints the elements of the given array arr.
