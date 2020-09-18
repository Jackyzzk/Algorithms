class Solution(object):
    """
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向
(水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
示例 2:
[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。
注意: 给定的矩阵grid 的长度和宽度都不超过 50。
链接：https://leetcode-cn.com/problems/max-area-of-island
    """
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, column, ret = len(grid), len(grid[0]), 0
        direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def dfs(x, y):
            grid[x][y] = 0
            que, count = [(x, y)], 1
            while que:
                x, y = que.pop()
                for a, b in direction:
                    if 0 <= x + a < row and 0 <= y + b < column:
                        if grid[x + a][y + b] == 1:
                            que.append((x + a, y + b))
                            grid[x + a][y + b] = 0
                            count += 1
            return count

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    ret = max(ret, dfs(i, j))
        return ret


def main():
    grid = \
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    test = Solution()
    ret = test.maxAreaOfIsland(grid)
    print(ret)


if __name__ == '__main__':
    main()
