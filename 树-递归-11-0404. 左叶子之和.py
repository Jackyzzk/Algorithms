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
        def aux_sum(root):
            if not root:
                return 0
            if root.left:
                if not root.left.left and not root.left.right:
                    self.aux += aux_sum(root.left)
                else:
                    aux_sum(root.left)
            aux_sum(root.right)
            return root.val

        aux_sum(root)
        return self.aux


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    nums = [3, 9, 20, None, None, 15, 7]  # 24
    # nums = [1, 2, 3, 4, 5]  # 4
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.sumOfLeftLeaves(root)
    print(ret)


if __name__ == '__main__':
    main()
