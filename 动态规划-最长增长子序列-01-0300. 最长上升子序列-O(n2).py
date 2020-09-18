class Solution(object):
    """
给定一个无序的整数数组，找到其中最长上升子序列的长度。
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
    """
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        opt = [1] * n  # opt[i]表示以当前元素为结尾的最长上升子序列
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    opt[i] = max(opt[i], opt[j] + 1)
        return max(opt)


def main():
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = []
    test = Solution()
    ret = test.lengthOfLIS(nums)
    print(ret)


if __name__ == '__main__':
    main()
