'''
class from Bro Code
https://youtu.be/XKHEtdqhLK8?si=L-c30rp08X7KOpD9
#15 lists 列表
#16 2D lists 二维列表
#17 tuples 元组
#18 set 集合
#19 dictionary 字典
#20 index operator [] 索引运算符
#21 functions 函数
#22 return statement 返回语句
#23 keyword arguments 关键字参数
#24 nested functions 嵌套函数
#25 scope 作用域
#26 *args parameters 传递不定数量的参数
#27 **kwargs parameters 传递不定数量的关键字参数
'''
# #class15: lists 列表 used to store multiple items in a single variable
# food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

# food[0] = "sushi" # change the first element
# # print(food[0])

# food.append("ice cream") # add an element to the end of the list 在最后添加元素
# food.remove("hotdog") # remove an element from the list 删除指定元素
# food.pop() # remove the last element from the list 删除最后一个元素
# food.insert(0, "cake") # add an element at a specific index 在指定位置添加元素
# food.sort() # sort the list in alphabetical order 按字母顺序排序
# food.clear() # remove all elements from the list 删除所有元素
# for i in food:
#     print(i)


# # class16 2D lists 二维列表 a list of lists
# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
# food = [drinks, dinner, dessert]
# # print(food)
# # print(food[0])
# # print(food[0][1]) # soda

# class17: tuples 元组 collection which is ordered and unchangeable
#                      used to group together related data

# student = ("Bro" ,21,"male")
# print(student.count("male")) # 1
# print(student.index(21)) # 1

# for x in student:
#     print(x)

# if "Bro" in student:
#     print("Bro is here")

# # class18 set 集合 collection which is unordered, unindexed. No duplicate members
# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}

# # utensils.add("napkin")
# # utensils.remove("fork")
# # utensils.clear()
# # utensils.pop()

# # utensils.update(dishes) # combine two sets 合并两个集合
# # dinner_table = utensils.union(dishes) # combine two sets 合并两个集合

# print(utensils.difference(dishes)) # utensils have but dishes don't have 

# for x in utensils:
#     print(x)

# class19: dictionary 字典 a changeable, unordered collection of unique key:value pairs
#                          Fast because they use hashing, allow us to access a value quickly

# # {Key:Value}
# capitals = {"USA":"Washington D.C.", 
#             "India":"New Delhi", 
#             "China":"Beijing",
#             "Russia":"Moscow"}

# # update 没有则添加 有则修改
# capitals.update({"Germany":"Berlin"}) # 添加新元素
# capitals.update({"USA":"Las Vegas"}) # 修改元素  

# capitals.pop("India") # 删除元素
# capitals.clear() # 删除所有元素

# print(capitals["USA"])

# print(capitals.get("Germany")) # None 使用get方法，如果没有这个key，返回None 更安全

# print(capitals.keys()) # dict_keys(['USA', 'India', 'China', 'Russia'])
# print(capitals.values()) # dict_values(['Washington D.C.', 'New Delhi', 'Beijing', 'Moscow'])
# print(capitals.items()) # dict_items([('USA', 'Washington D.C.'), ('India', 'New Delhi'), ('China', 'Beijing'), ('Russia', 'Moscow')])

# class20: index operator [] 索引运算符 gives access to a sequence's elements

# name = "bro Code"
# if (name[0].islower()):
#     name = name.capitalize()
# print(name) # Bro Code

# first_name = name[:name.index(" ")].upper()
# print(first_name) # BRO

# last_name = name[name.index(" ")+1:].lower()
# print(last_name) # code

# last_character = name[-1]
# print(last_character) # e


# # class21 functions 函数 a block of code which is executed only when it is called
# def hello(name,age): 
#     print("Hello!" + name + ", you are " + str(age) + " years old.")

# hello("Bro Code", 21) 

# # class22: return statement 返回语句
# def add(num1, num2):
#     return num1 + num2

# print(add(4,5)) # 9

# class23: keyword arguments 关键字参数 arguments preceded by an identifier when we pass them to a function
#                                      The order of the arguments doesn't matter, unlike positional arguments
#                                      Python knows the names of the arguments that our function receives


# def hello(first, middle, last):
#     print("Hello " + first + " " + middle + " " + last)

# hello(last="Code", middle="Bro", first="The") # Hello The Bro Code 

# class24 nested functions 嵌套函数 a function inside another function

# print(round(abs(float((input("Enter a number: ")))))) 

# # class25 scope 作用域 the region that a variable is recognized
# #                     a variable is only available from inside the region it is created
# #                     a global and locally scoped version of a variable can be created

# def display():
#     # name = "Bro" # local variable
#     print(name)

# name = "Code" # global variable 
# display()


# # class26: *args parameters 传递不定数量的参数 parameters that will pack all arguments into a tuple
# #                                             useful so that a function can accept a varying amount of arguments

 
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(add(1,2,3,4,5)) # 15


# def add(*stuff):
#     sum = 0
#     for i in stuff:
#         sum += i
#     return sum

# print(add(1,2,3,4,5)) # 15

# # class27 **kwargs parameters 传递不定数量的关键字参数 parameters that will pack all arguments into a dictionary
# #                                                    useful so that a function can accept a varying amount of keyword arguments

# def hello(**kwargs):
#     print("Hello" + " "+ kwargs['first'] + " "+ kwargs['last'])
#     print("hello", end=" ")
#     for key, value in kwargs.items():
#         print( value, end=" ")

# hello(title="Mr.", first="Bro", middle="Code", last="Python") # Hello Bro Code Python