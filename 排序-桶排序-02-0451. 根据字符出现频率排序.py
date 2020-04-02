class Solution(object):
    """
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
输入: "tree"
输出: "eert"
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
输入: "cccaaa"
输出: "cccaaa"
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
输入: "Aabb"
输出: "bbAa"
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
链接：https://leetcode-cn.com/problems/sort-characters-by-frequency/
    """
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        count, ret = {}, []
        for x in s:
            count[x] = count.get(x, 0) + 1
        m = max(count.values())
        bucket = [[] for i in range(m + 1)]
        for key, val in count.items():
            bucket[val].append(val * key)
        for i in range(m, 0, -1):
            ret.extend(list(bucket[i]))
        return ''.join(ret)


def main():
    s = "aaaccc"
    test = Solution()
    ret = test.frequencySort(s)
    print(ret)


if __name__ == '__main__':
    main()
