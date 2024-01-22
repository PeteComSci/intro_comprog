Factorial Calculation is a straightforward example of recursion, clearly showing how a problem can be broken down into smaller instances of itself.

### Factorial Calculation
```plaintext
function factorial(n)
    // Base case: if n is 0 or 1
    if n <= 1
        return 1

    // Recursive case: n! = n * (n-1)!
    else
        return n * factorial(n - 1)
```
**Explanation:**
- **Base Case (`if n <= 1`)**: The factorial of 0 or 1 is 1 by definition. This condition provides a stopping point for the recursion.
- **Recursive Case (`else return n * factorial(n - 1)`)**: The function calls itself with `n - 1`. This represents the mathematical definition of factorial, where `n! = n * (n-1)!`. The recursion continues until it reaches the base case.

