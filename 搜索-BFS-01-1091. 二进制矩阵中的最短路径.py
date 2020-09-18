class Solution(object):
    """
在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。
一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：
相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
C_1 位于 (0, 0)（即，值为 grid[0][0]）
C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。
输入：[[0,1],[1,0]]
输出：2
输入：[[0,0,0],[1,1,0],[1,1,0]]
输出：4
1 <= grid.length == grid[0].length <= 100
grid[i][j] 为 0 或 1
链接：https://leetcode-cn.com/problems/shortest-path-in-binary-matrix
    """
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def judge(a, b):
            if 0 <= a < m and 0 <= b < n:
                if not grid[a][b] and not visit[a][b]:
                    aux.append((a, b))
                    visit[a][b] = 1

        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        visit = [[0] * n for i in range(m)]
        que, aux = [(0, 0)], []
        visit[0][0], count = 1, 1

        while que:
            x, y = que.pop()  # 因为有 aux 辅助换层，这里可以不填 0
            if (x, y) == (m - 1, n - 1):
                return count
            judge(x - 1, y - 1)
            judge(x, y - 1)
            judge(x + 1, y - 1)
            judge(x - 1, y)
            judge(x + 1, y)
            judge(x - 1, y + 1)
            judge(x, y + 1)
            judge(x + 1, y + 1)
            if not que:
                que, aux = aux, que
                count += 1
        return -1


def main():
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    # grid = [[0, 1], [1, 0]]
    # grid = []
    # grid = [[0]]
    test = Solution()
    ret = test.shortestPathBinaryMatrix(grid)
    print(ret)


if __name__ == '__main__':
    main()
