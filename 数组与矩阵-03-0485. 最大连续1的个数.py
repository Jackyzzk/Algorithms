class Solution(object):
    """
给定一个二进制数组， 计算其中最大连续1的个数。
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。
链接：https://leetcode-cn.com/problems/max-consecutive-ones
    """
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = ret = 0
        for x in nums:
            if x:
                count += 1
            else:
                ret = max(ret, count)
                count = 0
        ret = max(ret, count)
        return ret


def main():
    nums = [1, 1, 0, 1, 1, 1]
    test = Solution()
    ret = test.findMaxConsecutiveOnes(nums)
    print(ret)


if __name__ == '__main__':
    main()
