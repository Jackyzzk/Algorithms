# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，在树的最后一行找到最左边的值。
输入:
    2
   / \
  1   3
输出:  1
输入:
    1
   / \
  2   3
 /   / \
4   5   6
   /
  7
输出:  7
注意: 您可以假设树（即给定的根节点）不为 NULL。
链接：https://leetcode-cn.com/problems/find-bottom-left-tree-value/
    """
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        que = [root]
        while que:
            p = que.pop(0)
            if p.right:  # 根右左遍历，最后剩下的就是最左边的
                que.append(p.right)
            if p.left:
                que.append(p.left)
        return p.val


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    nums = [1, 2, 3, 4, None, 5, 6, None, None, None, None, 7]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.findBottomLeftValue(root)
    print(ret)


if __name__ == '__main__':
    main()
