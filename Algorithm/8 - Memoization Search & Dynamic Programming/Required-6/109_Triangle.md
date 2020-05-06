[109. Triangle](./109_Triangle.md)
### Description
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
**Note:** Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

<br>

### Example
Example 1:

    Input the following triangle:
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    Output: 11
    Explanation: The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Example 2:

    Input the following triangle:
    [
         [2],
        [3,2],
       [6,5,7],
      [4,4,8,1]
    ]
    Output: 12
    Explanation: The minimum path sum from top to bottom is 12 (i.e., 2 + 2 + 7 + 1 = 12).

<br>

### My Soulution
1. Solution: Divide & Conquer + Memoization
```Python
    def minimumTotal(self, triangle):
        return self.divide_conquer(triangle, 0, 0, {})
        
    def divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0
        
        if (x, y) in memo:
            return memo[(x, y)]
        
        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y + 1, memo)
        
        memo[(x, y)] = triangle[x][y] + min(left, right)
        return memo[(x, y)]     
```

2. Solution: 自顶向下的方式的多重循环动态规划
    使用了滚动数组优化空间<br>
    时间复杂度 O(n^2)
    空间复杂度 O(n) （额外空间）
    
```Python
    def minimumTotal(self, triangle):
        n = len(triangle)
        
        # state: dp[i][j] 代表从 0, 0 走到 i, j 的最短路径值
        dp = [[0] * n, [0] * n]
        
        # initialize: 初始化起点
        dp[0][0] = triangle[0][0]
        
        # function: dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        # i, j 这个位置是从位置 i - 1, j 或者 i - 1, j - 1 走过来的
        for i in range(1, n):
            dp[i % 2][0] = dp[(i - 1) % 2][0] + triangle[i][0]
            dp[i % 2][i] = dp[(i - 1) % 2][i - 1] + triangle[i][i]
            for j in range(1, i):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - 1]) + triangle[i][j]
               
        # answer: 最后一层的任意位置都可以是路径的终点
        return min(dp[(n - 1) % 2])
```

3. Solution: DP bottom-up with no extra space, reusing exsiting list
```Python
     def minimumTotal(self, triangle):
         for i in range(len(triangle) - 2, -1, -1):
             for j in range(i + 1):
                 triangle[i][j] += min(triangle[i + 1][j], 
                 triangle[i + 1][j + 1])
        return triangle[0][0]
```
<br>

### Related Problems
[110. Minimum Path Sum]()