# Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Return the answer in any



## Observations
- `nums`: list of numbers
- `target`: target number

## Solutions

**a. Brute Force Solution:**  
1. Check every possible pair in the list.

**b. Search for Complement:**  
1. For every number, scan the list for its complement.  
2. Use binary search (if the list is sorted).

**c. Hash Map Approach $:**  
1. Insert each number into a hash map.  
2. Iterate through the list and check if the complement of the current number exists in the hash map.

**d. Sorting with Two Pointers**
1. Sort the array while keeping track of the original indices
2. Use two pointers (start and end) to find the pair thats sums to the target
3. Note: This approach works if you can sort and need indices *less efficient than the hash map approach
