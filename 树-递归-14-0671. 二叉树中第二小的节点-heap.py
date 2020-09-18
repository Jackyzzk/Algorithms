# Definition for a binary tree node.
import heapq


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
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            que = [root]
            while que:
                p = que.pop()
                heapq.heappush(rec, p.val)
                if p.right:
                    que.append(p.right)
                if p.left:
                    que.append(p.left)

        rec = []
        dfs(root)
        m = heapq.heappop(rec)
        while rec:
            x = heapq.heappop(rec)
            if x != m:
                return x
        return -1


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
    nums = [2, 2, 5, None, None, 5, 7]  # 5
    nums = [2, 2, 2]  # -1
    nums = [1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.findSecondMinimumValue(root)
    print(ret)


if __name__ == '__main__':
    main()
