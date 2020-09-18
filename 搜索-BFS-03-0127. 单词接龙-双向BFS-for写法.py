class Solution(object):
    """
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的
最短转换序列的长度。转换需遵循如下规则：
每次转换只能改变一个字母。转换过程中的中间单词必须是字典中的单词。
如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。所有单词只由小写字母组成。字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出: 5
解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
输出: 0
解释: endWord "cog" 不在字典中，所以无法进行转换。
链接：https://leetcode-cn.com/problems/word-ladder
    """
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Python中的字符串是不可变类型
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        wordList.remove(endWord)
        que, que2 = {beginWord}, {endWord}
        n, count = len(beginWord), 1

        while que:
            aux = set()
            count += 1
            for x in que:
                for i in range(n):
                    words = {x[:i] + chr(j) + x[i + 1:] for j in range(97, 123)}
                    if words & que2:
                        return count
                    aux |= words & wordList
                    wordList -= words
            que = aux
            if len(que) > len(que2):
                que, que2 = que2, que
        return 0


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log"]
    test = Solution()
    ret = test.ladderLength(beginWord, endWord, wordList)
    print(ret)


if __name__ == '__main__':
    main()
