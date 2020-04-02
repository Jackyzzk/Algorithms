class Solution(object):
    """
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些
水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
链接：https://leetcode-cn.com/problems/word-search/
    """
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(x, y, pre, rest):
            if not rest:
                return True
            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x + a < row and 0 <= y + b < column and (x + a, y + b) not in pre:
                    if board[x + a][y + b] == rest[0]:
                        if dfs(x + a, y + b, pre | {(x, y)}, rest[1:]):
                            return True
            return False

        row, column = len(board), len(board[0])
        for i in range(row):
            for j in range(column):
                if board[i][j] == word[0]:
                    if dfs(i, j, set(), word[1:]):
                        return True
        return False


def main():
    board = \
    [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    # word = "AB"
    # word = "SEE"
    word = "ABCB"
    # board = \
    # [["A", "B", "C", "E"],
    #  ["S", "F", "E", "S"],
    #  ["A", "D", "E", "E"]]
    # word = "ABCESEEEFS"  # true
    test = Solution()
    ret = test.exist(board, word)
    print(ret)


if __name__ == '__main__':
    main()
