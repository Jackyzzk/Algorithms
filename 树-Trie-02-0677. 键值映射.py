class MapSum(object):
    """
实现一个 MapSum 类里的两个方法，insert 和 sum。
对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。
如果键已经存在，那么原来的键值对将被替代成新的键值对。
对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。
输入: insert("apple", 3), 输出: Null
输入: sum("ap"), 输出: 3
输入: insert("app", 2), 输出: Null
输入: sum("ap"), 输出: 5
链接：https://leetcode-cn.com/problems/map-sum-pairs
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sons = {}
        self.ret = 0

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        tree = self.sons
        for x in key:
            if x not in tree:
                tree[x] = {}
            tree = tree[x]
        tree['end'] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        tree = self.sons
        self.ret = 0
        for x in prefix:
            if x not in tree:
                return 0
            tree = tree[x]

        def dfs(rest):
            for t in rest:
                if t == 'end':
                    self.ret += rest['end']
                else:
                    dfs(rest[t])

        dfs(tree)
        return self.ret


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple",3], ["ap"], ["app",2], ["ap"]]

def main():
    test = MapSum()
    test.insert('apple', 3)
    print(test.sum('ap'))
    test.insert('app', 2)
    print(test.sum('ap'))


if __name__ == '__main__':
    main()
