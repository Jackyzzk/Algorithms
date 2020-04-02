class Trie(object):
    """
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
示例:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sons = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        tree = self.sons
        for x in word:
            if x not in tree:
                tree[x] = {}
            tree = tree[x]
        tree['end'] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tree = self.sons
        for x in word:
            if x not in tree:
                return False
            tree = tree[x]
        if 'end' in tree:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tree = self.sons
        for x in prefix:
            if x not in tree:
                return False
            tree = tree[x]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# ["Trie","insert","search","search","startsWith","insert","search"]
# [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]

# ["Trie","insert","search","startsWith"]
# [[],["a"],["a"],["a"]]
# [null,null,true,true]

def main():
    test = Trie()
    test.insert('apple')
    print(test.search('apple'))
    print(test.search('app'))
    print(test.startsWith('app'))
    test.insert('app')
    print(test.search('app'))

    # test.insert('a')
    # print(test.search('a'))
    # print(test.startsWith('a'))


if __name__ == '__main__':
    main()
