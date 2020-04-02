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
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
输入: [3,4,5,1,3,null,1]
     3
    / \
   4   5
  / \   \
 1   3   1
输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
链接：https://leetcode-cn.com/problems/house-robber-iii/
    """
    def dp(self, cur):
        if not cur:
            return [0, 0]

        l = self.dp(cur.left)
        r = self.dp(cur.right)

        return [max(l) + max(r), cur.val + l[0] + r[0]]

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dp(root))


def create(nums, i):
    if nums[i] is None:
        return None
    root = TreeNode(nums[i])
    root.left = create(nums, i * 2 + 1) if i * 2 + 1 < m else None
    root.right = create(nums, i * 2 + 2) if i * 2 + 2 < m else None
    return root


def main():
    # nums = [3, 2, 3, None, 3, None, 1]  # 7
    nums = [3, 4, 5, 1, 3, None, 1]  # 9
    # nums = [4, 1, None, 2, None, None, None, 3]  # 7
    global m
    m = len(nums)
    root = create(nums, 0)
    test = Solution()
    ret = test.rob(root)
    print(ret)


if __name__ == '__main__':
    main()
