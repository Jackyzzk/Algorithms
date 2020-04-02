class Solution(object):
    """
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出
和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
链接：https://leetcode-cn.com/problems/two-sum/
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        rec = {}
        for i in range(n):
            if nums[i] in rec:
                return [rec[nums[i]], i]
            else:
                t = target - nums[i]
                rec[t] = i


def main():
    nums = [2, 7, 11, 15]
    target = 9
    test = Solution()
    ret = test.twoSum(nums, target)
    print(ret)


if __name__ == '__main__':
    main()
