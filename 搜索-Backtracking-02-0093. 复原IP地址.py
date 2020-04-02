class Solution(object):
    """
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
链接：https://leetcode-cn.com/problems/restore-ip-addresses/
    """
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(pre, rest, k):  # k 记录可以添加小数点的个数
            if k <= len(rest) <= 3 * k:
                if k == 0:
                    ret.append(pre[:-1])
                    return

                for i in range(1, 4):
                    if int(rest[:i]) < 256 and len(rest[:i]) == i and (rest[0] != '0' or i == 1):
                        dfs(pre + rest[:i] + '.', rest[i:], k - 1)

        ret = []
        dfs('', s, 4)
        return ret


def main():
    s = "25525511135"
    s = "0000"
    # s = "010010"  # ["0.10.0.10","0.100.1.0"]
    s = "172162541"  # ["17.216.25.41","17.216.254.1","172.16.25.41","172.16.254.1","172.162.5.41","172.162.54.1"]
    test = Solution()
    ret = test.restoreIpAddresses(s)
    print(ret)


if __name__ == '__main__':
    main()
