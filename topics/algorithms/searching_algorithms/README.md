# Searching Algorithms

Searching algorithms are crucial in computing for finding elements within collections. This module will explore a variety of searching techniques, each suited to different situations and data structures. From the simple linear search to more advanced methods, understanding these algorithms will empower you to solve search-related problems more efficiently.

---

### Topics Covered:

1. **[Linear Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/linear_search)**
   - A straightforward approach where each element of a list is checked sequentially until the target is found or the list ends.
   - **Example:** Finding a specific book by checking each book on a shelf one by one.

2. **[Binary Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/binary_search)**
   - An efficient method for sorted arrays, repeatedly dividing the search interval in half.
   - **Example:** Looking for a word in a dictionary by continuously splitting the word range.

3. **[Jump Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/jump_search)**
   - Balances linear and binary search by jumping ahead in fixed intervals, then performing linear search within the interval.
   - **Example:** Searching for a song in an alphabetically organized playlist by skipping a set number of songs at a time.

4. **[Exponential Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/exponential_search)**
   - Combines the principles of binary search and jump search. It first finds a range where the target could be and then performs a binary search within that range.
   - **Example:** Finding a specific contact in a digital phonebook where contacts are exponentially more frequent toward the end of the list.

5. **[Interpolation Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/interpolation_search)**
   - A variant of binary search for uniformly distributed data. It estimates the position of the target based on its value and the distribution of values in the array.
   - **Example:** Searching for a specific page number in a textbook, predicting its position based on the total number of pages.

6. **[Ternary Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/ternary_search)**
   - Similar to binary search but divides the array into three parts instead of two, reducing the possible search area more rapidly.
   - **Example:** Finding the highest point on a relatively smooth landscape, where you eliminate one-third of the area in each step.

7. **[Fibonacci Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/fibonacci_search)**
   - A search technique using Fibonacci numbers to divide the array. It’s a compromise between binary and interpolation search.
   - **Example:** Searching a high score list where ranks are determined by Fibonacci sequence levels.

---

By exploring these diverse searching algorithms, you will gain a comprehensive understanding of how different methods can be applied to various data structures and scenarios. Each algorithm offers a unique approach to problem-solving, reinforcing the importance of choosing the right tool for the task at hand.

---

Here's a comparison table detailing the different searching algorithms along with their explanations, examples, complexities, and best usage scenarios:

| Algorithm          | Explanation                                                                                          | Example Before                               | Example After                            | Best Case      | Average Case     | Worst Case     | Best Usage Scenario                                                                                     |
|--------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------|------------------------------------------|----------------|------------------|----------------|--------------------------------------------------------------------------------------------------------|
| **[Linear Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/linear_search)**  | Checks each element sequentially until the target is found or the list ends.                          | List of books on a shelf, looking for "1984". | Found "1984" at position 3.              | O(1)           | O(n)             | O(n)           | Small datasets or when the list is unsorted.                                                           |
| **[Binary Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/binary_search)**  | Divides the search interval in half repeatedly, used for sorted arrays.                               | Sorted array of numbers, looking for 7.       | Found 7 at position 4.                   | O(1)           | O(log n)         | O(log n)       | Large, sorted datasets where fast search is needed.                                                    |
| **[Jump Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/jump_search)**    | Jumps ahead in fixed intervals, then performs linear search within the interval.                      | Sorted list of songs, looking for "Come As You Are". | Found the song at position 6.   | O(√n)          | O(√n)            | O(√n)          | Sorted arrays where binary search's strict divide may not be as efficient.                             |
| **[Exponential Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/exponential_search)** | Combines principles of binary and jump search by finding a range exponentially, then binary search. | Digital phonebook, looking for "Isaac".        | Found "Isaac" at position 8.            | O(log i)       | O(log i)         | O(log n)       | Unbounded or infinite lists, or when the size of the list is unknown.                                  |
| **[Interpolation Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/interpolation_search)** | Variant of binary search for uniformly distributed data, estimates position.                          | Sorted pages of a textbook, looking for page 600. | Found page 600.                     | O(1)           | O(log log n)     | O(n)           | Searching through uniformly distributed datasets for quicker results than binary search.               |
| **[Ternary Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/ternary_search)** | Similar to binary search but divides the array into three parts instead of two.                        | Finding the highest point on a smooth landscape.  | Found the highest point at position 7. | O(1)           | O(log₃ n)        | O(log₃ n)     | Finding maximum or minimum in unimodal functions or arrays with a strict increase then decrease (or vice versa). |
| **[Fibonacci Search](https://github.com/PeteComSci/intro_comprog/tree/3ba46e263efed87003b8ef9af12c4ec697bdcede/topics/algorithms/searching_algorithms/topics/fibonacci_search)** | Uses Fibonacci numbers to divide the array, a compromise between binary and interpolation search.  | High score list ranked by Fibonacci levels, looking for a specific score. | Found the score at position 5.    | O(log i)       | O(log i)         | O(log n)       | Large datasets where the size is unknown or when memory usage needs to be minimized.                    |

In this table:
- **n** represents the number of elements in the array or list.
- **i** refers to the position of the target element in the array or list.
- **Best Case** scenario generally assumes the target is located early in the search process or has some optimal condition.
- **Average Case** and **Worst Case** provide a general estimate of the algorithm's performance based on typical and extreme conditions, respectively.
- **Best Usage Scenario** gives insight into the most suitable applications for each algorithm, considering their strengths and characteristics.

---

This comparison aims to provide a clear understanding of each searching algorithm, making it easier to choose the most suitable one based on the specific needs and characteristics of the dataset or problem at hand.
