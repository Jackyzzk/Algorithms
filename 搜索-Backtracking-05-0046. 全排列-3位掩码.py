class Solution(object):
    """
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
链接：https://leetcode-cn.com/problems/permutations/
    """
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 布尔数组在这题里的作用是判断某个位置上的元素是否已经使用过。有两种等价的替换方式：
        # （1）哈希表；
        # （2）位掩码，即使用一个整数表示布尔数组。此时可以将空间复杂度降到O(1)
        def dfs():
            # nonlocal visit
            if len(pre) == len(nums):
                ret.append(pre[:])  # 切片是生成一个新的列表
                return
            for i in range(len(nums)):
                if not 1 << i & self.visit:
                    self.visit |= 1 << i
                    pre.append(nums[i])
                    dfs()
                    pre.pop()
                    self.visit ^= 1 << i

        ret, pre, self.visit = [], [], 0
        dfs()
        return ret


def main():
    nums = [1, 2, 3]
    test = Solution()
    ret = test.permute(nums)
    print(ret)


if __name__ == '__main__':
    main()
