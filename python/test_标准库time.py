import time

# 时间戳
# print(time.time())

# 国外的时间格式
# print(time.asctime())

# 等待括号中接时间多少秒
# print(time.sleep(1))

# 将时间戳转成时间元祖
# print(time.localtime(123456))

# 将当前时间转换成带格式的时间
# 格式:time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取两天前的时间
# 获取当前时间
# now_time = time.time()
# 获取前两天的时间戳
# befor_tiem = now_time - 60*60*48
# 将两天前的时间戳转换成时间元祖
# time_tuple = time.localtime(befor_tiem)
# 将时间元祖转换成指定的时间格式
# result_time = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
# print(result_time)

# 获取两天后的时间
#获取当前时间
# now_time = time.time()
# after_time = now_time + 60*60*48
# after_time_tuple = time.localtime(after_time)
# result_time = time.strftime("%Y-%m-%d %H:%M:%S", after_time_tuple)
# print(result_time)