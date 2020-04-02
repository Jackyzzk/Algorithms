class Solution(object):
    """
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，
并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。
如果不存在这样的两个单词，返回 0。
输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "xtfn"。
输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。
输入: ["a","aa","aaa","aaaa"]
输出: 0
解释: 不存在这样的两个单词。
链接：https://leetcode-cn.com/problems/maximum-product-of-word-lengths
    """
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        rec, ret = {}, 0
        for t in words:
            aux = 0
            for x in t:
                aux |= 1 << ord(x) - 97  # ord('a') ，用二进制来标记出现了什么字母
            for x in rec:
                if not aux & x:  # 两个数的二进制相与为0的话表示没有公共的元素
                    ret = max(ret, len(t) * rec[x])
            if len(t) > rec.get(aux, 0):
                rec[aux] = len(t)
        return ret


def main():
    # words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    # words = ["a","ab","abc","d","cd","bcd","abcd"]
    words = ["a","aa","aaa","aaaa"]
    test = Solution()
    ret = test.maxProduct(words)
    print(ret)


if __name__ == '__main__':
    main()
