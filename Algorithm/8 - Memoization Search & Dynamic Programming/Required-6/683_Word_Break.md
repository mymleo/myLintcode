[683. Word Break III](./683_Word_Break.md)
### Description
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

**Note:** Ignore case

<br>

### Example
Example 1:

    Input:
    "CatMat"
    ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
    Output: 3
    Explanation:
    we can form 3 sentences, as follows:
    "CatMat" = "Cat" + "Mat"
    "CatMat" = "Ca" + "tM" + "at"
    "CatMat" = "C" + "at" + "Mat"

Example 2:

    Input:
    "a"
    []
    Output: 0

<br>

### My Soulution
Solution：recursion + memoization
```Python
class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        # 获取最长单词的长度、小写化的字典
        max_length, lower_dict = self.get_lower_dict(dict)
        memo = {}
        if self.is_possible(s.lower(), max_length, lower_dict, memo):
            return memo[s.lower()]
        return 0
    
    # memo 记录 s 能有多少种分法
    def is_possible(self, s, max_length, dict, memo):
        if len(s) == 0:
            return False
        
        if s in memo:
            return True
        
        memo[s] = 0
        for i in range(len(s)):
            prefix = s[:i+1]
            if i + 1 > max_length:
                break
            
            if prefix not in dict:
                continue
            
            if self.is_possible(s[i+1:], max_length, dict, memo):
                memo[s] += memo[s[i+1:]]
        
        # 整个s是否在字典中
        if s in dict:
            memo[s] += 1
        
        return memo[s] != 0
    
    def get_lower_dict(self, dict):
        max_length = 0
        lower_dict = set()
        for word in dict:
            max_length = max(max_length, len(word))
            lower_dict.add(word.lower())
        return max_length, lower_dict
```