class Solution(object):
    """
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
输入: [2,2,1]
输出: 1
输入: [4,1,2,1,2]
输出: 4
链接：https://leetcode-cn.com/problems/single-number
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for x in nums:
            ret ^= x  # 异或运算具有交换律和结合律 t ^ t = 0, t ^ 0 = t
        return ret


def main():
    nums = [4, 1, 2, 1, 2]
    # nums = [2, 2, 1]
    test = Solution()
    ret = test.singleNumber(nums)
    print(ret)


if __name__ == '__main__':
    main()
