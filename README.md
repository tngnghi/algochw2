# Algorithm Implementations — CS 460

Python implementations of fundamental algorithms, written and analyzed for CS 460: Algorithms at SDSU.

## What's Implemented

### Sorting
- **Quick Sort** — classic last-element pivot with partition
- **Modified Quick Sort** — median-of-three pivot for better performance on sorted/reverse-sorted input
- Empirical runtime comparison across random, ascending, and descending inputs

### Dynamic Programming
| Problem | Approach |
|---|---|
| Subset Sum | Recursive with early termination |
| Minimum Cost Path | Naïve recursive · Top-down memoization · Bottom-up DP · Path reconstruction |
| Matrix Chain Multiplication | Top-down memoized · Bottom-up with split-index table · Full parenthesization output |
| Rod Cutting | Top-down memoized · Bottom-up with cut reconstruction |

### Other
- **Stable Priority Sort** — bucket sort preserving relative order within each priority group
- **Slice, Sort, K-th Element** — process range queries on arrays
- **Data Filtering & Sorting** — filter by field threshold, sort by another field

## Notes

All implementations include inline comments explaining the logic. No AI tools were used — verified against provided test cases and autograder.
