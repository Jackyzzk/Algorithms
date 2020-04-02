class Solution(object):
    """
编写一个程序，通过已填充的空格来解决数独问题。
一个数独的解法需遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
     5  3  . | .  7  . | .  .  .
     6  .  . | 1  9  5 | .  .  .
     .  9  8 | .  .  . | .  6  .
     ---------------------------
     8  .  . | .  6  . | .  .  3
     4  .  . | 8  .  3 | .  .  1
     7  .  . | .  2  . | .  .  6
     ---------------------------
     .  6  . | .  .  . | 2  8  .
     .  .  . | 4  1  9 | .  .  5
     .  .  . | .  8  . | .  7  9
答案
     5  3  4 | 6  7  8 | 9  1  2
     6  7  2 | 1  9  5 | 3  4  8
     1  9  8 | 3  4  2 | 5  6  7
     ---------------------------
     8  5  9 | 7  6  1 | 4  2  3
     4  2  6 | 8  5  3 | 7  9  1
     7  1  3 | 9  2  4 | 8  5  6
     ---------------------------
     9  6  1 | 5  3  7 | 2  8  4
     2  8  7 | 4  1  9 | 6  3  5
     3  4  5 | 2  8  6 | 1  7  9
给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
链接：https://leetcode-cn.com/problems/sudoku-solver
    """
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(pre=0):
            if pre == n:
                return True
            for j in range(pre, n):
                a, b = que[j]
                t = (a // 3) * 3 + b // 3
                num_set = (row[a] | column[b] | box[t]) ^ 0b1111111111
                for num in range(1, 10):
                    temp = 1 << num
                    if num_set & temp:
                        board[a][b] = str(num)
                        row[a] |= temp
                        column[b] |= temp
                        box[t] |= temp
                        if dfs(j + 1):
                            return True
                        row[a] ^= temp
                        column[b] ^= temp
                        box[t] ^= temp
                return False

        row, column, box = [0] * 9, [0] * 9, [0] * 9
        que = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    x = 1 << int(board[i][j])
                    k = (i // 3) * 3 + j // 3
                    row[i] |= x
                    column[j] |= x
                    box[k] |= x
                else:
                    que.append((i, j))
        n = len(que)
        dfs()
        return board


def main():
    board = \
    [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
    test = Solution()
    ret = test.solveSudoku(board)
    print(ret)


if __name__ == '__main__':
    main()
