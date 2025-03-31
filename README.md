# Math Utility Functions

This repository contains a collection of Python utility functions for performing common mathematical and string operations. These functions are designed to be simple, efficient, and easy to use.

## Features

- Prime number checking with multiple implementations
- String reversal methods
- Fibonacci sequence calculation with memoization
- Factorial, permutation, and combination calculations
- List operations including removal of duplicates and elements
- Least common multiple (LCM) calculation
- Dictionary key lookup by value
- Element frequency counting in lists

## Functions Overview

### Prime Number Check
- `is_prime0(num)`: Checks if a number is prime using a list comprehension.
- `is_prime1(num)`: Checks if a number is prime using a loop.
- `is_prime2(num)`: Optimized prime check using the square root method.

### String Operations
- `reverse_string0(string)`: Reverses a string using list reversal.
- `reverse_string1(string)`: Reverses a string using slicing.
- `rem_sub_str0(string, sub_string)`: Removes the first occurrence of a substring.
- `rem_sub_str1(string, sub_string)`: Removes a substring using `replace()`.

### List Operations
- `remove_value_from_list(sam_list, *value)`: Removes specified values from a list.
- `rem_dup_list0(sam_list)`: Removes duplicates using iteration.
- `rem_dup_list1(sam_list)`: Removes duplicates using dictionary keys.
- `count_element0(val)`: Counts occurrences of elements in a list.
- `count_element1(val)`: Optimized element count using `Counter`.
- `least_common_mul(num_list)`: Computes the least common multiple (LCM).

### Fibonacci Sequence
- `fib0(num)`: Computes Fibonacci numbers using iteration.
- `fib1(num)`: Optimized Fibonacci calculation using memoization.

### Factorial, Permutation, and Combination
- `p(n, r)`: Computes permutation `P(n, r) = n! / (n-r)!`.
- `c(n, r)`: Computes combination `C(n, r) = n! / (r!(n-r)!)`.

### Dictionary Operations
- `find_key0(dict0, value)`: Finds keys by value using iteration.
- `find_key1(dict0, value)`: Finds keys by value using list comprehension.

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/math-utils.git
   cd math-utils
   ```
2. Import and use functions in your Python scripts:
   ```python
   from math_utils import is_prime2, fib1
   
   print(is_prime2(17))  # True
   print(fib1(10))       # 34
   ```

## License
This project is licensed under the MIT License.

## Author
Yoshmika Sandeepa

## Contributions
Feel free to submit pull requests or report issues if you find any bugs or have suggestions for improvement.

