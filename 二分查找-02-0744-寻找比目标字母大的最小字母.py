class Solution(object):
    """
给定一个只包含小写字母的有序数组letters 和一个目标字母 target，
寻找有序数组里面比目标字母大的最小字母。数组里字母的顺序是循环的。
举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。
letters = ["c", "f", "j"], target = "a", 输出: "c"
letters = ["c", "f", "j"], target = "c", 输出: "f"
letters = ["c", "f", "j"], target = "d", 输出: "f"
letters = ["c", "f", "j"], target = "g", 输出: "j"
letters = ["c", "f", "j"], target = "j", 输出: "c"
letters = ["c", "f", "j"], target = "k", 输出: "c"
letters长度范围在[2, 10000]区间内。
letters 仅由小写字母组成，最少包含两个不同的字母。
目标字母target 是一个小写字母。
链接：https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/
    """
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        p1, p2 = 0, len(letters) - 1
        while p1 < p2 - 1:
            t = (p1 + p2) >> 1
            if letters[t] > target:
                p2 = t
            else:
                p1 = t
        return letters[p2]


def main():
    letters = ["c", "f", "j"]
    target = "f"
    test = Solution()
    ret = test.nextGreatestLetter(letters, target)
    print(ret)


if __name__ == '__main__':
    main()
