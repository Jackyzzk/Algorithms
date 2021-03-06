class Solution(object):
    """
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
输入: [3,0,1]
输出: 2
输入: [9,6,4,2,3,5,7,0,1]
输出: 8
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
链接：https://leetcode-cn.com/problems/missing-number
    """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, ret = len(nums), 0
        for i in range(n):
            ret ^= nums[i] ^ i
        return ret ^ n


def main():
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    # nums = [3, 0, 1]
    test = Solution()
    ret = test.missingNumber(nums)
    print(ret)


if __name__ == '__main__':
    main()
