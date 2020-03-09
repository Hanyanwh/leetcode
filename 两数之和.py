# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


class Solution:
    def twoSum(self, nums, target):
        """
        无负数的情况
        """
        index = [-1 for x in range(target+1)]
        num_list = [0 for x in range(target+1)]
        for i in range(len(nums)):
            if nums[i] <= target:
                num_list[nums[i]] = 1
                index[nums[i]] = i
        for i in range(len(nums)):
            if nums[i] <= target:
                if num_list[target - nums[i]] and i != index[target - nums[i]]:
                    return [i, index[target - nums[i]]]

        return []

    def twoSum_nature(self, nums, target):
        """
        存在负数
        内存占用过多
        """

        # 找到数列的最大和最小值
        nums_max = 0
        nums_min = 0
        for i in range(len(nums)):
            if nums[i] < nums_min:
                nums_min = nums[i]
            elif nums[i] > nums_max:
                nums_max = nums[i]

        positive_index = [-1 for x in range(nums_max+1)]
        positive_num_list = [0 for x in range(nums_max+1)]

        negative_index = [-1 for x in range(-nums_min + 1)]
        negative_num_list = [0 for x in range(-nums_min + 1)]

        # 组装辅助数组
        for i in range(len(nums)):
            if nums[i] < 0:
                negative_num_list[-nums[i]] = 1
                negative_index[-nums[i]] = i
            else:
                positive_num_list[nums[i]] = 1
                positive_index[nums[i]] = i

        for i in range(len(nums)):
            if target - nums[i] < 0 and (target - nums[i] >= nums_min):
                if negative_num_list[nums[i] - target] and i != negative_index[nums[i] - target]:
                    return [i, negative_index[nums[i] - target]]
            elif target - nums[i] >= 0 and (target - nums[i] <= nums_max):
                if positive_num_list[target - nums[i]] and i != positive_index[target - nums[i]]:
                    return [i, positive_index[target - nums[i]]]

        return []

    def twoSum_nature_end(self, nums, target):
        """
        存在负数
        时间复杂度太大
        """
        for n in range(len(nums)):
            for m in range(n, len(nums)):
                if nums[n] + nums[m] == target and (m != n):
                    return [n, m]

        return []

    def twoSum_nature_end_end(self, nums, target):
        """
        存在负数
        """
        # 找到数列的最大和最小值
        nums_max = 0
        nums_min = 0
        for i in range(len(nums)):
            if nums[i] < nums_min:
                nums_min = nums[i]
            elif nums[i] > nums_max:
                nums_max = nums[i]
        if target > 0:
            if nums_max > target-nums_min:
                flag = target-nums_min
            else:
                flag = nums_max
            positive_index = [-1 for x in range(flag + 1)]
            positive_num_list = [0 for x in range(flag + 1)]

            negative_index = [-1 for x in range(-nums_min + 1)]
            negative_num_list = [0 for x in range(-nums_min + 1)]
        else:
            if nums_min < target-nums_max:
                flag = target-nums_max
            else:
                flag = nums_min

            positive_index = [-1 for x in range(nums_max + 1)]
            positive_num_list = [0 for x in range(nums_max + 1)]

            negative_index = [-1 for x in range(-flag + 1)]
            negative_num_list = [0 for x in range(-flag + 1)]

        # 组装辅助数组
        for i in range(len(nums)):
            if nums[i] < 0 and (-nums[i] < len(negative_num_list)):
                negative_num_list[-nums[i]] = 1
                negative_index[-nums[i]] = i
            elif nums[i] >= 0 and (nums[i] < len(positive_num_list)):
                positive_num_list[nums[i]] = 1
                positive_index[nums[i]] = i

        for i in range(len(nums)):
            if target - nums[i] < 0 and (target - nums[i] >= nums_min):
                if negative_num_list[nums[i] - target] and i != negative_index[nums[i] - target]:
                    return [i, negative_index[nums[i] - target]]
            elif target - nums[i] >= 0 and (target - nums[i] <= nums_max):
                if positive_num_list[target - nums[i]] and i != positive_index[target - nums[i]]:
                    return [i, positive_index[target - nums[i]]]

        return []

    def twoSum_nature_end_end(self, nums, target):
        """
        存在负数
        """



# 试运行
put = Solution()
