# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
    """
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def bfs(root):
            que, res = [root], []
            while que:
                root = que.pop(0)
                if root:
                    res.append(root.val)
                    if root.left or root.right:
                        que.append(root.left)
                        que.append(root.right)
                else:
                    res.append(None)
            if not res[-1]:
                res.pop()
            return res

        def dfs(a, b):
            if a > b:
                return [None]
            ret = []
            for i in range(a, b + 1):  # 选一个做根节点
                if (a, i - 1) not in rec:
                    rec[a, i - 1] = dfs(a, i - 1)
                if (i + 1, b) not in rec:
                    rec[i + 1, b] = dfs(i + 1, b)
                for l in rec[a, i - 1]:
                    for r in rec[i + 1, b]:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ret.append(root)
            return ret

        if not n:
            return []
        rec = {}
        # return [bfs(x) for x in dfs(1, n)]
        return dfs(1, n)


def main():
    n = 3
    # n = 0  # []
    test = Solution()
    ret = test.generateTrees(n)
    print(ret)


if __name__ == '__main__':
    main()
