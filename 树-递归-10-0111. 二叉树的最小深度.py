# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
    """
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        n1 = self.minDepth(root.left)
        n2 = self.minDepth(root.right)
        if n2 == 0:  # 保证是叶子节点
            return n1 + 1
        if n1 == 0:
            return n2 + 1
        return min(n1, n2) + 1


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
    # nums = [3, 9, 20, None, None, 15, 7]
    nums = [1, 2]  # 2
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.minDepth(root)
    print(ret)


if __name__ == '__main__':
    main()
