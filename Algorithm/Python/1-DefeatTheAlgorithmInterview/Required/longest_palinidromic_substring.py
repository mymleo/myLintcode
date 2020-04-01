"""Description
Given a string S, find the longest palindromic substring in S. You may assume 
that the maximum length of S is 1000, and there exists one unique longest 
palindromic substring.
"""

"""Example
Example 1:

    Input:"abcdzdcab"
    Output:"cdzdc"

Example 2:

    Input:"aba"
    Output:"aba"
"""

"""Challenge
O(n^2) time is acceptable. Can you do it in O(n) time.
"""

"""Related Problems
"""

"""
200. Longest Palindromic Substring
Tags: String
Difficulty: Medium
"""
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    ## 基于中心线枚举的方法:O(n^2)
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ""
            
        self.start, self.longest = 0, 0
        for middle in range(len(s)):
            # odd
            self.findLongestPalindromeFrom(s, middle, middle)

            # even
            self.findLongestPalindromeFrom(s, middle, middle + 1)
                
        return s[self.start:self.start + self.longest]
    
    def findLongestPalindromeFrom(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        if self.longest < right - left - 1:
            self.start = left + 1
            self.longest = right - left - 1

    ## other solutions:
    # 基于区间型动态规划的解法
    # 使用 manacher's Algorithm:O(n)
    #参考资料: https://www.felix021.com/blog/read.php?2040

