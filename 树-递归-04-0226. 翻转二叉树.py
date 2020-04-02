# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
翻转一棵二叉树。
示例：
输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1
链接：https://leetcode-cn.com/problems/invert-binary-tree/
    """
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        root.left, root.right = root.right, root.left  # 放在前面会快一点，为什么？24 ms，11.8 MB
        self.invertTree(root.left)
        self.invertTree(root.right)
        # 放在这就慢一点，36 ms，11.6 MB
        return root


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    nums = [4, 2, 7, 1, 3, 6, 9]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.invertTree(root)
    print(ret)


if __name__ == '__main__':
    main()
