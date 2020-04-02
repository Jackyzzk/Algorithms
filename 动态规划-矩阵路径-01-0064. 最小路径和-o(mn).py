class Solution(object):
    """
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
链接：https://leetcode-cn.com/problems/minimum-path-sum
    """
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])
        opt = [[0] * column for i in range(row)]
        for i in range(row):
            for j in range(column):
                if i and j:
                    opt[i][j] = min(opt[i - 1][j], opt[i][j - 1]) + grid[i][j]
                else:
                    opt[i][j] = opt[i - 1][j] + opt[i][j - 1] + grid[i][j]  # opt[-1]逆着取会取到0不产生影响
        return opt[-1][-1]
        # return opt


def main():
    grid = \
[
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
    test = Solution()
    ret = test.minPathSum(grid)
    print(ret)


if __name__ == '__main__':
    main()
