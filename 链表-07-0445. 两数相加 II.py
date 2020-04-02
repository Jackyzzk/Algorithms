# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。
它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
进阶:
如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7
链接：https://leetcode-cn.com/problems/add-two-numbers-ii/
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rec1, rec2 = [], []
        p1, p2 = l1, l2
        while p1:
            rec1.append(p1.val)
            p1 = p1.next
        while p2:
            rec2.append(p2.val)
            p2 = p2.next
        n1, n2 = len(rec1), len(rec2)
        n = max(n1, n2)
        rec1[0:0] = [0] * (n - n1 + 1)
        rec2[0:0] = [0] * (n - n2 + 1)
        plus = 0
        for i in range(n, -1, -1):
            t = rec1[i] + rec2[i] + plus
            plus = t // 10
            rec1[i] = t % 10
        if rec1[0] == 0:
            rec1[0:2] = [rec1[1]]
        return create(rec1)


def create(nums):
    n = len(nums)
    aux = ListNode(0)
    p = aux
    for i in range(n):
        p.next = ListNode(nums[i])
        p = p.next
    return aux.next


def main():
    list1 = [7, 2, 4, 3]
    list2 = [5, 6, 4]
    l1 = create(list1)
    l2 = create(list2)
    test = Solution()
    ret = test.addTwoNumbers(l1, l2)
    print(ret)


if __name__ == '__main__':
    main()

