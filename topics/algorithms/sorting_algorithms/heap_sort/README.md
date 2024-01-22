Heap Sort is particularly useful for its guaranteed O(n log n) time complexity, making it suitable for large datasets. Unlike Merge Sort, it doesn't require additional space, which makes it more memory efficient.

### Heap Sort
```plaintext
function heapSort(array)
    arrayLength = length(array)  // Get the number of elements in the array

    // Build a max heap from the array
    for i from (arrayLength / 2) - 1 to 0 step -1
        heapify(array, arrayLength, i)

    // Extract elements from the heap one by one
    for i from arrayLength - 1 to 0 step -1
        // Move the current root to the end (since it's the largest)
        swap(array[0], array[i])
        // Call heapify on the reduced heap
        heapify(array, i, 0)
    // The array is now sorted
    return array

function heapify(array, heapSize, rootIndex)
    largest = rootIndex  // Initialize largest as root
    leftChild = 2 * rootIndex + 1  // left = 2*i + 1
    rightChild = 2 * rootIndex + 2  // right = 2*i + 2

    // If left child is larger than root
    if leftChild < heapSize and array[leftChild] > array[largest]
        largest = leftChild

    // If right child is larger than largest so far
    if rightChild < heapSize and array[rightChild] > array[largest]
        largest = rightChild

    // If largest is not root
    if largest != rootIndex
        swap(array[rootIndex], array[largest])
        // Recursively heapify the affected sub-tree
        heapify(array, heapSize, largest)
```
**Explanation:**
- **arrayLength = length(array)**: Determine the size of the array.
- **for i from (arrayLength / 2) - 1 to 0 step -1**: Build a max heap. Start from the last non-leaf node and heapify each node in a bottom-up manner.
- **heapify(array, arrayLength, i)**: Ensure the subtree rooted at index `i` obeys the max heap property.
- **for i from arrayLength - 1 to 0 step -1**: Extract elements from the heap one by one. The largest element in the heap is at the root, and we move it to the end of the array.
- **swap(array[0], array[i])**: Move the current root to the end, as it's the largest.
- **heapify(array, i, 0)**: Call heapify on the reduced heap to ensure the max heap property is maintained.
- **leftChild = 2 * rootIndex + 1, rightChild = 2 * rootIndex + 2**: Calculate the indices of the left and right children of the current node.
- **if leftChild < heapSize and array[leftChild] > array[largest]**: Check if the left child is larger than the current largest.
- **if rightChild < heapSize and array[rightChild] > array[largest]**: Check if the right child is larger than the current largest.
- **if largest != rootIndex**: If the largest is not the current root, swap them and recursively heapify the affected subtree.

