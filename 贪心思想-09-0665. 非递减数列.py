class Solution(object):
    """
给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。
输入: [4,2,3]
输出: True
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
输入: [4,2,1]
输出: False
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
说明:  n 的范围为 [1, 10,000]。
链接：https://leetcode-cn.com/problems/non-decreasing-array/
    """
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums[0:0] = [float('-inf')]
        count, n = 0, len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if count:
                    return False
                count += 1
                if nums[i] < nums[i - 2]:  # 问题的关键在于修改 i 还是 i - 1
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]  # 原则是在满足要求的情况下把数往小的改
        return True


def main():
    nums = [4, 2, 3]
    # nums = [3, 4, 2, 3]
    # nums = [2, 3, 3, 2, 4]  # true
    test = Solution()
    ret = test.checkPossibility(nums)
    print(ret)


if __name__ == '__main__':
    main()
