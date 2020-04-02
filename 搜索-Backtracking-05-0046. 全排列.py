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
            for x in nums:
                if x not in aux:
                    aux.add(x)
                    pre.append(x)
                    dfs()
                    pre.pop()
                    aux.remove(x)

        ret, pre, aux = [], [], set()
        dfs()
        return ret


def main():
    nums = [1, 2, 3]
    test = Solution()
    ret = test.permute(nums)
    print(ret)


if __name__ == '__main__':
    main()
