class Solution(object):
    """
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，
其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
编写一个算法来重建这个队列。总人数少于1100人。
输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height/
    """
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        people.sort(key=lambda x: (-x[0], x[1]))  # 先插大的数，后面插小的数的时候不会影响第二位的值
        for x in people:
            ret.insert(x[1], x)
        return ret


def main():
    p = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    # p = []
    test = Solution()
    ret = test.reconstructQueue(p)
    print(ret)


if __name__ == '__main__':
    main()
