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
链接：https://leetcode-cn.com/problems/combination-sum-iv
    """
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        rec, count = {0: 1}, 0
        while rec:
            aux = {}
            for t in rec:
                for x in nums:
                    if x + t in aux:
                        aux[x + t] += rec[t]
                    elif x + t < target:
                        aux[x + t] = rec[t]
                    elif x + t == target:
                        count += rec[t]
            rec = aux
        return count
        # 512ms  5.51 %
        # 12.7MB  12.82 %


def main():
    nums, target = [1, 2, 3], 4
    test = Solution()
    ret = test.combinationSum4(nums, target)
    print(ret)


if __name__ == '__main__':
    main()
