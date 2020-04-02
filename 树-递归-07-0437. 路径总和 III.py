# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
返回 3。和等于 8 的路径有:
1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
链接：https://leetcode-cn.com/problems/path-sum-iii/
    """
    count = 0

    def path(self, root, sum):
        if not root:
            return 0
        if sum == root.val:
            self.count += 1
        self.path(root.left, sum - root.val)
        self.path(root.right, sum - root.val)
        return 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.path(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.count


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    # nums = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    # h = 8  # 3
    nums = [1, -2, -3, 1, 3, -2, None, -1]
    h = -1  # 4
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.pathSum(root, h)
    print(ret)


if __name__ == '__main__':
    main()
