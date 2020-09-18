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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.pre_sum = 0
        self.count = 0
        self.target = sum
        rec = {0: 1}

        def dfs(root):
            if not root:
                return root

            self.pre_sum += root.val
            if self.pre_sum - self.target in rec:
                self.count += rec[self.pre_sum - self.target]
            rec[self.pre_sum] = rec.get(self.pre_sum, 0) + 1

            dfs(root.left)
            dfs(root.right)

            rec[self.pre_sum] -= 1
            self.pre_sum -= root.val  # 这两步是回溯

        dfs(root)
        return self.count


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
    # nums = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    # h = 8  # 3
    nums = [1, -2, -3, 1, 3, -2, None, -1]
    h = -1  # 4
    nums = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    h = 22  # 3
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.pathSum(root, h)
    print(ret)


if __name__ == '__main__':
    main()
