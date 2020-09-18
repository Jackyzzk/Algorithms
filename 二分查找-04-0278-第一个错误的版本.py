# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    """
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。
由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。
实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
给定 n = 5，并且 version = 4 是第一个错误的版本。
调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。
链接：https://leetcode-cn.com/problems/first-bad-version/
    """
    def firstBadVersion(self, n, k):
        """
        :type n: int
        :rtype: int
        """
        def isBadVersion(version):
            if version >= k:
                return True

        p1, p2 = 1, n
        while p1 < p2:
            t = (p1 + p2) >> 1
            if isBadVersion(t):
                p2 = t  # t有可能是解，所以把解凑在 p2
            else:
                p1 = t + 1
        return p2


def main():
    n, k = 5, 4  # 4
    # n, k = 2, 1  # 1
    n, k = 2, 2  # 2
    test = Solution()
    ret = test.firstBadVersion(n, k)
    print(ret)


if __name__ == '__main__':
    main()
