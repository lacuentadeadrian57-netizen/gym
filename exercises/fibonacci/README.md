# Exercise: Fibonacci Numbers

The Fibonacci sequence is one of the most famous sequences in mathematics. It appears in nature, art, and architecture, and is a fundamental example of recursion and iterative growth in computer science.

## The Sequence

The sequence starts with $0$ and $1$, and each subsequent number is the sum of the two preceding ones:

- $F(0) = 0$
- $F(1) = 1$
- $F(n) = F(n-1) + F(n-2)$ for $n \ge 2$

The beginning of the sequence is: $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...$

## The Task

Implement a function `fibonacci(n: int) -> int` that calculates the $n$-th Fibonacci number.

### Specifications

- **Function Name**: `fibonacci`
- **Arguments**: `n` (an integer, where $0 \le n \le 30$)
- **Return Type**: `int`

### Constraints

Your implementation should be efficient enough to handle $n$ up to $30$ within the time limit.

### Example

```python
>>> fibonacci(5)
5
>>> fibonacci(10)
55
```

## Instructions

1. Open `exercises/fibonacci/solution.py`.
2. Implement the `fibonacci` function.
3. Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4. Run `make test` locally to verify your solution.
