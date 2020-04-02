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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l2:
            return l1
        if not l1:
            return l2
        p1, p2 = l1, l2
        left, right = None, None
        while p1 and p2:
            if p2.val <= p1.val:
                if left:
                    left.next = p2
                left, right, = p2, p2.next
                p2.next, p2 = p1, right
            else:
                if p1.next:
                    left, p1 = p1, p1.next
                else:
                    p1.next = p2
                    break
        return l1 if l1.val < l2.val else l2


def create(nums):
    n = len(nums)
    a = ListNode(nums[0])
    x = a
    for i in range(1, n):
        x.next = ListNode(nums[i])
        x = x.next
    return a


def main():
    # list1 = [1, 2, 4]
    # list2 = [1, 3, 4]
    list1 = [1]
    list2 = [2]
    l1 = create(list1)
    l2 = create(list2)
    test = Solution()
    ret = test.mergeTwoLists(l1, l2)
    print(ret)


if __name__ == '__main__':
    main()
