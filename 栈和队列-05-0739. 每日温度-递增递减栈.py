class Solution(object):
    """
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。
如果之后都不会升高，请在该位置用 0 来代替。
例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
链接：https://leetcode-cn.com/problems/daily-temperatures
    """
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        ret, que = [0] * n, []
        for i in range(n):
            while que and T[i] > T[que[-1]]:
                ret[que.pop()] = i - que[-1]
            else:
                que.append(i)
        return ret


def main():
    t = [73, 74, 75, 71, 69, 72, 76, 73]
    # t = [89,62,70,58,47,47,46,76,100,70]  # [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
    test = Solution()
    ret = test.dailyTemperatures(t)
    print(ret)


if __name__ == '__main__':
    main()
