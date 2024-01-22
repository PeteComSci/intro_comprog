While the Fibonacci Sequence is a great example to demonstrate recursion, it's worth noting that the direct recursive approach can be highly inefficient for larger values of `n` due to the repeated calculations of the same Fibonacci numbers. Dynamic programming or memoization techniques are often used to optimize it.

### Fibonacci Sequence
```plaintext
function fibonacci(n)
    // Base cases: if n is 0 or 1
    if n == 0
        return 0
    else if n == 1
        return 1

    // Recursive case: Fibonacci number is the sum of the two preceding ones
    else
        return fibonacci(n - 1) + fibonacci(n - 2)
```
**Explanation:**
- **Base Case 1 (`if n == 0`)**: If `n` is 0, the function returns 0, as the 0th number in the Fibonacci sequence is 0.
- **Base Case 2 (`else if n == 1`)**: If `n` is 1, the function returns 1, as the 1st number in the Fibonacci sequence is 1.
- **Recursive Case (`else return fibonacci(n - 1) + fibonacci(n - 2)`)**: The function calls itself twice, once with `n - 1` and once with `n - 2`, then adds the results. This aligns with the definition of the Fibonacci sequence, where each number is the sum of the two preceding ones.
