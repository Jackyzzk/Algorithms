class Solution(object):
    """
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。
注意： 0 ≤ x, y < 2 ** 31.
输入:  x = 1, y = 4
输出:  2
解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
链接：https://leetcode-cn.com/problems/hamming-distance
    """
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        t = x ^ y
        count = 0
        while t:
            t &= t - 1  # t & (t - 1)可以去掉 t 二进制表示的最后一个 1
            count += 1
        return count


def main():
    x = 1
    y = 4
    test = Solution()
    ret = test.hammingDistance(x, y)
    print(ret)


if __name__ == '__main__':
    main()
