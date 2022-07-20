# Topics

In order to facilitate the study of topics on a need-to-know basis, the coding exercises related to each topic are listed below. Some exercises cover more than one topic and thus may appear in more than one list. Each problem has its difficulty specified as shown on Leetcode. 

## Arrays
Arrays are a data structure consisting of a list of ordered elements. Each element may be identified by an array index, which denotes its position inside the array. Array indexes normally start at `0` and end at `n-1` (`n` being the array length). [Arrays on Wikipedia](https://en.wikipedia.org/wiki/Array_data_structure).

Coding exercises involving arrays:
- [724](../leetcode/724-find-pivot-index/): Find pivot index (`easy`)
- [1480](../leetcode/1480-running-sum-of-1d-array/): Running sum of 1D array (`easy`)

## Dynamic Programming
It is a faster alternative to recursion problems which have repeatable operations, relying on saving the results of previous calculations. The Fibonacci sequence is a classic example, where `F(i) = F(i-1) + F(i-2)`, but `F(i-1) = F(i-2) + F(i-3`, therefore we have to calculate `F(i-2)` multiple times. DP usually finds application in problems which can be broken into sub-problems/sub-domains. Since it relies on saving operations, it is a technique heavy on memory (usually involving the creation of arrays and matrices). [Dynamic programming on Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming).

Coding exercises involving dynamic programming:
- [392](../leetcode/392-is-subsequence/): Is subsequence (`easy`)

## Hash Maps
The hash map, also known as dictionary, is a data structure that maps keys to values, with roughly O(1) access to the value if one has the corresponding key. A hash map uses a hash function to determine where the value is going to be stored. On lookup, the key is hashed to find the corresponding value. This data structure offers fast lookup at a high memory expense. [Hash maps on Wikipedia](https://en.wikipedia.org/wiki/Hash_table). 

Coding exercises involving hash maps:
- [205](../leetcode/205-isomorphic-strings/): Isomorphic strings (`easy`)

## Prefix Sum
The prefix sum, also known as the cumulative sum, is a sequence of numbers `y` as such that each element of the sequence is the running total of the elements from another sequence `x`. That is, `y0 = x0` ; `y1 = x0 + x1` ; `y2 = x0 + x1 + x2`. [Prefix Sum on Wikipedia](https://en.wikipedia.org/wiki/Prefix_sum).

Coding exercises involving prefix sum:
- [724](../leetcode/724-find-pivot-index/): Find pivot index (`easy`)
- [1480](../leetcode/1480-running-sum-of-1d-array/): Running sum of 1D array (`easy`)

## Recursion
It is the definition of a thing based on itself. In the case of programming functions, it is when a function is called inside itself. We always need a stop condition when using recursion, or we may incur in an infinite recursion and stack overflow. [Recursion on Wikipedia](https://en.wikipedia.org/wiki/Recursion).

Coding exercises involving recursion:
- [21](../leetcode/21-merge-two-sorted-lists/): Merge two sorted lists (`easy`)

## Strings
Strings are sequence of characters, so they are any kind of text found in code. [Strings in Wikipedia](https://en.wikipedia.org/wiki/String_(computer_science)).

Coding exercises involving strings:
- [205](../leetcode/205-isomorphic-strings/): Isomorphic strings (`easy`)
- [392](../leetcode/392-is-subsequence/): Is subsequence (`easy`)