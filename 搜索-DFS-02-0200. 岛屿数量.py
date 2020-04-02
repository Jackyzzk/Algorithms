class Solution(object):
    """
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。
输入:
11110
11010
11000
00000
输出: 1
输入:
11000
11000
00100
00011
输出: 3
链接：https://leetcode-cn.com/problems/number-of-islands
    """
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row, column, count = len(grid), len(grid[0]), 0

        def dfs(x, y):
            grid[x][y] = None
            que = [(x, y)]
            while que:
                x, y = que.pop()
                for a, b in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
                    if 0 <= x + a < row and 0 <= y + b < column:
                        if grid[x + a][y + b] == '1':
                            que.append((x + a, y + b))
                            grid[x + a][y + b] = None

        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count


def main():
#     grid = \
# [["1","1","1","1","0"],
#  ["1","1","0","1","0"],
#  ["1","1","0","0","0"],
#  ["0","0","0","0","0"]]
    grid = \
[["1","1","0","0","0"],
 ["1","1","0","0","0"],
 ["0","0","1","0","0"],
 ["0","0","0","1","1"]]  # 3
    # grid = []
    test = Solution()
    ret = test.numIslands(grid)
    print(ret)


if __name__ == '__main__':
    main()
