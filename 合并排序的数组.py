# 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
#
# 初始化 A 和 B 的元素数量分别为 m 和 n。
#
# 示例:
#
# 输入:
# A = [1,2,3,0,0,0], m = 3
# B = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]


class Solution:
    def merge(self, A, m, B, n):
        """
        额外数组归并
        """
        for i in range(n):
            A[m+i] = B[i]

        A_ = 0
        B_ = m
        temp = []
        flag = 0

        while A_ < m and B_ < m + n:
            if A[A_] < A[B_]:
                temp.append(A[A_])
                A_ = A_ + 1
            else:
                temp.append(A[B_])
                B_ = B_ + 1
            flag = flag + 1

        while A_ < m:
            temp.append(A[A_])
            A_ = A_ + 1

        while B_ < n + m:
            temp.append(A[B_])
            B_ = B_ + 1

        temp

        return temp

    def merge_2(self, A, m, B, n):
        """
        数组自身逆序归并
        A 的后半部分是空的，可以直接覆盖而不会影响结果


        """
        i = m - 1
        j = n - 1
        flag = n + m - 1
        while j >= 0 and i >= 0:
            if A[i] > B[j]:
                A[flag] = A[i]
                i = i - 1
            else:
                A[flag] = B[j]
                j = j - 1
            flag = flag - 1
        while j >= 0:
            A[flag] = B[j]
            j = j - 1
            flag = flag - 1

        return A


# 输出
put = Solution()
print(put.merge_2([2, 0], 1, [1], 1))
