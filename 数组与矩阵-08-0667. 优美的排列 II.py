class Solution(object):
    """
给定两个整数 n 和 k，你需要实现一个数组，这个数组包含从 1 到 n 的 n 个不同整数，同时满足以下条件：
1、如果这个数组是 [a1, a2, a3, ... , an] ，那么数组 [|a1 - a2|, |a2 - a3|,
|a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数；
2、如果存在多种答案，你只需实现并返回其中任意一种.
输入: n = 3, k = 1
输出: [1, 2, 3]
解释: [1, 2, 3] 包含 3 个范围在 1-3 的不同整数， 并且 [1, 1] 中有且仅有 1 个不同整数 : 1
输入: n = 3, k = 2
输出: [1, 3, 2]
解释: [1, 3, 2] 包含 3 个范围在 1-3 的不同整数， 并且 [2, 1] 中有且仅有 2 个不同整数: 1 和 2
 n 和 k 满足条件 1 <= k < n <= 104.
链接：https://leetcode-cn.com/problems/beautiful-arrangement-ii
    """
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        p1, p2 = 2, n
        count = 1
        ret = [1]
        while p1 != p2 + 1:
            if count < k:
                count += 1
                if count % 2:
                    ret.append(p1)
                    p1 += 1
                else:
                    ret.append(p2)
                    p2 -= 1
            elif count % 2:
                ret.extend([x for x in range(p1, p2 + 1)])
                break
            else:
                ret.extend([x for x in range(p2, p1 - 1, -1)])
                break
        return ret




def main():
    n, k = 5, 1
    # n, k = 5, 4  # [1,5,2,4,3]
    test = Solution()
    ret = test.constructArray(n, k)
    print(ret)


if __name__ == '__main__':
    main()
