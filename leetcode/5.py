"""
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

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