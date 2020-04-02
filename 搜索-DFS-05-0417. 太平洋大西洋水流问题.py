class Solution(object):
    """
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。
“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。
规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。
提示：输出坐标的顺序不重要, m 和 n 都小于150
给定下面的 5x5 矩阵:
  太平洋 ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋
返回:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow/
    """
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return None
        row, column = len(matrix), len(matrix[0])
        visit = [[0] * column for i in range(row)]  # 0:未访问  1:到达太平洋  2:到达大西洋  3:均可到达

        def dfs(x, y, k):
            if visit[x][y] >= k:
                return
            que = [(x, y)]
            visit[x][y] += k
            while que:
                x, y = que.pop()
                for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= x + a < row and 0 <= y + b < column:
                        if visit[x + a][y + b] < k and matrix[x + a][y + b] >= matrix[x][y]:
                            que.append((x + a, y + b))
                            visit[x + a][y + b] += k

        for j in range(column):
            dfs(0, j, 1)
        for i in range(row):
            dfs(i, 0, 1)
        for j in range(column):
            dfs(row - 1, j, 2)
        for i in range(row):
            dfs(i, column - 1, 2)

        return [[i, j] for i in range(row) for j in range(column) if visit[i][j] == 3]


def main():
    matrix = \
    [[1,2,2,3,5],
     [3,2,3,4,4],
     [2,4,5,3,1],
     [6,7,1,4,5],
     [5,1,1,2,4]]
    test = Solution()
    ret = test.pacificAtlantic(matrix)
    print(ret)


if __name__ == '__main__':
    main()
