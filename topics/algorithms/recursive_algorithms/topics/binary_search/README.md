Binary Search is a highly efficient algorithm for searching sorted arrays, with a time complexity of O(log n). It significantly reduces the search space by half with each step, making it much faster than linear search algorithms.

### Binary Search
```plaintext
function binarySearch(array, left, right, target)
    // Base case: The element is not present in the array
    if right < left
        return -1

    // Calculate mid index
    mid = left + (right - left) / 2

    // Base case: If the element is present at the middle itself
    if array[mid] == target
        return mid

    // If the element is smaller than mid, it can only be present in the left subarray
    if array[mid] > target
        return binarySearch(array, left, mid - 1, target)

    // Else the element can only be present in the right subarray
    return binarySearch(array, mid + 1, right, target)
```
**Explanation:**
- **Base Case (`if right < left`)**: If the right index is less than the left index, the target is not present in the array. Return -1 to indicate the target is not found.
- **Calculate Mid Index (`mid = left + (right - left) / 2`)**: Determine the middle element of the current subarray. The formula avoids integer overflow, a common issue in `(left + right) / 2`.
- **Base Case (`if array[mid] == target`)**: If the element at the mid index is the target, return the mid index, indicating the target has been found.
- **Recursive Case - Left Subarray (`if array[mid] > target`)**: If the target is less than the element at mid, recursively search in the left subarray.
- **Recursive Case - Right Subarray**: If the target is greater than the element at mid, recursively search in the right subarray.

