"""Description:
Given a string which consists of lowercase or uppercase letters, find the length
of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.
"""

"""Example
Example 1:

    Input : s = "abccccdd"
    Output : 7
    Explanation :
    One longest palindrome that can be built is "dccaccd", whose length is `7`.
"""

"""Related Problems:
916. Paliindrome Permutation
891. Valid Palindrome II
745. Palindromic Ranges
678. Shortest Palindrome
415. Valid Palindrome
"""

"""
627. Longest Palindrome
Tags: Hash Table
Difficulty: Easy
"""
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
            
        longest = 0
        odd_num_char = False
        for _, value in char_dict.items():
            if value % 2 == 0:
                longest += value
            else:
                odd_num_char = True
                longest += (value - 1)
        
        if odd_num_char:
            longest += 1
        
        return longest
    
    ## version_2
    # the answer is the count of characters that has even number of appereances.
    # for characters that has odd number of appereances,
    # their appereances minus 1 will make their apperances even.
    # And finally we can put an unused character in the middle of the palindrome
    def longestPalindrome(self, s):
        hash = {}

        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True

        remove = len(hash)
        if remove > 0:
            remove -= 1
    
        return len(s) - remove
