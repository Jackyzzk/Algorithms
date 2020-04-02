class Solution(object):
    """
在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
输入:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
输出:
[[1,2,3,4]]
解释: 行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
输入:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
输出:
[[1,2],
 [3,4]]
解释: 没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
给定矩阵的宽和高范围在 [1, 100]。给定的 r 和 c 都是正数。
链接：https://leetcode-cn.com/problems/reshape-the-matrix
    """
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        aux = []
        for x in nums:
            aux += x
        n = len(aux)
        if r * c != n:
            return nums
        # ret = [[]] * r  # ret[0] 到 ret[r - 1] 都指向了同一个空列表[]
        ret = [[] for i in range(r)]  # ret[0] 到 ret[r - 1] 都是空列表[]，但不是同一个[]
        for i in range(r):
            for j in range(c):
                ret[i].append(aux[i * c + j])
        return ret


def main():
    # nums = [[1, 2], [3, 4]]
    # r = 1
    # c = 4
    nums = [[1, 2], [3, 4]]
    r = 4
    c = 1
    test = Solution()
    ret = test.matrixReshape(nums, r, c)
    print(ret)


if __name__ == '__main__':
    main()
