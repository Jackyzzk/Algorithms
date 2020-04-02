class Solution(object):
    """
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
你需要让组成和的完全平方数的个数最少。
输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
链接：https://leetcode-cn.com/problems/perfect-squares
    """
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        que, aux, count = [n], [], 1
        while que:
            t = que.pop()
            root = int(t ** 0.5)
            for i in range(1, root + 1):
                if t == i * i:
                    return count
                if t <= 3 * i * i:  # 一个正整数一定可以用4个平方和表示，如果是4个一样则还可以用更少个数的平方和表示
                    aux.append(t - i * i)
            if not que:
                que, aux = aux, que  # 一个队列存同一层的元素
                count += 1


def main():
    n = 12
    test = Solution()
    ret = test.numSquares(n)
    print(ret)


if __name__ == '__main__':
    main()
