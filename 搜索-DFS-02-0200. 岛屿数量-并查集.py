class UnionFindSet(object):
    def __init__(self, row, column, k):
        self.parent = [[(i, j) for j in range(column)] for i in range(row)]
        self.count = k

    def find(self, node):
        x, y = node
        if self.parent[x][y] != (x, y):
            self.parent[x][y] = self.find(self.parent[x][y])
        return self.parent[x][y]

    def union(self, node1, node2):
        p1x, p1y = self.find(node1)
        p2x, p2y = self.find(node2)
        if (p1x, p1y) == (p2x, p2y):
            return
        self.count -= 1
        self.parent[p2x][p2y] = p1x, p1y


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
        row, column = len(grid), len(grid[0])
        count = sum(grid[i].count('1') for i in range(row))
        ufs = UnionFindSet(row, column, count)
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    for a, b in {(0, 1), (1, 0)}:
                        if 0 <= i + a < row and 0 <= j + b < column:
                            if grid[i + a][j + b] == '1':
                                ufs.union((i, j), (i + a, j + b))
        return ufs.count


def main():
    grid = \
[["1","1","1","1","0"],
 ["1","1","0","1","0"],
 ["1","1","0","0","0"],
 ["0","0","0","0","0"]]
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
