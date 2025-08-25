# Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or false otherwise.


# Observations
- palindrome examples: 'a', 'aba', 'abba', 'abcba'.
- only alphanumeric characters

# Solutions

**a. Brute Force**
- Filtering not alphanumeric character
- Use head and tail pointers
- Compare each character one by one

**b. Two Pointers**`