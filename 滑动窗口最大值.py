# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#  
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
#
# 提示：
#
# 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
#
#  
#
# 进阶：
#
# 你能在线性时间复杂度内解决此题吗？
#


class Solution:
    def maxSlidingWindow(self, nums, k):
        """

        不是线性时间复杂度
        递减数列时间复杂度为O(k*(n-k))，但是平均时间复杂度应该是趋近于O(n)的，k越大时间复杂度越低
        执行时间88.59%， 内存100%。
        """
        max_num, max_index, i, result = 0, 0, 0, []
        k_windows = [0, k - 1]

        while i < len(nums):
            if max_index < k_windows[0]:
                i = k_windows[0]
                max_num = nums[i]
                max_index = i
                continue

            elif max_index >= k_windows[0] and max_num < nums[i]:
                max_num = nums[i]
                max_index = i

            if i == k_windows[1]:
                k_windows[0] += 1
                k_windows[1] += 1
                result.append(max_num)

            i += 1

        return result
#:wq
