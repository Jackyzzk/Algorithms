# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
链接：https://leetcode-cn.com/problems/balanced-binary-tree/
    """
    def depth(self, root):
        # 用-1来表示不平衡，并提前阻断递归
        if not root:
            return 0
        n1 = self.depth(root.left)
        if n1 == -1:
            return -1
        n2 = self.depth(root.right)
        if n2 == -1:
            return -1
        return max(n1, n2) + 1 if abs(n1 - n2) <= 1 else -1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.depth(root) != -1


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
    # nums = [1, 2, 2, 3, 3, None, None, 4, 4]
    nums = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, None, None, 5, 5]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.isBalanced(root)
    print(ret)


if __name__ == '__main__':
    main()
