# Best Time to Buy and Sell Stock

Given an array `prices` where `prices[i]` is the price of a stock on day `i`, find the maximum profit you can achieve from a single buy and a single sell.

You must buy before you sell. If no profit can be made, return 0.

## Observations
- `prices`: a list of numbers

## Solutions

**a. Brute Force Solution**
1. Check every possible pair for the price gap.

**b. Two Pointers**
1. Decide where the two pointers start: the first two elements.
2. Decide how the two pointers move: slow and fast pointers.

**c. Iterative Solution**
1. Iterate through the whole list.
2. Keep track of the minimum price.
3. Keep updating the maximum profit.
