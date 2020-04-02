class Solution(object):
    """
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
链接：https://leetcode-cn.com/problems/subsets
    """
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        for x in nums:
            ret += [t + [x] for t in ret]
        return ret


def main():
    nums = [1, 2, 3]
    test = Solution()
    ret = test.subsets(nums)
    print(ret)


if __name__ == '__main__':
    main()
