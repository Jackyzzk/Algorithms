# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __len__(self):
        p = self
        count = 0
        while p is not None:
            count += 1
            p = p.next
        return count


class Solution(object):
    """
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
返回一个符合上述规则的链表的列表。
举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]

输入: root = [1, 2, 3], k = 5
输出: [[1],[2],[3],[],[]]
输入: root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

root 的长度范围： [0, 1000].
输入的每个节点的大小范围：[0, 999].
k 的取值范围： [1, 50].
链接：https://leetcode-cn.com/problems/split-linked-list-in-parts/
    """
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        n = len(root)
        p = root
        man = [n // k] * k
        ret = []
        for i in range(n % k):
            man[i] += 1
        for i in range(k):
            ret[k:k] = [p]
            for j in range(man[i] - 1):
                p = p.next
            if p:
                p.next, p = None, p.next
        return ret


def create(nums):
    n = len(nums)
    aux = ListNode(0)
    p = aux
    for i in range(n):
        p.next = ListNode(nums[i])
        p = p.next
    return aux.next


def main():
    # list1 = [1, 2, 3]
    # k = 5
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    # list2 = [5, 6, 4]
    root = create(list1)
    test = Solution()
    ret = test.splitListToParts(root, k)
    print(ret)


if __name__ == '__main__':
    main()
