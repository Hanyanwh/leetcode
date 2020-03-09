# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5

"""

        这个题是看过题解做的！！！！！

"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """

                leetcode理解版本

        """
        length_nums1 = len(nums1)
        length_nums2 = len(nums2)

        if length_nums1 >= length_nums2:
            long_list_size = length_nums1
            long_list = nums1
            short_list_size = length_nums2
            short_list = nums2
        else:
            short_list_size = length_nums1
            short_list = nums1
            long_list_size = length_nums2
            long_list = nums2

        if long_list_size == 0:
            raise ValueError

        start = 0
        end = short_list_size
        while start <= end:
            i_short_list = int((start + end) / 2)
            j_long_list = int((long_list_size + short_list_size + 1) / 2 - i_short_list)
            if i_short_list < short_list_size and short_list[i_short_list] < long_list[j_long_list - 1]:
                start = i_short_list + 1
            elif i_short_list >0 and short_list[i_short_list - 1] > long_list[j_long_list]:
                end = i_short_list - 1
            else:
                if i_short_list == 0:
                    max_of_left = long_list[j_long_list - 1]
                elif j_long_list == 0:
                    max_of_left = short_list[i_short_list - 1]
                else:
                    max_of_left = max(short_list[i_short_list - 1], long_list[j_long_list - 1])

                if (long_list_size + short_list_size) % 2 == 1:
                    return max_of_left

                if i_short_list == short_list_size:
                    min_of_right = long_list[j_long_list]
                elif j_long_list == long_list_size:
                    min_of_right = short_list[i_short_list]
                else:
                    min_of_right = min(short_list[i_short_list], long_list[j_long_list])

                return (max_of_left + min_of_right) / 2.0

    def findMedianSortedArrays_easy(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            m, n, A, B = n, m, B, A

        i_start = 0
        i_end = m

        mind_num = int((m+n+1)/2)
        while i_start <= i_end:
            i = int((i_start+i_end)/2)
            j = mind_num - i
            if i > 0 and A[i-1] > B[j]:
                i_end = i-1
            elif i < m and B[j-1] > A[i]:
                i_start = i + 1
            else:

                if i == 0:
                    left_max = B[j - 1]
                elif j == 0:
                    left_max = A[i - 1]
                else:
                    left_max = max(A[i-1], B[j-1])

                if (m + n) % 2:
                    return left_max

                if i == m:
                    right_min = B[j]
                elif j == n:
                    right_min = A[i]
                else:
                    right_min = min(A[i], B[j])

                return (left_max + right_min)/2.0

put = Solution()
print(put.findMedianSortedArrays([1, 2], [3, 6]))