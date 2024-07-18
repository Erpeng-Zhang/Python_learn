'''
class from Bro Code
https://youtu.be/XKHEtdqhLK8?si=L-c30rp08X7KOpD9
# 62 if name = '__main__'
'''

# # class62: if name = '__main__'
# def main():
#     print("Hello!")

# if __name__ == '__main__':
#     # print(__name__ )
#     main()



# class63 time module 时间模块
import time

# # time.ctime() 
# print(time.ctime(0)) # Thu Jan  1 08:00:00 1970

# print(time.ctime(10000000)) # 1619780000.0

# # time
# print(time.time()) # 1619780000.0

# print(time.ctime(time.time())) # 当前时间

# # time_object = time.localtime()
# time_object = time.gmtime() # UTC 时间
# print(time_object)

# print(time.strftime("%Y-%m-%d %H:%M:%S", time_object)) # 

# #字符串转时间
# time_str = "2024 july 18"
# time_object = time.strptime(time_str, "%Y %B %d")
# print(time_object)

# # 时间元组(year month day hour minute second weekday yearday isdst)
# time_tuple = (2024, 7, 18, 21, 10, 0, 0, 0, 0)
# # asctime 时间元组转化为时间
# time_string = time.asctime(time_tuple)
# # mktime 时间转化为时间戳
# time_string = time.mktime(time_tuple)
# print(time_string)


 
# class64: threading 多线程
import threading

# print(threading.active_count()) # 1
# print(threading.enumerate()) # 

def breakfast():
    time.sleep(3)
    print("Eat breakfast")

def study():
    time.sleep(4)
    print("Study")

def drink_coffee():
    time.sleep(2)
    print("Drink coffee")


x = threading.Thread(target=breakfast, name="breakfast")
x.start()

y = threading.Thread(target=drink_coffee, name="drink_coffee")
y.start()

z = threading.Thread(target=study, name="study")
z.start()

x.join()
y.join()
z.join()

print(threading.active_count()) # 4
print(threading.enumerate()) #
print(time.perf_counter())










# class65: daemon threads 守护线程

# multiprocessing  多进程