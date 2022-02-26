# def  sum():
#     sp = [1,2,3,4,5]
#     sum = 0
#     for i in sp:
#         sum += i
#     print(sum)
#
# sum()
# def add(a,b):
#     return a+b
# print(add(a=2,b=3))
# total = add(b = 4, a = 5)
# print(total)
# def keyword_function(a=1,b=2):
#     return a + b
# print(keyword_function(b=4,a=5))
# print(keyword_function())
# def mixed_function (a,b=2,c=3):
#     return a+b+c
# mixed_function(b=4,c=5)
# print(mixed_function(1, b=4, c=5))
# print(mixed_function(1))
# def manu(*args,**kwargs):
#     print(args)
#     print(kwargs)
# many(1,2,3,name="Mike",job="programmer")
# def function_a():
#     global a
#     a = 1
#     b =2
#     return a+b
# def function_b()
#     c=3
#     return a+c
# print(function_a())
# print(function_b())
# def func1(a,b):
#     def inner_func(x):
#         return x*x*x
#     return inner_func(a)+inner_func(b)
# print(func1(4,5))
# def sum(a,b):return a+b
# print(sum(1,5))
# def is_year_leap(year):
#     if year % 4 == 0 and year %100 == 0 and year % 400 != 0:
#         return True
#     else:
#         return False
#
# print(is_year_leap(1600))
# import math
# def square(a):
#     p = 4*a
#     s= a**2
#     d = a*math.sqrt(2)
#     return p,s,d
# print(square(int(input("Введите сторону квадрата: "))))
# def season(month):
#     if month ==12 or month >=1 and month<=2:
#         return "winter"
#     if month >=3 and month <=5:
#         return "spring"
#     if month >=6 and month <=8:
#         return "summer"
#     if month >= 9 and month <= 11:
#         return "autumn"
# print(season(int(input("Введите месяц: "))))
# def digits(n):
#     i = 0
#     while n>0:
#         n = n//10
#         i += 1
#     return i
# num = int(input('Введите число: '))
# print('Количество разрядов: ',digits(num))







# class Car:
#     default_color = 'Grey'
#     default_weight = 5000
#
#     def __init__(self,color,type,year):
#         self.color = color
#         self.type = type
#         self.year = type
#
#     def turn_on(self):
#         pass
#
#     def info(self):
#         print(self.color,self.model)
# car_obj_1 = Car('blue','BMW')
# car_obj_2 = Car('red','BMW2')
# car_obj_1.turn_on()
# print(car_obj_1.color)
# print(car_obj_2.model)
# car_obj_1.info()
# car_obj_2.info()
