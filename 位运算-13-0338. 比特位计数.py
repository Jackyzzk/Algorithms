class Solution(object):
    """
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，
计算其二进制数中的 1 的数目并将它们作为数组返回。
输入: 2
输出: [0,1,1]
输入: 5
输出: [0,1,1,2,1,2]
给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数
（如 C++ 中的 __builtin_popcount）来执行此操作。
链接：https://leetcode-cn.com/problems/counting-bits
    """
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        opt = [0] * (num + 1)
        for i in range(num + 1):
            if i & 1:
                # 二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1
                opt[i] = opt[i - 1] + 1
            else:
                # 二进制表示中，偶数中 1 的个数一定和右移 1 位之后的那个数一样多，因为最低位是 0 右移不影响
                opt[i] = opt[i >> 1]
        return opt


def main():
    num = 5
    test = Solution()
    ret = test.countBits(num)
    print(ret)


if __name__ == '__main__':
    main()
