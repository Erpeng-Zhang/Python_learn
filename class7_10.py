'''
class from Bro Code
https://youtu.be/XKHEtdqhLK8?si=L-c30rp08X7KOpD9
#7：math functions 数学函数
#8: string slice 字符串切片 
#9: if statements 条件语句
#10: logical operators(and,or,not) 逻辑运算符
#11: while loops 循环
#12: for loops 循环
#13: nested loops 嵌套循环
#14: loop control statements 循环控制语句
'''
# # class7: math functions 数学函数
# import math

# pi = 3.14
# x,y,z = 1,2,3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(-pi))
# print(pow(pi, 2)) #乘方运算
# print(math.sqrt(420)) #开方运算
# print(max(x,y,z))


# class8: string slice 字符串切片 create a substring by extracting elements from another string
    # indexing[] or slice()   下标或切片函数
    # [start:stop:step]
# # 下标法
# name = "Bro Code"
# first_name = name[0:3]   
# first_name = name[:3]    # same as above 
# print(first_name)

# last_name = name[4:8]
# last_name = name[4:]     # same as above
# print(last_name)

# funky_name = name[0:8:2] # step by 2  步长放最后
# funky_name = name[::2]   # same as above
# print(funky_name)

# reversed_name = name[::-1] # reverse the string 步长-1可以实现倒置
# print(reversed_name)

# # slice()方法
# website1 = "http://google.com"
# website2 = "http://wikipedia.com"

# slice = slice(7, -4)  #(开始，结束) 前包后不包
# print(website1[slice]) # google
# print(website2[slice]) # wikipedia

# # class9: if statements 条件语句 a block of code that will only run if its condition is true
# age = int(input("Enter your age: "))

# if age == 100:
#     print("You are a century old")
# elif age >= 18:
#     print("You are an adult")
# elif age < 0:
#     print("You haven't been born yet")
# else:
#     print("You are a child")

# class10 logical operators(and,or,not) = used to check if two or more conditional statements are true

# temp = float(input("Enter the temperature: "))

# if temp >= 0 and temp <= 30:
#     print("The temperature is good today!")
#     print("Go outside!")
# elif temp < 0 or temp > 30:
#     print("The temperature is bad today!")
#     print("Stay inside!")


# if not(temp >= 0 and temp <= 30):
#     print("The temperature is bad today!")
#     print("Stay inside!")
# elif not(temp < 0 or temp > 30):
#     print("The temperature is good today!")
#     print("Go outside!")

# class11: while loops 循环 = a statement that will execute its block of code 
#                             as long as its condition is true
# name = ""
# while len(name) == 0:
#     name = input("Enter your name: ")
# print("Hello " + name + "!")

# class12: for loops 循环 = a statement that will execute its block of code 
#                           a limited amount of times
#                           while loop = unlimited
#                           for loop = limited
# import time
# for i in range(10):
#     print(i)


# for i in range(50,100,2):
#     print(i)


# for i in "Bro Code":
#     print(i)

# for i in range(10,0,-1):
#     print(i)
#     time.sleep(1) #暂停1秒
# print("Happy New Year!")

# # class13: nested loops 嵌套循环 = a loop inside another loop
# rows = int(input("How many rows: "))
# columns = int(input("How many columns: "))
# symbol = input("Enter a symbol to use: ")
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print() # 换行

# class14 loop control statements 循环控制语句
#  break        used to terminate the loop entirely 跳出循环
#  continue     skip to the next iteration of the loof 跳过当前循环
#  pass         does nothing, act as a placeholder 什么都不做，作为占位符

# while True:
#    name = input("Enter your name: ")
#    if name != "":
#        break

# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue
#         print(i, end="")
#     print(i, end="")
    

# for i in range(1,21):
#     if i == 13:
#         pass
#         print(i)
#     else:
#         print(i)
        