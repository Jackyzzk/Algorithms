# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
计算给定二叉树的所有左叶子之和。
    3
   / \
  9  20
    /  \
   15   7
在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
链接：https://leetcode-cn.com/problems/sum-of-left-leaves/
    """
    aux = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return root
        que, ret = [root], 0
        while que:
            p = que.pop()
            if p.right:
                que.append(p.right)
            if p.left:
                que.append(p.left)
            if p.left and not p.left.left and not p.left.right:
                ret += p.left.val
        return ret


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
    nums = [3, 9, 20, None, None, 15, 7]  # 24
    # nums = [1, 2, 3, 4, 5]  # 4
    nums = []
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.sumOfLeftLeaves(root)
    print(ret)


if __name__ == '__main__':
    main()
