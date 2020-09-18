class Solution(object):
    """
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。
可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。
能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。
输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。
    """
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed[0:0] = [0]
        flowerbed.append(0)
        count, i = 0, 1
        while i < len(flowerbed) - 1:
            if flowerbed[i + 1]:
                i += 3
            elif flowerbed[i]:
                i += 2
            elif flowerbed[i - 1]:
                i += 1
            else:
                flowerbed[i] = 1
                count += 1
                i += 2
        return count >= n


def main():
    # flowerbed, n = [0, 1, 0, 0, 0, 1, 0], 1
    # flowerbed, n = [1, 0, 0, 0, 0, 1], 2
    # flowerbed, n = [0, 0, 1, 0, 1], 1
    # flowerbed, n = [1], 0
    flowerbed, n = [1, 0, 0, 0, 1, 0, 0], 2
    test = Solution()
    ret = test.canPlaceFlowers(flowerbed, n)
    print(ret)


if __name__ == '__main__':
    main()
