# Topics

In order to facilitate the study of topics on a need-to-know basis, the coding exercises related to each topic are listed below. Some exercises cover more than one topic and thus may appear in more than one list. Each problem has its difficulty specified as shown on Leetcode or Beecrowd. 

## Arithmetic Progression
Arithmetic progression (AP) is a sequence of numbers where the difference between each preceding and succeeding term is constant. There are known formulas to calculate the Nth term of an AP and its sum to the Nth member (called an arithmetic series). For example, the sequence 1, 3, 5, 7, ... is an AP with a difference constant of 2. [Arithmetic Progression on Wikipedia](https://en.wikipedia.org/wiki/Arithmetic_progression).

Coding exercises involving arithmetic progressions:
- [BC #2218](../beecrowd/2218-the-terrible-evilson/): The terrible Evil-Son (`level 1`)

## Arrays
Arrays are a data structure consisting of a list of ordered elements. Each element may be identified by an array index, which denotes its position inside the array. Array indexes normally start at `0` and end at `n-1` (`n` being the array length). [Arrays on Wikipedia](https://en.wikipedia.org/wiki/Array_data_structure).

Coding exercises involving arrays:
- [LC #724](../leetcode/724-find-pivot-index/): Find pivot index (`easy`)
- [LC #1480](../leetcode/1480-running-sum-of-1d-array/): Running sum of 1D array (`easy`)
- [LC #2073](../leetcode/2073-time-needed-to-buy-tickets/): Time need to buy tickets (`easy`)

## Dynamic Programming
It is a faster alternative to recursion problems which have repeatable operations, relying on saving the results of previous calculations. The Fibonacci sequence is a classic example, where `F(i) = F(i-1) + F(i-2)`, but `F(i-1) = F(i-2) + F(i-3`, therefore we have to calculate `F(i-2)` multiple times. DP usually finds application in problems which can be broken into sub-problems/sub-domains. Since it relies on saving operations, it is a technique heavy on memory (usually involving the creation of arrays and matrices). [Dynamic programming on Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming).

Coding exercises involving dynamic programming:
- [LC #392](../leetcode/392-is-subsequence/): Is subsequence (`easy`)
- [BC #2986](../beecrowd/2986-not-all-strikes/): Nem Tudo é Greve Versão Hard (`level 1`)

## Greatest Common Divisor
The Greatest Common Divisor (GCD) of two or more integers is the largest positive integer that divides each of them. One can calculate the GCD by the recursive Euclidean Algorithm: `gcd(x,y) => gcd(y, x % y) ...` until `gcd(d, 0)` where `d` is the GCD. [GCD on Wikipedia](https://en.wikipedia.org/wiki/Greatest_common_divisor).

Coding exercises involving greatest common divisors:
- [BC #1630](../beecrowd/1630-stakes/): Stakes (`level 1`)

## Hash Maps
The hash map, also known as dictionary, is a data structure that maps keys to values, with roughly O(1) access to the value if one has the corresponding key. A hash map uses a hash function to determine where the value is going to be stored. On lookup, the key is hashed to find the corresponding value. This data structure offers fast lookup at a high memory expense. [Hash maps on Wikipedia](https://en.wikipedia.org/wiki/Hash_table). 

Coding exercises involving hash maps:
- [LC #205](../leetcode/205-isomorphic-strings/): Isomorphic strings (`easy`)
- [LC #1](../leetcode/1-two-sum/): Two Sum (`easy`)

## Linked Lists
Linkeds lists are an ordered, linear data structure in which nodes containing values point to other nodes in a sequence. This differs from arrays in that the nodes are not necessarily beside one another in memory, thus we cannot access the linked list elements through indexes. The traversal up to a node `n` in a linked list has a cost of `O(n)`. [Linked lists on Wikipedia](https://en.wikipedia.org/wiki/Linked_list).

Coding exercises involving linked lists:
- [LC #21](../leetcode/21-merge-two-sorted-lists/): Merge two sorted lists (`easy`)
- [LC #206](../leetcode/206-reverse-linked-list/): Reverse linked list (`easy`)
- [LC #876](../leetcode/876-middle-of-linked-list/): Find middle of linked list (`easy`)
- [LC #142](../leetcode/142-linked-list-cycle/): Find cycle in linked list (`medium`)
- [LC #2](../leetcode/2-add-two-numbers/): Add two numbers (`medium`)

## Prefix Sum
The prefix sum, also known as the cumulative sum, is a sequence of numbers `y` as such that each element of the sequence is the running total of the elements from another sequence `x`. That is, `y0 = x0` ; `y1 = x0 + x1` ; `y2 = x0 + x1 + x2`. [Prefix Sum on Wikipedia](https://en.wikipedia.org/wiki/Prefix_sum).

Coding exercises involving prefix sum:
- [LC #724](../leetcode/724-find-pivot-index/): Find pivot index (`easy`)
- [LC #1480](../leetcode/1480-running-sum-of-1d-array/): Running sum of 1D array (`easy`)

## Recursion
It is the definition of a thing based on itself. In the case of programming functions, it is when a function is called inside itself. We always need a stop condition when using recursion, or we may incur in an infinite recursion and stack overflow. [Recursion on Wikipedia](https://en.wikipedia.org/wiki/Recursion).

Coding exercises involving recursion:
- [LC #21](../leetcode/21-merge-two-sorted-lists/): Merge two sorted lists (`easy`)
- [LC #206](../leetcode/206-reverse-linked-list/): Reverse linked list (`easy`)
- [LC #2](../leetcode/2-add-two-numbers/): Add two numbers (`medium`)

## Stack
A stack is a data structure with serves as a collection of elements, with two operations: push and pop. It's a LIFO (last in, first out) list, meaning you can only add to the top of the stack and remove from the top of the stack. [Stacks on Wikipedia](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)).

Coding exercises involving stacks:
- [LC #1614](../leetcode/1614-maximum-nesting-depth/): Maximum nesting depth of the parentheses (`easy`)
- [LC #1544](../leetcode/1544-make-the-string-great/): Make the string great (`easy`)


## Strings
Strings are sequence of characters, so they are any kind of text found in code. [Strings in Wikipedia](https://en.wikipedia.org/wiki/String_(computer_science)).

Coding exercises involving strings:
- [LC #205](../leetcode/205-isomorphic-strings/): Isomorphic strings (`easy`)
- [LC #392](../leetcode/392-is-subsequence/): Is subsequence (`easy`)
- [LC #1614](../leetcode/1614-maximum-nesting-depth/): Maximum nesting depth of the parentheses (`easy`)
- [LC #1544](../leetcode/1544-make-the-string-great/): Make the string great (`easy`)