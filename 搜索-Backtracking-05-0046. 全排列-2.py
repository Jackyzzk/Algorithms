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
        def dfs():
            if len(pre) == len(nums):
                ret.append(pre[:])  # 切片是生成一个新的列表
                return
            for i, x in enumerate(nums):
                if not visit[i]:
                    visit[i] = 1
                    pre.append(x)
                    dfs()
                    pre.pop()
                    visit[i] = 0

        ret, pre = [], []
        n = len(nums)
        visit = [0] * n
        dfs()
        return ret


def main():
    nums = [1, 2, 3]
    test = Solution()
    ret = test.permute(nums)
    print(ret)


if __name__ == '__main__':
    main()
