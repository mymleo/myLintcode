"""120. Word Ladder
Tags: Breadth-First Search(BFS)
"""

from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # start 和 end 可能不在 dict 中
        dict = set(dict) # 保证 end in dict 且去重
        dict.add(end)

        queue = deque([start])
        visited = set([start])
        distance = 0

        while queue:
            distance += 1
            for _ in range(len(queue)):
                cur_word = queue.popleft()
                if cur_word == end:
                    return distance
                
                next_words = self.findNextWordsFrom(cur_word)
                for next_word in next_words:
                    if next_word not in dict or next_word in visited:
                        continue
                    #########################
                    queue.append(next_word)
                    visited.add(next_word)
                    #########################
        return 0

    def findNextWordsFrom(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words

# test
# print(Solution().ladderLength('a', 'c', ['a', 'b', 'c'])) # 2
print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])) # 5

