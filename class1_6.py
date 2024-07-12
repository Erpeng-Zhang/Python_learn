'''
class from Bro Code
https://youtu.be/XKHEtdqhLK8?si=L-c30rp08X7KOpD9
#1:环境安装与第一个程序
#2: variables 变量 : str, int, float, bool
#3: multiple assignment 多重赋值 allow us to assign multiple variables at the same time in one line of code
#4: string methods 字符串方法
#5：type casting 类型转换 = convert the data type of a value into another data type
#6: user input 输入
'''

# # class1:环境安装与第一个程序
# print("I love pozza")
# print("It's really good!")


# # class2: variables 变量
# # str
# name = "Bro"
# first_name = "Bro"
# Laat_name = "Code"
# full_name = first_name + " " + Laat_name
# print(type(name))
# print("Hello "+ name)

# # int
# age = 24
# print(age+1)
# print(type(age))

# age = 24
# age += 1
# # print("Your age is "+ age) # error
# print("Your age is "+ str(age))
# print(type(age))

# # # float
# height = 250.5
# print(height)
# print("You height is: " + str(height) + "cm")
# print(type(height))

# # bool
# human = False
# print("Are you a human:" + str(human))
# print(type(human))

# class3: multiple assignment 多重赋值
# name = "Bro"
# age = 24
# attractive = True
# print(name)
# print(age)
# print(attractive)

# name, age, attractive = "Bro", 24, True
# print(name)
# print(age)
# print(attractive)

# Spongebob, Patrick, Sandy, Squidward = "Spongebob", "Patrick", "Sandy", "Squidward"
# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)

# # 多变量赋相同值
# Spongebob = Patrick = Sandy = Squidward = 30
# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)


# # class4: string methods 字符串方法
# name = "Bro Code"
# print(len(name))
# print(name.find("o")) #找到第一个o的位置
# print(name.capitalize()) #首字母大写
# print(name.upper()) #全部大写
# print(name.lower()) #全部小写
# # name = "111"
# print(name.isdigit()) #是否为数字
# print(name.isalpha()) #是否为字母
# print(name.count("o")) #o的个数
# print(name.replace("o", "a")) #替换
# print(name*3) #重复三次

# # class5 type casting 类型转换
# x = 1 # int
# y = 2.0 # float
# z = "3" # str

# y = int(y)


# print(x)
# print(y)
# # print(z*3) # 字符串乘法——重复三次
# z = int(z)
# print(z*3)

# x = 1 # int
# y = 2.0 # float
# z = "3" # str
# # 转换为字符串才能再相加
# print("X is " + str(x))
# print("Y is " + str(y))
# print("Z is " + z)


# class6: user input 输入
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))# 输入浮点数
age = age + 1
print("Hello " + name + "! You are " + str(age) + " years old and " + str(height) + "cm tall.")




