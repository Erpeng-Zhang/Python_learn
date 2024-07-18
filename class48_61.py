'''
class from Bro Code
https://youtu.be/XKHEtdqhLK8?si=L-c30rp08X7KOpD9
# 48: abstract classes
# 49: object as arguments
# 50: duck typing
# 51: walrus operator :=
# 52: functions to variables
# 53: higher order functions
# 54: lambda
# 55: sort
# 56: map
# 57: filter
# 58: reduce
# 59: list comprehensions
# 60: dictionary comprehensions
# 61: zip functions
'''



# # class48: abstract classes
# '''
# Prevents a user from creating an object of that class
# compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract methods = a method that has a declartion but does not have an implementation

# 阻止用户创建该类的对象
# 强制用户在子类中重写抽象方法

# 抽象类=包含一个或多个抽象方法的类。
# 抽象方法=具有声明但没有实现的方法
# '''
# # 导入ABC和abstractmethod
# from abc import ABC, abstractmethod
# class Vehicle(ABC):

#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def go(self):
#         print("You drive a car")

#     def stop(self):
#         print("You stop a car")

# class Motorcycle(Vehicle):
#     def go(self):
#         print("You ride a motorcycle")
    
#     def stop(self):
#         print("You stop a motorcycle")

# car = Car()
# car.go()
# motorcycle = Motorcycle()
# motorcycle.go()


# # class49：object as arguments
# class Car:
#     color = None

# class Motorcycle:
#     color = None

# def change_color(vehicel, color):
#     vehicel.color = color

# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
# change_color(car_1, "red")
# change_color(car_2, "blue")
# change_color(car_3, "green")
# print("Car 1 color:", car_1.color)
# print("Car 2 color:", car_2.color)
# print("Car 3 color:", car_3.color)

# motorcycle_1 = Motorcycle()
# motorcycle_2 = Motorcycle()
# change_color(motorcycle_1, "red")
# change_color(motorcycle_2, "blue")
# print("Motorcycle 1 color:", motorcycle_1.color)
# print("Motorcycle 2 color:", motorcycle_2.color)


# # class50: duck typing = concept of an object is less important than the methods/attributes
# #                        class type is not checked if minimum method/attribute are present
# #                      if it walks like a duck and quacks like a duck, it must be a duck
# #                      一个对象的概念不如方法/属性重要；如果最少的方法/属性存在，则不检查类类型；如果它走起来像鸭子，叫起来像鸭子，那么它一定是鸭子

# class Duck:
#     def walk(self):
#         print("Duck is walking")

#     def talk(self):
#         print("Duck is quacking")

# class Chicken:
#     def walk(self):
#         print("Chicken is walking")

#     def talk(self):
#         print("Chicken is clucking")

# class Person():
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter")

# duck = Duck()
# chicken = Chicken()
# person = Person()
# person.catch(duck)
# # 即使传入不是鸭子 但是它跑他叫，它就是鸭子
# person.catch(chicken)

# # class51:walrus operator :=
# ''' 
# new to python3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression  

# 赋值表达式运算符，又名海象运算符
# 将值分配给变量作为较大表达式的一部分
# '''
# # happy = True
# # print(happy)

# print(happy := True)

# # foods = list()
# # while True:
# #     food=(input("Enter food or enter quit to leave: "))
# #     if food == "quit":
# #         break
# #     foods.append(food)
# # print(foods)

# foods = list()
# while (food := input("Enter food or enter quit to leave: ")) != "quit":
#     foods.append(food)
# print(foods)



# # class52: functions to variables
# def hello():
#     print("Hello")

# hi = hello
# print(hello)
# print(hi)
# hi()

# say = print
# say("say can work as print")


# # class53: higher order functions = functions that accept other functions as arguments or return functions as output 
# #                                   高阶函数=接受其他函数作为参数或返回函数作为输出的函数

# # accept other functions as arguments
# def loud(text):
#     return text.upper()

# def quiet(text):
#     return text.lower()

# def hello(func):
#     text = func("Hello")
#     print(text)

# hello(loud)
# hello(quiet)

# # return functions as output 
# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend

# divide = divisor(2)
# print(divide(10))

# # class54: lambda = function written in one line using lambda keyword
# #                   accepts any number of arguments but has only one expression
# #                   (think of it as a shortcut)
# #                   (useful if needed for a short period of time, throw_away)
# #                   写在一行的函数，使用lambda关键字
# #                   接受任意数量的参数，但只有一个表达式 匿名函数

# def double(x):
#     return x*2
# print(lambda x: x*2)

# multiply = lambda x, y: x*y
# print(multiply(2, 3))
# add = lambda x, y, z: x+y+z
# print(add(2, 3, 4))

# full_name = lambda first, last: first + last
# age_check = lambda age: True if age >= 18 else False


# class55: sort
'''
sort() method = used with lists
sort() function = used with iterables

sort()方法=与列表一起使用
sort()函数=与可迭代一起使用
'''

# student = ["Aquidward","Spongebob","Patrick","Sandy","Mr. Krabs"]
# # student.sort(reverse=True)
# sorted_student = sorted(student, reverse=True)
# for i in student:
#     print(i)
# print()
# for i in sorted_student:
#     print(i)

# students = [("Aquidward","B", 10),("Spongebob","A", 12),("Patrick","C", 8),("Sandy","A", 11),("Mr. Krabs","D", 9)]
# grade = lambda grades: grades[1]
# students.sort(key=grade)

# for i in students:
#     print(i)

# age = lambda ages: ages[2]
# students.sort(key=age)
# for i in students:
#     print(i)

# # sorted()
# students = (("Aquidward","B", 10),("Spongebob","A", 12),("Patrick","C", 8),("Sandy","A", 11),("Mr. Krabs","D", 9))
# age = lambda ages: ages[2]
# sorted_students = sorted(students, key=age)
# for i in sorted_students:
#     print(i)


# # class56: map() applies a function to all the items in an input_list(list tuple etc)
# # map(function,iterable)

# store = [("shirt", 20.00),("pants", 25.00),("jacket", 50.00),("socks", 10.00)]
# to_euros = lambda data: (data[0], data[1]*0.82)
# to_dollars = lambda data: (data[0], data[1]/0.82)
# store_euros = map(to_euros, store)
# store_dollars = map(to_dollars, store)
# for i in store_euros:
#     print(i)
# print("-"*33)
# for i in store_dollars:
#     print(i)

# # class57: filter = create a collection of elements from an iterable for which a function returns true
# # filter(function, iterable)

# friends = [("Rachel", 19),("Monica", 20),("Phoebe", 18),("Joey", 21),("Chandler", 22),("Ross", 23)]
# age = lambda data: data[1] >= 21

# drinking_buddies = list(filter(age, friends))
# for i in drinking_buddies:
#     print(i)

# # class58: reduce = apply a function to an iterable and reduce it to a single cumulative value
# #                   performs function on first two elements and reduce repeats process until 1 value remains
# #                   reduce(function, iterable)

# import functools
# letters = ["H","E","L","L","O"]
# word = functools.reduce(lambda x, y: x+y, letters)
# print(word)

# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x, y: x*y, factorial)
# print(result)


# # class59: list comprehensions = a way to create lists with less syntax
# #                                can mimic certain lambda functions, easier to read
# #                                list = [expression (if/else) for item in iterable]

# # # 一般方式 
# # squares = []                #声明一个空列表
# # for i in range(10):         #for循环
# #     squares.append(i**2)    #定义每次循环所需的操作
# # print(squares)

# # students = [100,98,66,54,88,90,70,44,30,20]

# # passed_students = list(filter(lambda x: x >= 60, students))

# # print(passed_students)
# students = [100,98,66,54,88,90,70,44,30,20]
# # passed_students = [x for x in students if x >= 60]
# passed_students = ["Pass" if x >= 60 else "Failed" for x in students]
# print(passed_students)



# class60: dictionary comprehensions = create dictionaries using an expression
#                                     can replace for loops and certain lambda functions
#                                     dictionary = {key: value for (key,value)) in iterable}

# # 例1
# cities_in_F = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
# cities_in_C = {key: (value-32)*5/9 for (key,value) in cities_in_F.items()}
# print(cities_in_C)

# # 例2
# weather = {"New York": "snowy", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# # 例3
# cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
# desc_cities = {key: "Warm" if value >= 70 else "Cold" for (key,value) in cities.items()}
# print(desc_cities)

# # 例4
# def check_temp(value):
#     if value >= 70:
#         return "Hot"
#     elif 69 >= value >= 40:
#         return "Warm"
#     else:
#         return "Cold"

# cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
# desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
# print(desc_cities)

# class61: zip functions = aggregate elements from two or more iterables(lists, tuples, etc)
#                          creates a zip object with paired elements stored in tuples for each element

# # 例1
# user_names = ["Tom", "Jerry", "Spike"]
# passwords = ["123", "456", "789"]

# users = list(zip(user_names, passwords))

# print(type(users))    

# for i in users:
#     print(i)

# # 例2
# usernames = ["Tom", "Jerry", "Spike"]
# passwords = ("123", "456", "789")
# login_date = ["1/1/2020", "1/2/2020", "1/3/2020"]

# users = zip(usernames, passwords, login_date)

# for i in users:
#     print(i)