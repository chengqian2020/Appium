# 函数的参数

# 必须参数
# 必须参数的含义就是，如果在函数内有参数，且我们在调用的过程中，没有给参数进行传参，则会报错
# 示例
# def test(a):
#     print(a)
#
# test()    #不填值则会报错


# 默认参数
# 1.调用函数时，如果没有传递参数，则会使用默认参数
# 2.默认参数在定义函数的时候定义
# 3.默认值只会执行一次，这条规则在默认值可变对象时很重要
# def test1(a, b=[]):
#     b.append(a)
#     return b
#
# print(test1(10))
# print(test1(11))


# # 字典传参
# def test2(**a):
#     print(a.keys())
#
# test2(a=1,b=2,c=3)

# 元祖传参
# def test3(*a):
#     print(a[0])
#     print(a[1])
#     print(a[2])
#
# test3(1,2,3)

# 特殊传参 仅限关键字传参
# def test4(*,a):
#     print(a)

# test4(a=1)  #必须指定关键字参数

# 解包传参字典
# def test5(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#
# dict_test = {"a":"1","b":"2","c":"3"}
#
# test5(**dict_test)
# 解包传参元祖
# def test6(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#
# yuanzu = (1,2,3)
#
# test6(*yuanzu)


