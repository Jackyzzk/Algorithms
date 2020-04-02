class Solution(object):
    """
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。
输入: [1,1,2,3,3,4,4,8,8]
输出: 2
输入: [3,3,7,7,10,11,11]
输出: 10
注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。
链接：https://leetcode-cn.com/problems/single-element-in-a-sorted-array/
    """
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(nums) - 1
        while p1 < p2 - 1:
            t = (p1 + p2) >> 1
            if t & 1:  # 奇数
                if nums[t] == nums[t - 1]:
                    p1 = t + 1
                else:
                    p2 = t
            else:  # 偶数
                if nums[t] != nums[t + 1]:
                    p2 = t + 1
                else:
                    p1 = t + 2
        return nums[p1]  # 先想好把解放在哪一边


def main():
    # nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    # nums = [3, 3, 7, 7, 10, 11, 11]
    # nums = [1, 1, 2, 3, 3]
    nums = [1, 2, 2, 3, 3]
    test = Solution()
    ret = test.singleNonDuplicate(nums)
    print(ret)


if __name__ == '__main__':
    main()
