class Solution(object):
    """
给定一个整数，写一个函数来判断它是否是 3 的幂次方。
输入: 27   输出: true
输入: 0    输出: false
输入: 9    输出: true
输入: 45   输出: false
进阶：你能不使用循环或者递归来完成本题吗？
链接：https://leetcode-cn.com/problems/power-of-three/
    """
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # return n > 0 and (1162261467 % n == 0)  # 进阶解法
        if n < 1:
            return False
        t = 0
        while n > 1 and t == 0:
            t = n % 3
            n = n // 3
        if t != 0:
            return False
        else:
            return True


def main():
    n = 2
    test = Solution()
    ret = test.isPowerOfThree(n)
    print(ret)


if __name__ == '__main__':
    main()
