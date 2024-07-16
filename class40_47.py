'''
class from Bro Code
https://youtu.be/XKHEtdqhLK8?si=L-c30rp08X7KOpD9
# 40: object oriented programming 面向对象编程
# 41: class variables 类变量
# 42: inheritance 继承
# 43: multiple level inheritance 多重继承 when a drived (child) class inherits from another derived (child) class
# 44: multiple inheritance 多重继承 when a child class inherits from more then one parent classes
# 45: methed overriding 方法重写
# 46: methed chaining 方法链 calling multiple methods sequentially
# 47: super function 超级函数 = Function used to give access to methods and properties of a parent class
'''

# # class40: object oriented programming 面向对象编程

# from car import Car
# car_1 = Car("Chevy", "Camaro", 2022, "red")
# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

# car_1.driving()
# car_1.stop()

# car_2 = Car("Ford", "Mustang", 2023, "blue")
# car_2.driving()
# car_2.stop()



# # class41: class variables 类变量
# from car import Car

# car_2 = Car("Ford", "Mustang", 2023, "blue")
# car_1 = Car("Chevy", "Camaro", 2022, "red")


# print(Car.wheels) #类未声明实例也可获得变量值

# car_1.wheels = 2  # 重新赋值

# print(car_1.wheels)
# print(car_2.wheels)


# # class42: inheritance 继承
# class Animal:
#     alive = True    

#     def eat(self):
#         print("This animal is eating.")

#     def sleep(self):
#         print("This animal is sleeping.")

# # 继承 父类写在括号里
# class Rabbit(Animal):
#     def run(self):
#         print("This rabbit is running.")

# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming.")

# class Hawk(Animal):
#     def fly(self):
#         print("This hawk is flying.")

# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# rabbit.eat()
# fish.sleep()
# hawk.eat()

# rabbit.run()
# fish.swim()
# hawk.fly()


# # class43: multiple level inheritance 多重继承 when a drived (child) class inherits from another derived (child) class
# class Organism:
#     alive = True

# class Animal(Organism):
#     def eat(self):
#         print("This animal is eating.")

# class Dog(Animal):
#     def bark(self):
#         print("This dog is barking.")

# dog = Dog()
# dog.eat()
# dog.bark()
# print(dog.alive)

# # class44:  multiple inheritance 多重继承 when a child class inherits from more then one parent classes
# class Prey:
#     def flee(self):
#         print("This prey is fleeing.")

# class Predator:
#     def hunt(self):
#         print("This predator is hunting.")

# class Rabbit(Prey):
#     def eat_grass(self):
#         print("This rabbit is eating grass.")

# class Hawk(Predator):
#     def eat_meat(self):
#         print("This hawk is eating meat.")

# # 继承多个父类 直接写在括号里
# class Fish(Prey, Predator):
#     def swim(self):
#         print("This fish is swimming.")

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# rabbit.flee()
# hawk.hunt()

# fish.flee()
# fish.hunt()

# # class45: methed overriding 方法重写
# class Animal:
#     def eat(self):
#         print("This animal is eating.")

# class Rabbit(Animal):

#     # 方法重写 直接重写
#     def eat(self):
#         print("This rabbit is eating.")

#     def run(self):
#         print("This rabbit is running.")

# Rabbit = Rabbit()
# Rabbit.eat()
# Rabbit.run()


# class46: methed chaining 方法链 calling multiple methods sequentially
#                                each call performs an action on the same object and returns self

# class Car:
#     def turn_on(self):
#         print("The car is starting.")
#         return self
    
#     def drive(self):
#         print("The car is driving.")
#         return self
    
#     def turn_off(self):
#         print("The car is stopping.")
#         return self
    
#     def brake(self):
#         print("The car is braking.")
#         return self
    

# car = Car()
# car.turn_on().drive().brake().turn_off() 

# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()  # \表示换行 可读性更高

# #  class47: super function 超级函数 = Function used to give access to methods and properties of a parent class
# #                                    returns a temporary object of the superclass when used

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

    
# class Square(Rectangle):
#     def __init__(self, length, width):
#         super().__init__(length, width)

#     def area(self):
#         return self.length * self.width

# class Cube(Rectangle):
#     def __init__(self, length, width,height):
#         super().__init__(length, width)
#         self.height = height

#     def volume(self):
#         return self.length * self.width * self.height

# cube = Cube(5, 5, 5)
# print(cube.length)
# print(cube.width)
# print(cube.height)

# square = Square(5, 5)
# print(square.length)
# print(square.width)

# print("-"*22)
# print(square.area())
# print(cube.volume())
    