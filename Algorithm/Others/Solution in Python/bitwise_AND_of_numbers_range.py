class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 1010 & 1001 = 1000 相当于把二进制最后一个 1 给去掉了
        while m < n:
            n = n & (n-1)
        return n