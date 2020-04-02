class Solution(object):
    """
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
链接：https://leetcode-cn.com/problems/maximum-subarray/
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        opt = [float('-inf')] * (n + 1)
        for i in range(1, n + 1):
            opt[i] = max(nums[i - 1], nums[i - 1] + opt[i - 1])
        return max(opt)


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    test = Solution()
    ret = test.maxSubArray(nums)
    print(ret)


if __name__ == '__main__':
    main()
