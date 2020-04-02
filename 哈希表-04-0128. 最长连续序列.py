class Solution(object):
    """
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence/
    """
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = set(nums)
        rec = {}
        for x in nums:
            rec[x] = rec.get(x - 1, 0) + rec.get(x + 1, 0) + 1
        return max(rec.values())


def main():
    # nums = [100, 4, 200, 1, 3, 2]
    nums = [1, 0, -1]  # 3
    # nums = [1, 2, 0, 1]  # 3
    test = Solution()
    ret = test.longestConsecutive(nums)
    print(ret)


if __name__ == '__main__':
    main()
