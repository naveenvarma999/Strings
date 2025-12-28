""" Given a string s, find the length of the longest 
     substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
 Note that "bca" and "cab" are also correct answers.
 
"""
def lengthOfLongestSubstring(s):
    chrSet = set()
    left = 0 
    max_len = 0

    for right in range(len(s)):
        while s[right] in chrSet:
            chrSet.remove(s[left])
            left += 1
        chrSet.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
s = "abcabcbb"
result = lengthOfLongestSubstring(s)
print(result)