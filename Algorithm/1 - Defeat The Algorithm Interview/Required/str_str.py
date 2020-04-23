"""Description
For a given source string and a target string, you should output the first index
(from 0) of target string in source string.

If target does not exist in source, just return -1.
"""

"""Clarification
Do I need to implement KMP Algorithm in a real interview?

    Not necessary. When you meet this problem in a real interview, 
the interviewer may just want to test your basic implementation ability. 
But make sure you confirm with the interviewer first.
"""

"""Example
Example 1:

    Input: source = "source" ，target = "target"
    Output: -1	
    Explanation: If the source does not contain the target content, return - 1.

Example 2:

    Input:source = "abcdabcdefg" ，target = "bcd"
    Output: 1	
    Explanation: If the source contains the target content, return the location 
where the target first appeared in the source.
"""

"""Challenge
O(n^2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
"""

"""Related Problems
594. strStr II
"""

"""
13. Implement strStr()
Tags: Basic Implementation & String
Difficulty: Easy
"""
class Solution:
    """
    @param source: {string} source a source string
    @param target: {string} target a target string
    @return : {int} return an integer as the index
    """
    def strStr(self, source, target):
        # Write your code here
        if source is None or target is None:
            return -1
            
        lens = len(source)
        lent = len(target)

        for i in range(lens - lent + 1):
            if source[i:i + lent] == target:
                return i
        return -1