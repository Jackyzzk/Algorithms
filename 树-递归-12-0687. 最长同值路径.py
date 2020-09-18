# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。
这条路径可以经过也可以不经过根节点。
注意：两个节点之间的路径长度由它们之间的边数表示。
输入:
              5
             / \
            4   5
           / \   \
          1   1   5
输出:  2
输入:
              1
             / \
            4   5
           / \   \
          4   4   5
输出:  2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
链接：https://leetcode-cn.com/problems/longest-univalue-path/
    """
    count = 0

    def dfs(self, root):  # 返回的是 经过root且都是root.val的最大深度
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if root.left and root.left.val != root.val:  # 自底向上
            left = 0
        if root.right and root.right.val != root.val:  # 如果不加这两句就是求最大深度
            right = 0
        if left + right > self.count:
            self.count = left + right
        return max(left, right) + 1

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.count


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


def main():
    # nums = [5, 4, 5, 1, 1, None, 5]  # 2
    nums = [1, 4, 5, 4, 4, None, 5]  # 2
    # nums = [1, None, 1, None, None, 1, 1, None, None, None, None, 1, 1, 1]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.longestUnivaluePath(root)
    print(ret)


if __name__ == '__main__':
    main()
