class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        DP: Runtime Limit
        O(n) time, O(n) space
        """
#         # dp[i] 表示能否跳到 i 上 0 <= i <= n - 1
#         dp = [False] * len(nums)
        
#         # 初始化
#         dp[0] = True
        
#         for i in range(1, len(nums)):
#             for j in range(0, i):
#                 if not dp[j]:
#                     return False
                
#                 if nums[j] + j >= i:
#                     dp[i] = True
#                     break
#         return dp[-1]
        
        """
        Greedy: O(n) time, O(1) space
        """
        reachable, index = 0, 0
        while index <= reachable and index < len(nums):
            if index + nums[index] > reachable:
                reachable = index + nums[index]
            index += 1
        
        return reachable >= len(nums) - 1 