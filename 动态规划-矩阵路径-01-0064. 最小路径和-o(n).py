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
        opt = [0] * column
        for i in range(row):
            for j in range(column):
                if i and j:
                    opt[j] = min(opt[j - 1], opt[j]) + grid[i][j]
                elif i:  # 第一列
                    opt[j] = opt[j] + grid[i][j]
                else:  # 第一行，第一个时，opt[-1]取到0没有影响
                    opt[j] = opt[j - 1] + grid[i][j]
        return opt[-1]


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
