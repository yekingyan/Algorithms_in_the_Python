#!python3
# 二分查找算法, binary search, half-interval search
# 时间复杂度O(log n)，空间复杂度O(1)


def log(*args, **kwargs):
    print("log", *args, **kwargs)


def createArray(num):
    """
    生成下限为0，上限为num的升序列表，间隔为1
    :param num:数字
    :return:数组（升序列表）
    """
    # 判断是否是数字
    if type(num) == int:
        array = []
        for i in range(num+1):
            # i = i * 2  # 注释此行，间隔由2变1
            array += [i]

        # log(array)
        return array
    else:
        log("请输入数字")
        return "请输入数字"


def binarySearch(match, lists):
    """
    用二分法查找path在lists中的具体位置
    :param lists: 列表，元组
    :param match: 要查找的数字
    :return: 具体位置i（lists[i]）或None
    """
    high = len(lists) - 1
    low = 0
    # times = 0 # 计次数

    # 当条件成立证明该值不存在
    while low <= high:
        # 列表入参要整型
        mid = int((high + low) / 2)
        if lists[mid] > match:
            high = mid - 1
        elif lists[mid] < match:
            low = mid + 1
        else:
            # log("mid:{}, times:{}".format(mid, times))
            return mid
        # times += 1


def binarySearch2(match, lists):
    """
    用递归的方法实现二分查找算法
    :param match:要查找的数字
    :param lists: 列表，元组
    :return: 布尔值
    """
    n = len(lists)
    if 0 == n:
        return False
    mid = int(n / 2)
    if lists[mid] == match:
        return True
    elif lists[mid] < match:
        # 由于用了切片的方法，因此不能确定mid的值
        return binarySearch2(match, lists[mid:])
    else:
        return binarySearch2(match, lists[:mid])


# 单元测试
def test_binarySearch():
    """
    测试二分查找1
    """
    lists = createArray(100)
    # 把数组的元素提出来与函数计算值作一一校对
    for l in lists:
        mid = binarySearch(l, lists)
        tup = (l, lists[mid])
        # log(tup)
        assert l == lists[mid], "wrong mid:{}".format(mid)



# 单元测试
def test_binarySearch2():
    """
    测试二分查找2
    """
    lists = createArray(100)
    # 把数组的元素提出来与函数计算值作一一校对
    for l in lists:
        tup = (l, binarySearch2(l, lists))
        # log(tup)
        assert tup[1] == True, "wrong match{}".format(tup)



if __name__ == '__main__':
    test_binarySearch()
    log("----------------------------")
    test_binarySearch2()




