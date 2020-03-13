# 给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
#
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。
#
# 示例 1:
#
# 输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出: [-1,3,-1]
# 解释:
#     对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
#     对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
#     对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
# 示例 2:
#
# 输入: nums1 = [2,4], nums2 = [1,2,3,4].
# 输出: [3,-1]
# 解释:
#     对于num1中的数字2，第二个数组中的下一个较大数字是3。
#     对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
# 注意:
#
# nums1和nums2中所有元素是唯一的。
# nums1和nums2 的数组大小都不超过1000。


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """

            利用栈记录nums2中与nums1相等的元素
            在遍历nums2时不断让每个元素与栈顶元素比较，直到遍历结束

        """
        stack = []
        result = [-1 for i in range(len(nums1))]
        for i in nums2:
            while stack and i > stack[-1]:
                result[nums1.index(stack.pop())] = i
            if i in nums1:
                stack.append(i)
        return result


class Solution_end:
    def nextGreaterElement(self, nums1, nums2):
        """

                运用栈和hashmap
             （优化）   在hashmap中查找

        """
        stack, hashmap = [], {}
        result = [-1 for i in range(len(nums1))]
        for i in range(len(nums1)):
            hashmap[nums1[i]] = i
        for i in nums2:
            while stack and i > stack[-1]:
                result[hashmap[stack.pop()]] = i
            if i in hashmap:
                stack.append(i)
        return result

