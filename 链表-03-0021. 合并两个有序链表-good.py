# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/
    """
    def mergeTwoLists(self, p1, p2):
        """
        :type p1: ListNode
        :type p2: ListNode
        :rtype: ListNode
        """
        left = ass = ListNode(0)
        while p1 and p2:
            if p2.val <= p1.val:
                left.next, left = p2, p2
                p2 = p2.next
            else:
                left.next, left = p1, p1
                p1 = p1.next
        left.next = p2 if p2 else p1
        return ass.next


def create(nums):
    n = len(nums)
    a = ListNode(nums[0])
    x = a
    for i in range(1, n):
        x.next = ListNode(nums[i])
        x = x.next
    return a


def main():
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    # list1 = [1]
    # list2 = [2]
    l1 = create(list1)
    l2 = create(list2)
    test = Solution()
    ret = test.mergeTwoLists(l1, l2)
    print(ret)


if __name__ == '__main__':
    main()
