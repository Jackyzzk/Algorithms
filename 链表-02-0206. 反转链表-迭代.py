# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
反转一个单链表。
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
链接：https://leetcode-cn.com/problems/reverse-linked-list/
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        left = None
        while p:
            right = p.next
            p.next = left
            left = p
            p = right
        return left


def create(nums):
    n = len(nums)
    a = ListNode(nums[0])
    x = a
    for i in range(1, n):
        x.next = ListNode(nums[i])
        x = x.next
    return a


def main():
    list1 = [1, 2, 3, 4, 5]
    a = create(list1)
    test = Solution()
    ret = test.reverseList(a)
    print(ret)


if __name__ == '__main__':
    main()
