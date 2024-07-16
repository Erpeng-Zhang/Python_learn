class Car:
 
    # class variables 类变量
    wheels = 4

    # constructor 构造函数
    def __init__(self, make, model, year, color):
        self.make = make         # instance variables 实例变量
        self.model = model       # instance variables 实例变量
        self.year = year         # instance variables 实例变量
        self.color = color       # instance variables 实例变量


    def driving(self):  #调用时self不用传入参数
        print("The {} is driving.".format(self.model))

    def stop(self):
        print("The {} is stopped.".format(self.model))