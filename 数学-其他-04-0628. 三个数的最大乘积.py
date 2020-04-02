class Solution(object):
    """
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
输入: [1,2,3]       输出: 6
输入: [1,2,3,4]     输出: 24
注意:
给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers/
    """
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        t1 = nums[0] * nums[1] * nums[n - 1]
        t2 = nums[n - 3] * nums[n - 2] * nums[n - 1]
        return max(t1, t2)



def main():
    nums = [1, 2, 3, 4]
    # nums = [-4, -3, -2, -1, 60]
    test = Solution()
    ret = test.maximumProduct(nums)
    print(ret)


if __name__ == '__main__':
    main()
