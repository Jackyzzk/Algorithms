class Solution(object):
    """
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。
由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。
开始坐标总是小于结束坐标。平面内最多存在104个气球。
一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，
若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，
则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。
我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。
输入:  [[10,16], [2,8], [1,6], [7,12]]
输出: 2
对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。
链接：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/
    """
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        p1, count, n = 0, 1, len(points)
        for p2 in range(1, n):
            if points[p2][0] > points[p1][1]:
                count += 1
                p1 = p2
        return count


def main():
    p = [[10, 16], [2, 8], [1, 6], [7, 12]]  # 2
    # p = [[1, 2], [3, 4], [5, 6], [7, 8]]  # 4
    # p = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]  # 2
    # p = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]  # 2
    test = Solution()
    ret = test.findMinArrowShots(p)
    print(ret)


if __name__ == '__main__':
    main()
