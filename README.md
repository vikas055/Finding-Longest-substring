# Finding-Longest-substring

This code solves the "Longest Substring Without Repeating Characters" problem from LeetCode.

Explanation
The task is to find the length of the longest substring without duplicate characters in a given string s.

A sliding window approach is used:
Keep a list (new_list) to store the current substring without duplicates.
If a duplicate character is found, remove characters up to and including the first occurrence of that duplicate.
Always update the max_len with the longest unique substring length seen so far.
