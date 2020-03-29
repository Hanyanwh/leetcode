# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。


class Solution:
    def missingNumber(self, nums) -> int:
        """
        异或

        """
        res, n = len(nums), len(nums)
        for i in range(n):
            res ^= nums[i] ^ i
        return res
