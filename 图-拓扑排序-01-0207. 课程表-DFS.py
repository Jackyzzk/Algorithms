class Solution(object):
    """
现在你总共有 n 门课需要选，记为 0 到 n-1。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，
你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？
输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；
并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序，拓扑排序也可以通过 BFS 完成。
链接：https://leetcode-cn.com/problems/course-schedule
    """
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = [[] for i in range(numCourses)]
        visit = [0] * numCourses  # 0：未访问  1：正在访问  2：已经访问
        for x, t in prerequisites:
            adj[t].append(x)

        def judge(num):
            if visit[num] == 0:
                visit[num] = 1
                for x in adj[num]:
                    if not judge(x):
                        return False
                visit[num] = 2
                return True
            if visit[num] == 1:
                return False
            if visit[num] == 2:
                return True

        for i in range(numCourses):
            if not judge(i):
                return False
        return True


def main():
    # num, prerequisites = 2, [[1, 0], [0, 1]]
    # num, prerequisites = 2, [[1, 0]]
    num, prerequisites = 2, []  # true
    test = Solution()
    ret = test.canFinish(num, prerequisites)
    print(ret)


if __name__ == '__main__':
    main()
