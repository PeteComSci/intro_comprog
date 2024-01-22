Bucket Sort is particularly useful when the input is uniformly distributed over a range. It has an average-case and best-case time complexity of O(n + k), but its worst-case time complexity is O(n²) if all elements are placed into a single bucket.

### Bucket Sort
```plaintext
function bucketSort(array)
    arrayLength = length(array)  // Get the number of elements in the array
    bucketCount = 10  // Number of buckets
    buckets = array of bucketCount lists, each list is empty  // Initialize buckets

    // Step 1: Place each element in its respective bucket
    for i from 0 to arrayLength - 1
        index = arrayLength * array[i]  // Determine the bucket for this element
        append array[i] to buckets[index]

    // Step 2: Sort individual buckets using a suitable sorting algorithm
    for i from 0 to bucketCount - 1
        sort buckets[i]  // Sort the individual bucket

    // Step 3: Concatenate the sorted buckets
    k = 0
    for i from 0 to bucketCount - 1
        for element in buckets[i]
            array[k] = element
            k = k + 1
    // The array is now sorted
    return array
```
**Explanation:**
- **arrayLength = length(array)**: Determine the size of the array.
- **bucketCount = 10**: Define the number of buckets (can vary depending on the distribution of your data).
- **buckets = array of bucketCount lists**: Initialize an array of empty lists (buckets).
- **for i from 0 to arrayLength - 1**: Iterate through the array to distribute all elements into buckets.
- **index = arrayLength * array[i]**: Calculate the bucket index for the current element. The formula can vary based on the data distribution and the range of input.
- **append array[i] to buckets[index]**: Add the element to its respective bucket.
- **for i from 0 to bucketCount - 1; sort buckets[i]**: Sort individual buckets. You can use any sorting algorithm. Some implementations use insertion sort due to its efficiency with small data sets.
- **for i from 0 to bucketCount - 1; for element in buckets[i]**: Concatenate the sorted buckets back into the original array.

