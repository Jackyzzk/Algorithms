# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，
使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
输入: 二叉搜索树:
              5
            /   \
           2     13
输出: 转换为累加树:
             18
            /   \
          20     13
链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
    """
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        que, p, aux = [], root, 0
        while que or p:
            while p:
                que.append(p)
                p = p.right
            p = que.pop()
            aux += p.val
            p.val = aux
            p = p.left
        return root


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
    nums = [5, 2, 13]
    global m
    m = len(nums)
    root = create(nums, 0)
    bfs(root)
    test = Solution()
    ret = test.convertBST(root)
    bfs(ret)
    print(ret)


if __name__ == '__main__':
    main()
