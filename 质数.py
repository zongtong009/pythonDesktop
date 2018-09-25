import time
import math


num = 1
snum = 0
ints = eval(input())  # 输入数
start = time.perf_counter()
while num <= ints:

    num += 1  # num表示从1到ints,进行遍历

    # 判断语句
    div_num = 2  # 重置div_num
    while div_num <= math.sqrt(num):
        if num % div_num == 0:
            break  # 停止判断
        div_num += 1
    # 判断为质数后的操作
    else:
        snum += 1  # 质数的总数

        print("%d" % (num))
dur = time.perf_counter()-start
print("质数的总数为：", snum, "，用时为", dur*1000, "ms")
# math.sqtr(ints)
# for i in range(ints):
