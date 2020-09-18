# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
请判断一个链表是否为回文链表。
输入: 1->2
输出: false
输入: 1->2->2->1
输出: true
进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
链接：https://leetcode-cn.com/problems/palindrome-linked-list/
    """
    def reverse(self, head):
        left, p = None, head
        while p:
            p.next, p, left = left, p.next, p
        return left

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p, n = head, 0
        while p:
            n += 1
            p = p.next
        p = head
        for i in range(n // 2):
            p = p.next
        last = self.reverse(p)
        p1, p2 = head, last
        for i in range(n // 2):
            if p1.val == p2.val:
                p1, p2 = p1.next, p2.next
            else:
                return False
        return True


def create(nums):
    n = len(nums)
    aux = ListNode(0)
    p = aux
    for i in range(n):
        p.next = ListNode(nums[i])
        p = p.next
    return aux.next


def main():
    list1 = [1, 2, 2, 1]
    # list2 = [5, 6, 4]
    head = create(list1)
    test = Solution()
    ret = test.isPalindrome(head)
    print(ret)


if __name__ == '__main__':
    main()
