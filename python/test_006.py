# 列表
"""
list.append(x): 在列表的末尾添加一个元素，相当于a[len(a):] = [x]
list.inset(i,x):在给定的位置插入一个元素，第一个参数是要插入的元素的索引，以a.insert(0,x)插入列表头部，a.insert(len(a),x)等同于a.append
list.remove(x):移除列表中第一个值为x的元素，则抛出ValueError异常。
list.pop([i]):删除列表中给定位置的元素返回它，如果没有给定位置，a.pop()将会删除并返回列表中的最后一个元素
list.sort(key=None,reverse=false):对列表中的元素进行排序(参数可用于自定义排序)
list.reverse()：翻转列表中的元素
"""


# list_test = [1,3,2,9,6]
# list_test.append(3)
# list_test.insert(3,1)
# list_test.sort(reverse= True)
# list_test.reverse()
# print(list_test)

# list_results = []
# for i in range(1,5):
#     for n in range(1,5):
#         list_results.append(i*n)
#     print(list_results)

# list_results = [i*n for i in range(1,5) for n in range(1,5)]
# print(list_results)

# 列表可变，元祖不可变

# 元祖
# 元祖的不可变性
# 元祖的定义带括号与不带括号一个意思
# tuple1 = 1,2,3
# tuple2 = (4,5,6)

# print(tuple1,type(tuple1))
# print(tuple2,type(tuple1))

# 元祖的内置函数
# a = (1,2,3,"a","a")

# print(a.count("a"))     #统计元祖中有多少个字符串
# print(a.index(1))       #统计元祖中的int在第几个位置

# 集合
# a = {1,2,3}
# b = {1,4,5}

# 常用函数
# print(a.union(b))               #并集,ab重复的不展示
# print(a.intersection(b))      #取交集，展示两个集合中相同的
# print(a.difference(b))          #差集,a中有,b中没有的展示
# a.add(4)                         #集合添加

# 字典
# 添加字典
a={"测试":1,"复制":2}
b = dict(a=1,b=2)
# print(a,type(a))
# # print(b,type(b))

# print(a.keys())          #查看键
# print(a.values())        #查看值
print(a.pop("测试"))      #删除Key并展示删除的Value
print(a)
