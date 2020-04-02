class Solution(object):
    """
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.
链接：https://leetcode-cn.com/problems/longest-harmonious-subsequence/
    """
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rec, count = {}, 0
        for x in nums:
            rec[x] = rec.get(x, 0) + 1
        for x in rec:
            if x + 1 in rec:
                count = max(rec[x] + rec[x + 1], count)
        return count


def main():
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    # nums = []
    # nums = [1, 1, 1, 1]
    # nums = [3, 2, 2, 3, 2, 1, 3, 3, 3, -2, 0, 3, 2, 1, 0, 3, 1, 0, 1, 3, 0, 3, 3]
    # nums = [1,0,2,0,1,2,3,1,1,1,3,3,3,1,0,3,0,3,1,3,-1,2,2,1,1,3,1]
    test = Solution()
    ret = test.findLHS(nums)
    print(ret)


if __name__ == '__main__':
    main()
