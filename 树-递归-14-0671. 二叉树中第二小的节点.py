# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。
如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 
给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
输入:
    2
   / \
  2   5
     / \
    5   7
输出: 5
说明: 最小的值是 2 ，第二小的值是 5 。
输入:
    2
   / \
  2   2
输出: -1
说明: 最小的值是 2, 但是不存在第二小的值。
链接：https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/
    """
    i = j = 0  # i < j
    t = True

    def find(self, root):
        if self.t:
            if root.val > self.j:
                self.j, self.t = root.val, False
                return 0
        else:
            if self.i < root.val < self.j:
                self.j = root.val
                return 0
        if root.left:
            self.find(root.left)
        if root.right:
            self.find(root.right)

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.i = self.j = root.val
        self.find(root)
        if self.i != self.j:
            return self.j
        return -1


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    nums = [2, 2, 5, None, None, 5, 7]  # 5
    # nums = [2, 2, 2]  # -1
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.findSecondMinimumValue(root)
    print(ret)


if __name__ == '__main__':
    main()
