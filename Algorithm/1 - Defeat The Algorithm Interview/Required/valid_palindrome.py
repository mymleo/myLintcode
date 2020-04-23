"""Description:
Given a string, determine if it is a palindrome, considering only alphanumeric 
characters and ignoring cases.

Note:
    Have you consider that the string might be empty? This is a good question to
    ask during an interview.

    For the purpose of this problem, we define empty string as valid palindrome.
"""

"""Example
Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama"

Example 2:

    Input: "race a car"
    Output: false
    Explanation: "raceacar"
"""

"""Challenge
O(n) time without extra memory.
"""

"""Related Problems
893. 
891.
745.
744.
491.
627.
223.
200.
"""

"""
415. Valid Palindrome
Tags: Two pointers & String
Difficulty: Medium
"""
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
                    
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
