class Solution(object):
    """
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
即任意两个皇后不能位于同一行，同一列，同一斜线
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
输入: 4
输出: [
 [". Q . .",  // 解法 1
  ". . . Q",
  "Q . . .",
  ". . Q ."],

 [". . Q .",  // 解法 2
  "Q . . .",
  ". . . Q",
  ". Q . ."]
]
解释: 4 皇后问题存在两个不同的解法。
链接：https://leetcode-cn.com/problems/n-queens
    """
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(i=0):
            if i == n:
                ret.append(['.' * x + 'Q' + '.' * (n - 1 - x) for x in rec])
                return
            for j in range(n):
                if occupy[i][j] < 1:  # 同一点汇集了多个约束，不能在回溯的时候用0-1分辨出来
                    rec.append(j)
                    for x in range(i + 1, n):
                        for y in range(n):
                            if y == j or x - i == abs(y - j):
                                occupy[x][y] += 1
                    dfs(i + 1)
                    rec.pop()
                    for x in range(i + 1, n):
                        for y in range(n):
                            if y == j or x - i == abs(y - j):
                                occupy[x][y] -= 1

        ret, rec = [], []
        occupy = [[0] * n for i in range(n)]
        dfs()
        return ret


def main():
    n = 4
    # n = 5  # 10个
    test = Solution()
    ret = test.solveNQueens(n)
    print(ret)


if __name__ == '__main__':
    main()
