[120. Word Ladder](./120_Word_Ladder.md)
### Description
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
Transformation rule such that:

&nbsp;&nbsp;&nbsp;&nbsp;1.Only one letter can be changed at a time
&nbsp;&nbsp;&nbsp;&nbsp;2.Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )

**Note:**
> 
- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.

<br>

### Example
Example 1:

    Input：start = "a"，end = "c"，dict =["a","b","c"]
    Output：2
    Explanation：
    "a"->"c"

Example 2:

    Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
    Output：5
    Explanation：
    "hit"->"hot"->"dot"->"dog"->"cog"

<br>

### My Soulution
[Solution in Python](../Solution%20in%20Python/word_ladder.py)
[Solution in C++]()

<br>

### Related Problems
[121. Word Ladder II](./121_Word_Ladder_II.md)