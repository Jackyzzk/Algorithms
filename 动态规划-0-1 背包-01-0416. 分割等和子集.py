class Solution(object):
    """
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意: 每个数组中的元素不会超过 100，数组的大小不会超过 200
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
    """
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        if nums_sum & 1:
            return False
        n = len(nums)
        half_sum = nums_sum >> 1
        opt = [[False] * (half_sum + 1) for i in range(n + 1)]  # 前 i 个数能否构成和为 j
        opt[0][0] = False

        for i in range(1, n + 1):
            for j in range(1, half_sum + 1):
                if j > nums[i - 1]:
                    opt[i][j] = True if opt[i - 1][j - nums[i - 1]] or opt[i - 1][j] else False
                elif j < nums[i - 1]:
                    opt[i][j] = True if opt[i - 1][j] else False
                else:
                    opt[i][j] = True
        return opt[-1][-1]


def main():
    nums = [1, 5, 11, 5]
    nums = [1, 2, 3, 5]
    # nums = []
    test = Solution()
    ret = test.canPartition(nums)
    print(ret)


if __name__ == '__main__':
    main()
