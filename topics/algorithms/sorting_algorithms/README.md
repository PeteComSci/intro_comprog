# Sorting Algorithms

Sorting algorithms are fundamental in the field of computer science and are used to order elements in a list or array according to a specific order. Here's a list of some common sorting algorithms, each with its own unique mechanisms and use-cases:

**[Bubble Sort](https://github.com/Pete-ComSci/sorting_algorithms/tree/aee04d6e5bee71c9db49c54d927f4909a6b335ac/bubble_sort)**: A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. Best suited for small datasets or nearly sorted data.

**[Selection Sort](https://github.com/Pete-ComSci/sorting_algorithms/tree/aee04d6e5bee71c9db49c54d927f4909a6b335ac/selection_sort)**: Works by repeatedly selecting the minimum element from the unsorted part and moving it to the sorted part. It's not suitable for large datasets due to its high time complexity.

**[Insertion Sort](https://github.com/Pete-ComSci/sorting_algorithms/tree/aee04d6e5bee71c9db49c54d927f4909a6b335ac/insertion_sort)**: Builds the final sorted array one item at a time. It's efficient for small data sets and mostly sorted arrays but not suitable for large datasets.

**[Merge Sort](https://github.com/Pete-ComSci/sorting_algorithms/tree/aee04d6e5bee71c9db49c54d927f4909a6b335ac/merge_sort)**: A divide and conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. It has a consistently good performance but requires additional memory for the merging process.

**[Quick Sort](https://github.com/Pete-ComSci/sorting_algorithms/tree/aee04d6e5bee71c9db49c54d927f4909a6b335ac/quick_sort)**: Another divide and conquer algorithm. It picks an element as a pivot and partitions the array around the pivot. It's faster for large datasets but its performance depends heavily on the choice of the pivot.

**[Heap Sort](https://github.com/Pete-ComSci/sorting_algorithms/tree/aee04d6e5bee71c9db49c54d927f4909a6b335ac/heap_sort)**: Builds a heap from the input data, and then repeatedly extracts the maximum element from the heap and rebuilds the heap until the list is sorted. It's great for large data sets but not as fast as quick sort in practice.

**[Counting Sort](https://github.com/Pete-ComSci/sorting_algorithms/tree/aee04d6e5bee71c9db49c54d927f4909a6b335ac/counting_sort)**: An integer sorting algorithm that operates by counting the number of objects that have distinct key values, and using arithmetic to determine the positions of each key. It's efficient for small, integer-based datasets but uses a lot of memory for large ranges of keys.

**[Radix Sort](https://github.com/Pete-ComSci/sorting_algorithms/tree/aee04d6e5bee71c9db49c54d927f4909a6b335ac/radix_sort)**: Works by processing each digit of the numbers in the list, from least significant to most significant. It's fast for large lists of numbers with a small number of digits.

**[Bucket Sort](https://github.com/Pete-ComSci/sorting_algorithms/tree/aee04d6e5bee71c9db49c54d927f4909a6b335ac/bucket_sort)**: Distributes the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or by recursively applying the bucket sort.

**[Shell Sort](https://github.com/Pete-ComSci/sorting_algorithms/tree/aee04d6e5bee71c9db49c54d927f4909a6b335ac/shell_sort)**: A variant of insertion sort that allows the exchange of items that are far apart. The idea is to arrange the list of elements so that, starting anywhere, taking every hth element produces a sorted list.

**[Tim Sort](https://github.com/Pete-ComSci/sorting_algorithms/tree/aee04d6e5bee71c9db49c54d927f4909a6b335ac/tim_sort)**: Derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data. It's a stable, adaptive, and iterative mergesort that requires fewer comparisons when the input is partially sorted.

**[Comb Sort](https://github.com/Pete-ComSci/sorting_algorithms/tree/aee04d6e5bee71c9db49c54d927f4909a6b335ac/comb_sort)**: An improvement on bubble sort. The basic idea is to eliminate turtles, or small values near the end of the list, since in a bubble sort these slow the sorting down tremendously.

Each sorting algorithm has its own strengths and weaknesses, and the choice of sorting algorithm can depend on various factors including the size of the dataset, the nature of the data, and the specific requirements of the application.

Understanding the best use case for each algorithm can help in choosing the most efficient one for a given task.
The following table includes the best scenarios for using each algorithm over the others. 

| Algorithm     | Explanation   | Example Before | Example After | Best Case | Average Case | Worst Case | Best Usage Scenario |
|---------------|---------------|----------------|---------------|-----------|--------------|------------|---------------------|
| Bubble Sort   | Repeatedly swaps adjacent elements if they are in the wrong order. | [5, 3, 8, 4, 2] | [2, 3, 4, 5, 8] | O(n) | O(n²) | O(n²) | Small datasets or when data is almost sorted. Easy to implement. |
| Selection Sort | Selects the minimum element and moves it to the beginning. | [29, 10, 14, 37, 13] | [10, 13, 14, 29, 37] | O(n²) | O(n²) | O(n²) | Small datasets. Not influenced by the order of data (stable time complexity). |
| Insertion Sort | Builds the final sorted array one item at a time. | [22, 11, 99, 88, 9] | [9, 11, 22, 88, 99] | O(n) | O(n²) | O(n²) | Small or nearly sorted datasets. Useful for data sets that are continuously being added to. |
| Merge Sort     | Divides the array into halves, sorts them, and merges them. | [38, 27, 43, 3, 9] | [3, 9, 27, 38, 43] | O(n log n) | O(n log n) | O(n log n) | Large datasets. Ensures stable sort and consistent O(n log n) performance. |
| Quick Sort     | Picks a pivot and partitions the array around the pivot. | [33, 21, 45, 64, 55] | [21, 33, 45, 55, 64] | O(n log n) | O(n log n) | O(n²) | Large datasets where average case O(n log n) performance is acceptable. Not stable but can be quick with good pivot selection. |
| Heap Sort      | Converts the array into a heap and then sorts it. | [41, 39, 33, 18, 27] | [18, 27, 33, 39, 41] | O(n log n) | O(n log n) | O(n log n) | Large datasets. Good when you need guaranteed O(n log n) performance without extra space for merge sort. |
| Counting Sort  | Counts occurrences of each value to sort. | [1, 4, 1, 2, 7, 5, 2] | [1, 1, 2, 2, 4, 5, 7] | O(n+k) | O(n+k) | O(n+k) | Small integer range (k) relative to the number of items (n). Very efficient when k is not significantly greater than n. |
| Radix Sort     | Sorts the numbers digit by digit starting from least significant digit. | [170, 45, 75, 90, 802, 24, 2, 66] | [2, 24, 45, 66, 75, 90, 170, 802] | O(nk) | O(nk) | O(nk) | Large datasets with a fixed size of elements (like fixed-length integers). Efficient when the number of digits (k) is less. |
| Bucket Sort    | Distributes the elements into buckets, sorts them, and then merges. | [0.78, 0.17, 0.39, 0.26, 0.72] | [0.17, 0.26, 0.39, 0.72, 0.78] | O(n+k) | O(n+k) | O(n²) | When input is uniformly distributed over a range. Works well for floating point numbers. |
| Shell Sort     | Uses gap sequence to sort the array, reducing the gap over time. | [23, 29, 15, 19, 31, 7, 9] | [7, 9, 15, 19, 23, 29, 31] | O(n log n) | Depends on gap sequence | O(n²) | Medium to large datasets where a more complex algorithm like quick sort or merge sort is not as efficient. |
| Tim Sort       | Hybrid sorting algorithm derived from merge sort and insertion sort. | [5, 21, 7, 23, 19] | [5, 7, 19, 21, 23] | O(n) | O(n log n) | O(n log n) | Datasets that are partially sorted or have a lot of repeated elements. Great default choice for sorting objects. |
| Comb Sort      | Improves on bubble sort by using gap to compare and swap elements. | [8, 4, 10, 9, 6] | [4, 6, 8, 9, 10] | O(n log n) | O(n²/2^p) (p is the number of increments) | O(n²) | Larger datasets where bubble sort is too slow. Good when you want to avoid using extra space and need something simpler than quick sort. |

Remember, the best scenario for each algorithm can vary based on the specific characteristics of the data and the environment in which the algorithm is being used. The table provides a general guide, but the optimal choice can depend on additional factors.
