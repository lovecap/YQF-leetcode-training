"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
    """
    class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lenS = len(s)
        if lenS <= 1: return s
        minStart, maxLen, i = 0, 1, 0
        while i < lenS:
            if lenS - i <= maxLen / 2: break
            j, k = i, i
            while k < lenS - 1 and s[k] == s[k + 1]: k += 1
            i = k + 1
            while k < lenS - 1 and j and s[k + 1] == s[j - 1]:  k, j = k + 1, j - 1
            if k - j + 1 > maxLen: minStart, maxLen = j, k - j + 1
        return s[minStart: minStart + maxLen]
    