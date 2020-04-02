class Solution(object):
    """
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
输入: [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
输入: [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
链接：https://leetcode-cn.com/problems/non-overlapping-intervals/
    """
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        p1 = count = 0
        for p2 in range(1, n):
            if intervals[p2][0] >= intervals[p1][1]:
                p1 = p2
            else:
                count += 1
        return count


def main():
    # intervals = []
    # intervals = [[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]]
    intervals = [[-3, -1], [-2, 0], [-1, 1], [0, 2], [1, 3]]
    test = Solution()
    ret = test.eraseOverlapIntervals(intervals)
    print(ret)


if __name__ == '__main__':
    main()
