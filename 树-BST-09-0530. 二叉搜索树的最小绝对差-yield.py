# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。
输入:
   1
    \
     3
    /
   2
输出:  1
最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
注意: 树中至少有2个节点。
链接：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
    """
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            que, p = [], root
            while que or p:
                while p:
                    que.append(p)
                    p = p.left
                p = que.pop()
                yield p.val
                p = p.right
            yield None

        gen = dfs(root)
        a, b = next(gen), next(gen)
        aux = b - a
        while b:
            if b - a < aux:
                aux = b - a
            else:
                a, b = b, next(gen)
        return aux


def create(nums, i):
    if not nums:
        return None
    root = TreeNode(nums.pop(0))
    que = [root]
    while que:
        node = que.pop(0)
        left = nums.pop(0) if nums else None
        right = nums.pop(0) if nums else None
        node.left = TreeNode(left) if left is not None else None
        node.right = TreeNode(right) if right is not None else None
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    return root


def bfs(root):
    if not root:
        return root
    que, ret = [root], []
    while que:
        p = que.pop(0)
        ret.append(p.val)
        if p.left:
            que.append(p.left)
        if p.right:
            que.append(p.right)
    print(ret)


def main():
    nums = [1, None, 3, None, None, 2]
    global m
    m = len(nums)
    root = create(nums, 0)
    bfs(root)
    test = Solution()
    ret = test.getMinimumDifference(root)
    # bfs(ret)
    print(ret)


if __name__ == '__main__':
    main()
