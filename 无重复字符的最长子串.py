# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        时间复杂度极高的算法 o(n^3)
        """
        max_str = 0
        for i in range(len(s)):
            sub_max_str = 1
            for n in range(i+1, len(s)):
                flag = 0
                for m in range(i, n):
                    if s[m] == s[n]:
                        flag = 1
                        break
                if flag == 1:
                    break
                else:
                    sub_max_str = sub_max_str + 1
            if sub_max_str > max_str:
                max_str = sub_max_str
            if len(s) - i <= max_str:
                break
        return max_str

    def lengthOfLongestSubstring_end(self, s):
        """
        优化滑动窗口算法 o(n^2)
        """

        max_len = 0
        str_windows = {}
        temp = []
        i = 0
        while i < len(s):
            if str_windows.get(s[i], False):
                value = str_windows[s[i]]

                for key in str_windows:
                    if str_windows[key] <= value:
                        temp.append(key)
                for n in temp:
                    str_windows.pop(n)
                temp.clear()
                str_windows[s[i]] = i

            else:
                str_windows[s[i]] = i
            i = i + 1
            if len(str_windows) > max_len:
                max_len = len(str_windows)

        return max_len

    def lengthOfLongestSubstring_end_end(self, s):
        """
        优化滑动窗口算法 o(n) 不需要删除以前的值hashmap会去重
        """

        max_len = 0
        str_windows = {}
        j = 0
        for i in range(len(s)):
            if str_windows.get(s[i], False):
                j = max(str_windows[s[i]], j)
            str_windows[s[i]] = i+1
            max_len = max(max_len, i - j + 1)

        return max_len


put = Solution()
print(put.lengthOfLongestSubstring_end_end(s="abc"))
