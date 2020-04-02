class Solution(object):
    """
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
链接：https://leetcode-cn.com/problems/surrounded-regions
    """
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 从边界开始寻找'O'联通分量，这些分量将被保留
        if not board:
            return None
        row, column = len(board), len(board[0])

        def dfs(x, y):
            board[x][y] = 'P'  # protect
            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x + a < row and 0 <= y + b < column:
                    if board[x + a][y + b] == 'O':
                        dfs(x + a, y + b)

        for j in range(column):  # 上下两边界
            if board[0][j] == 'O':
                dfs(0, j)
            if board[row - 1][j] == 'O':
                dfs(row - 1, j)
        for i in range(1, row - 1):  # 左右两边界
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][column - 1] == 'O':
                dfs(i, column - 1)
        for i in range(row):
            for j in range(column):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'P':
                    board[i][j] = 'O'
        return board


def main():
    board = \
[["X","X","X","X"],
 ["X","O","O","X"],
 ["X","X","O","X"],
 ["X","O","X","X"]]
    # board = []
#     board = \
# [["O","O","O"],
#  ["O","O","O"],
#  ["O","O","O"]]  # 结果不变
#     board = \
# [["O","X","X","O","X"],
#  ["X","O","O","X","O"],
#  ["X","O","X","O","X"],
#  ["O","X","O","O","O"],
#  ["X","X","O","X","O"]]
# [["O", "X", "X", "O", "X"],
#  ["X", "X", "X", "X", "O"],
#  ["X", "X", "X", "O", "X"],
#  ["O", "X", "O", "O", "O"],
#  ["X", "X", "O", "X", "O"]]
    board = \
[["O","O","O","O","X","X"],
 ["O","O","O","O","O","O"],
 ["O","X","O","X","O","O"],
 ["O","X","O","O","X","O"],
 ["O","X","O","X","O","O"],
 ["O","X","O","O","O","O"]]
# [["O", "O", "O", "O", "X", "X"],
#  ["O", "O", "O", "O", "O", "O"],
#  ["O", "X", "O", "X", "O", "O"],
#  ["O", "X", "O", "O", "X", "O"],
#  ["O", "X", "O", "X", "O", "O"],
#  ["O", "X", "O", "O", "O", "O"]]
    board = \
[["X","O","X"],
 ["O","X","O"],
 ["X","O","X"]]
# [["X", "O", "X"],
#  ["O", "X", "O"],
#  ["X", "O", "X"]]
    test = Solution()
    ret = test.solve(board)
    print(ret)


if __name__ == '__main__':
    main()
