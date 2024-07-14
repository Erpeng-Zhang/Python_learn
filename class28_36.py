'''
class from Bro Code
https://youtu.be/XKHEtdqhLK8?si=L-c30rp08X7KOpD9
#28 

'''


# class28: str .format()  optional method that gives users 
#                         more control when displaying output 

# #{}占位
# animal = "cow"
# item = "moon"
# num = 3.14159

# print("The " + animal + " jumped over the " + item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {} jumped over the {}".format("cow", "moon")) # 可以重复使用
# print("The {0} jumped over the {0}".format(animal, item)) # index
# print("The {1} jumped over the {0}".format(item, animal)) # positional arguments
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) # keyword arguments

# text = "The {} jumped over the {}"
# print(text.format(animal, item))

# #占位
# name = "Bro"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}".format(name)) # 10 spaces 占位（默认左对齐）
# print("Hello, my name is {:>10}".format(name)) # right aligned 右对齐
# print("Hello, my name is {:<10}".format(name)) # left aligned 左对齐
# print("Hello, my name is {:^10}".format(name)) # center aligned 居中
# print("Hello, my name is {:_^10}".format(name)) # center aligned with underscores 居中，且空位用下划线填充

# # 数字
# number = 3.14159
# print("The number is {:.2f}".format(number)) # 2 decimal places 保留两位小数 .2f
# print("The number is {:.3f}".format(number)) # 3 decimal places 保留三位小数 .3f
# number = 1000
# print("The number is {:,}".format(number)) # comma separator 逗号分隔
# print("The number is {:b}".format(number)) # binary 二进制
# print("The number is {:o}".format(number)) # octal 八进制
# print("The number is {:x}".format(number)) # hexadecimal 十六进制
# print("The number is {:e}".format(number)) # scientific 科学计数法
# print("The number is {:E}".format(number)) # scientific 科学计数法


# # class29: random module 随机模块
# import random

# x = random.randint(1, 6) # 随机生成数字
# y = random.random() # 随机生成数字

# myList = ["rock", "paper", "scissors"]
# z = random.choice(myList) # 随机选择列表中的元素

# cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
# random.shuffle(cards) # 随机打乱列表中的元素

# print(x)
# print(y)
# print(z)

# # class30: exceptions handling 异常 events detected during execution that interrupt the normal flow of a program

# try:
#     numerator = int(input("Enter a number to divide: ")) # 除数
#     demoninator = int(input("Enter a number to divide by: "))  # 被除数 
#     result = numerator / demoninator
    
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("Enter only numbers, plz!")
# except Exception as e:
#     print("some thing went wrong:(")
#     print(e)
# else:
#     print(result)
# finally:
#     print("This will always execute.") # 无论如何都会执行

# #  class31: file detection 文件检测
# import os

# path = "D:\\test.txt"

# if os.path.exists(path):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("That location is a file!")
#     elif os.path.isdir(path):
#         print("That location is a directory!")
# else:
#     print("That location doesn't exist!")

# # class32: read a file 读取文件
# try:
#     with open("D:\\test.txt", "r") as file:
#         content = file.read()
#         print(content)
#     print(file.closed) # True——open() 会自动关闭文件
# except FileNotFoundError:
#     print("That file was not found.")
# except PermissionError:
#     print("You don't have permission to read that file.")
# except Exception as e:
#     print("Some unexpected error occurred.")
#     print(e)



# # class33: write to a file 写入文件
# try:
#     with open("test.txt", "w") as file:
#         file.write("I am writing to this file.")
# except FileNotFoundError:
#     print("That file was not found.")
# except PermissionError:
#     print("You don't have permission to write to that file.")
# except Exception as e:
#     print("Some unexpected error occurred.")
#     print(e)

# # class34: copy a file 复制文件
# import shutil 
# # shell utilities module 
# #  copyfile() #src, dst 都需是文件名, 如果dst 存在或无权限，会抛出异常
# #  copy() #dst 可以是目录名。
# #  copy2() 如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；
# #          如果是不在相同的文件系统的话就是做move操作，shutil.copytree
# #          ( olddir, newdir, True/Flase)，把olddir拷贝一份newdir，如
# #          果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果
# #          第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接，
# # shutil.rmtree( src ) 递归删除一个目录以及目录内的所有内容


# shutil.copyfile("test.txt", "copy.txt")# 复制文件
# shutil.copy("test.txt", "copy.txt") # 复制文件
# shutil.copy2("test.txt", "copy.txt") 


# # class35: move a file 移动文件
# import os

# source = "test.txt"
# destination = "D:\\test.txt"

# try:
#     if os.path.exists(destination):
#         print("There is already a file there.")
#     else:
#         os.replace(source, destination)
#         print(source + " was moved.")
# except FileNotFoundError:
#     print("That file was not found.")
# except PermissionError:
#     print("You don't have permission to move that file.")
# except Exception as e:
#     print("Something went wrong.")
#     print(e)



# class36: delete a file 删除文件
# import os

# psths = ["D:\\test.txt", "test.txt", "copy.txt"]

# for p in psths:
#     try:
#         os.remove(p)
#         print(p + " was deleted.")
#     except FileNotFoundError:
#         print(p + " was not found.")
#     except PermissionError:
#         print("You don't have permission to delete that file.")
#     except Exception as e:
#         print("Something went wrong.")
#         print(e)

# # shutil.rmtree() # 删除目录及目录下的所有文件
# import shutil
# path = "test"

# try:
#     shutil.rmtree(path)
# except FileNotFoundError:
#     print("That file was not found.")
# except PermissionError:
#     print("You don't have permission to delete that file.")
# except Exception as e:
#     print("Something went wrong.")
#     print(e)