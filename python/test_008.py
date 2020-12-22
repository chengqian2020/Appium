import json

# 字面量


# 文件读取
"""
第一步：打开文件、获取文件描述符
第二部：操作文件描述符(读|写)
第三步：关闭文件
"""

# f = open('datas/case','rt')
# # print(f.read())
# print(f.readline())

# print(f.readlines())
# f.close()


# with open('datas/case','rt') as f:
#     print(f.readlines())

info = '''
[{
    "chengqian": "fingo",
    "xuzilu": "beida",
    "xiongjingyi": "wahaha"
},
    {
        "chengqian": "fengou",
        "xuzilu": "alibba",
        "xiongjingyi": "wangyi"}]
'''

# 把数据类型转换成字符串
# data = json.dumps(info,sort_keys=True,indent=4)     #sort_keys代表按Key的顺序输出，indent缩进的方式输出
# print(data)
# print(type(data))

# 把数据类型转换成字符串并存储在文件中
# print("读取Json文件")
# json.dump(info, open('datas/json_dump.json', "w"))      #保存Json到json_dump.json文件中

# loads: 将 字符串 转换成 json
# print(type(info))
# data = json.loads(info)
# print(type(data))
# print(data)

#load把文件打开从字符串转换成json
# jsobj = json.load(open('datas/json_dump.json', 'r'))
# print(jsobj)
# print(type(jsobj))
# print(jsobj[0]["chengqian"])
