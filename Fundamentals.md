# DATA STRUCTURES AND ALGORITHMS FUNDAMENTALS

## Order of growth
- Also known as asymptotic complexity
- Describes the rate at which the running time / number of operations of an algorithm grows as the input size n increases.
- Focuses on the dominant term and ignores constant factors and lower-order terms, representing the algorithm's long-term scalability.
    - If `T(n) = 5n² + 100n + 1000`, the dominant term is n², so the order of growth is quadratic.

## Time complexity
- Describes how the number of operations performed by an algorithm grows as the size of the input n grows.
- Used to analyse how efficiently an algorithm scales with larger inputs.
- Usually expressed using Big-O notation.
- For example, an algorithm that performs at most n operations has a time complexity of `O(n)`.

## Big O notation
- A mathematical notation used to describe the asymptotic upper bound (worst case) of an algorithm's time or space complexity.
- It describes the order of growth of an algorithm as n becomes very large.
- When analysing Big O, constant factors and lower-order terms are ignored.
    - `O(2n + 5) → O(n)`
    - `O(5n² + 100n + 1000) → O(n²)`

| Big O          | Name                      | Example                            | Explanation                                                                |
| -------------- | ------------------------- | ---------------------------------- | -------------------------------------------------------------------------- |
| **O(1)**       | Constant                  | `array[5]`                         | Takes the same amount of time regardless of input size                     |
| **O(log n)**   | Logarithmic               | Binary search                      | The input is repeatedly divided into smaller parts                         |
| **O(n)**       | Linear                    | Linear search                      | The algorithm may need to examine every element                            |
| **O(n log n)** | Linearithmic / Log-linear | Merge sort                         | The algorithm performs `log n` levels of work, with `n` work at each level |
| **O(n²)**      | Quadratic                 | Bubble sort                        | Typically involves a loop nested inside another loop                       |
| **O(n³)**      | Cubic                     | Some matrix algorithms             | Typically involves three nested loops                                      |
| **O(2ⁿ)**      | Exponential               | Brute-force subset generation      | The number of possibilities doubles as `n` increases                       |
| **O(n!)**      | Factorial                 | Brute-force travelling salesperson | The number of possibilities grows extremely rapidly                        |

## Asymptotic analysis
- Asymptotic analysis evaluates an algorithm’s performance based on input size, ignoring actual running time. 
- It measures the order of growth of time or space
    -  for example, linear search grows linearly `[O(n)]`, while binary search grows logarithmically `[O(logn)]`.
- However it has drawbacks:
    - It ignores constant factors, so two algorithms with the same asymptotic complexity (e.g., `1000n*log ⁡n` vs `2n*log⁡ n`) cannot be directly compared for practical speed.
    - Asymptotic analysis focuses on large input sizes, but in real applications, these inputs may never occur.
    - An algorithm that is asymptotically slower can perform better for specific inputs, so would perform better than a theoretically faster algorithm.

## Space complexity
- Describes how much memory an algorithm requires as the input size grows 
- It includes the memory used by the input and any additional (auxillary) memory the algorithm allocates
    - Auxillary space is the extra memory used by the algorithm, excluding the input itself