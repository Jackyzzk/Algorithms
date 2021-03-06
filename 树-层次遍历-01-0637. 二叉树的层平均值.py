# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
节点值的范围在32位有符号整数范围内。
链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
    """
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        que, ret = [root], []
        n, aux = len(que), 0
        while n != 0:
            for t in range(n):
                p = que.pop(0)
                aux += p.val
                if p.left:
                    que.append(p.left)
                if p.right:
                    que.append(p.right)
            ret.append(float(aux) / n)
            n, aux = len(que), 0
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
    nums = [3, 9, 20, None, None, 15, 7]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.averageOfLevels(root)
    print(ret)


if __name__ == '__main__':
    main()
