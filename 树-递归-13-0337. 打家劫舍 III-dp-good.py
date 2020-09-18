# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
输入: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \
     3   1
输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
输入: [3,4,5,1,3,null,1]
     3
    / \
   4   5
  / \   \
 1   3   1
输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
链接：https://leetcode-cn.com/problems/house-robber-iii/
    """
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):  # 返回包括该节点的选 和 不选的最大值组成的列表 [ignore, select]
            if not root:
                return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)

            ignore = max(left) + max(right)
            select = root.val + left[0] + right[0]
            return [ignore, select]

        return max(dfs(root))


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
    nums = [3, 2, 3, None, 3, None, 1]  # 7
    nums = [3, 4, 5, 1, 3, None, 1]  # 9
    nums = [4, 1, None, 2, None, None, None, 3]  # 7
    nums = []
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.rob(root)
    print(ret)


if __name__ == '__main__':
    main()
