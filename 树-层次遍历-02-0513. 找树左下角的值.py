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
        n, p = len(que), root
        while n != 0:
            for i in range(n):
                p = que.pop(0)
                if p.right:  # 根右左遍历，最后剩下的就是最左边的
                    que.append(p.right)
                if p.left:
                    que.append(p.left)
            n = len(que)
        return p.val


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
    nums = [1, 2, 3, 4, None, 5, 6, None, None, None, None, 7]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.findBottomLeftValue(root)
    print(ret)


if __name__ == '__main__':
    main()
