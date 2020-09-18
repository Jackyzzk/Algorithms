class Solution(object):
    """
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
left[i] = nums[i - 1] * left[i - 1]
right[i] = nums[i + 1] * right[i + 1]
链接：https://leetcode-cn.com/problems/product-of-array-except-self/
    """
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1]
        right = [1]
        for i in range(1, n):
            left[n:n] = [nums[i - 1] * left[i - 1]]
        for i in range(n - 2, -1, -1):
            right[0:0] = [nums[i + 1] * right[0]]
        ret = []
        for i in range(n):
            ret[n:n] = [left[i] * right[i]]
        return ret


def main():
    nums = [1, 2, 3, 4]
    test = Solution()
    ret = test.productExceptSelf(nums)
    print(ret)


if __name__ == '__main__':
    main()
