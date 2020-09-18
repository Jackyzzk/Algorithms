class Solution(object):
    """
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
拆分时可以重复使用字典中的单词。你可以假设字典中没有重复的单词。
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
链接：https://leetcode-cn.com/problems/word-break
    """
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n, words = len(s), set(wordDict)
        opt = [0] * (n + 1)
        opt[0] = 1
        for p2 in range(1, n + 1):
            for p1 in range(p2 - 1, -1, -1):
                if opt[p1] and s[p1:p2:] in words:
                    opt[p2] = 1
                    break
        return opt[-1] == 1


def main():
    # s, wordDict = "leetcode", ["leet", "code"]
    # s, wordDict = "applepenapple", ["apple", "pen"]
    # s, wordDict = "catsandog", ["cats", "dog", "sand", "and", "cat"]
    s, wordDict = 'leetcode', ['leet', 'lee', 'tcode']
    test = Solution()
    ret = test.wordBreak(s, wordDict)
    print(ret)


if __name__ == '__main__':
    main()
