def bubble_sort(array):
    """
 Sorts an array using the bubble sort algorithm.

 Args:
   array: The array to sort.

 Returns:
   The sorted array.
 """

    # Get the number of elements in the array
    array_length = len(array)

    # Outer loop - manages the number of passes
    for i in range(array_length - 1):
        # Inner loop - performs the comparison in each pass
        for j in range(array_length - i - 1):
            # Compare adjacent elements
            if array[j] > array[j + 1]:
                # Swap if they are in wrong order
                array[j], array[j + 1] = array[j + 1], array[j]

    # The array is now sorted
    return array


# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = bubble_sort(data)
print(sorted_data)  # Output: [11, 12, 22, 25, 34, 64, 90]
