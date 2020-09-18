# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。
s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。
给定的树 s:
     3
    / \
   4   5
  / \
 1   2
给定的树 t：
   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
给定的树 s：
     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：
   4
  / \
 1   2
返回 false。
链接：https://leetcode-cn.com/problems/subtree-of-another-tree/
    """
    def judge(self, t1, t2):  # 判断是不是一样的
        if not (t1 or t2):  # not t1 and not t2，都是空
            return True
        elif not (t1 and t2):  # not t1 or not t2，只有一个空，剩下就都不是空
            return False
        if t1.val == t2.val:
            b1 = self.judge(t1.left, t2.left)
            b2 = self.judge(t1.right, t2.right)
            return b1 and b2
        else:
            return False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s:
            return self.judge(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        return False


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
    nums1 = [3, 4, 5, 1, 2]
    # nums1 = [3, 4, 5, 1, 2, None, None, None, 0, 0]
    nums2 = [4, 1, 2]
    # nums1 = [1, 1]
    # nums2 = [1]
    # nums1 = [3, 4, 5, 1, None, 2]
    # nums2 = [3, 1, 2]
    global m
    m = len(nums1)
    s = create(nums1, 0)
    m = len(nums2)
    t = create(nums2, 0)
    test = Solution()
    ret = test.isSubtree(s, t)
    print(ret)


if __name__ == '__main__':
    main()
