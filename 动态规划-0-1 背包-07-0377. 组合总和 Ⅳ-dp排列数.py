class Solution(object):
    """
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
nums = [1, 2, 3]
target = 4
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
因此输出为 7。
如果给定的数组中含有负数会怎么样？
问题会产生什么变化？
我们需要在题目中添加什么限制来允许负数的出现？
求解顺序的完全背包问题时，对物品的迭代应该放在最里层，
对背包的迭代放在外层，只有这样才能让物品按一定顺序放入背包中。
链接：https://leetcode-cn.com/problems/combination-sum-iv
    """
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        opt = [0] * (target + 1)
        opt[0] = 1
        for i in range(1, target + 1):
            for x in nums:
                if x <= i:
                    opt[i] += opt[i - x]
        return opt[-1]


def main():
    nums, target = [1, 2, 3], 4
    test = Solution()
    ret = test.combinationSum4(nums, target)
    print(ret)


if __name__ == '__main__':
    main()
