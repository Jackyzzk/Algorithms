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
        target = sum(nums)
        if target & 1:
            return False
        rec = 1  # 表示 0
        target = 1 << (target >> 1)
        for x in nums:
            rec |= rec << x  # 记录集合内元素所有可能的和标记在二进制位上
        if target & rec:
            return True
        return False


def main():
    nums = [1, 5, 11, 5]
    # nums = [1, 2, 3, 5]
    test = Solution()
    ret = test.canPartition(nums)
    print(ret)


if __name__ == '__main__':
    main()
