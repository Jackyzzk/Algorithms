class Solution(object):
    """
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
一共有5种方法让最终目标和为3。
数组非空，且长度不会超过20。
初始的数组的和不会超过1000。
保证返回的最终结果能被32位整数存下。
Positive, Negative
sum(P) - sum(N) = target
sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
2 * sum(P) = target + sum(nums)
链接：https://leetcode-cn.com/problems/target-sum
    """
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        m = sum(nums)
        target = S + m
        if target & 1 or target > 2 * m:
            return 0
        target >>= 1
        rec = {0: 1}
        for x in nums:
            aux = {}
            for t in rec:
                aux[x + t] = rec.get(x + t, 0) + rec[t]
            rec.update(aux)
        return rec[target]
        # return rec


def main():
    # nums, s = [1, 1, 1, 1, 1], 3
    # nums, s = [0, 2, 4, 6], 2
    nums, s = [0, 0, 0, 0, 0, 0, 0, 0, 1], 1
    # nums, s = [7, 9, 3, 8, 0, 2, 4, 8, 3, 9], 0  # 0
    # nums, s = [8, 0, 8, 5], 0
    # nums, s = [3, 0, 4, 3, 9], 0
    test = Solution()
    ret = test.findTargetSumWays(nums, s)
    print(ret)


if __name__ == '__main__':
    main()
