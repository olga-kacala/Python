
# x='1'
# y=2
# z=10.5

# x=float(x)
# y=float(y)
# suma=x+y+z

# a='eleven: '
# b= 11

# one = uno = jeden = '1'

# print(x)
# print(y)
# print(z)
# print(str(suma))
# print(a + str(b))
# print(one, uno, jeden)

# x='1'
# y=2
# z=10.5

# x=float(x)
# y=float(y)
# suma=x+y+z

# a='eleven: '
# b= 11

# one = uno = jeden = '1'

# print(x)
# print(y)
# print(z)
# print(str(suma))
# print(a + str(b))
# print(one, uno, jeden)


# web = 'http://google.com'
# web2 = 'http://wikipedia.com'

# slice = slice(7,-4)

# print(web[slice])
# print(web2[slice])

# print(web[:7])

# age = int(input('How old are you?'))

# if age == 100: 
#     print("You are 100")
# elif age >=18:
#     print("You are adult")
# elif age <0:
#     print("You are minus ")
# else:
#     print("You are baby")

# rows=int(input('how many rows?'))
# columns=int(input('how many columns?'))
# symbol=input('symbol:')

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# temp=int(input("What is the temp today?"))  

# if temp >=0 and temp <=30:
#     print("Go outside!")
# elif temp <0:
#     print("It is too cold")
# else: print("It is too hot")

# name = None
# while not name:
#     name = input("Enter your name")
# print("Hello " + name)

# import time
# for i in range(10,0,-1):
#     print(i)
#     time.sleep(2)
# print("Happy new year!")

# rows = int(input("Enter rows: "))
# columns = int(input("Enter columns: "))
# symbol= input("Enter symbol: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# while True:
#     name = input("Enter your name: ")
#     if name !="":
#         break
# print("hello " + name)

# tel = '123-456-789'

# for i in tel:
#     if i =='-':
#         continue
#     print(i, end="")

# drinks = ['coffe', 'tea']
# meals = ['pizza', 'hotdog']
# cars= ['md', 'wv']

# hobby = [drinks, meals, cars]

# print(hobby[2][1])

# student = ("Olga", 35, "femle")
# # print(student.count('Olga'))
# # print(student.index('Olga'))
# for i in student:
#     if i =="Olga":
#         print("Hello Oldzia!")

# zastawa = {'nóz', 'widelec'}
# kuchnia = {'blat', 'widelec'}

# print(zastawa.intersection(kuchnia))


# capitals = {
#     'Poland' : 'Warszawa',
#     'Germany' : 'Berlin'
# }

# # print(capitals.get('Poland'))

# for key,values in capitals.items():
#     print(values)

# name = "olga Ka!"

# if (name[0].islower):
#     name = name.capitalize()

# first = name[:4].upper()
# second = name[-3:-1].upper()
# last = name[-1]

# print(name)
# print(first)
# print(second)
# print(last)

# def hello(name,age):
#     print("Hello " + name + ". You are " + str(age) + " years old ;(")
# my_name = 'Olga'
# my_age = 35
# hello(my_name, my_age)

# def multiply (num1, num2):
#     result = num1 * num2
#     return result
# print(multiply(2,3))

# num=input("Enter number: ")
# print(abs(round(float(num))))

# name = "Ola"
# def names():
#     name="Olga"
#     print(name)
# names()
# print(name)


# def summary(*args):
#     sum = 0
#     args = list(args)
#     args[0]=100
#     for i in args:
#         sum += i
#     return sum
# print(summary(1,2,3,))

# Dane są zmienne a i b przechowujące liczby całkowite. Napisz kod, który wypisze informację, która z tych liczb jest większa.

# a = 7
# b = 4
# maxNum = max(a,b)
# print(maxNum)

# c = 5
# d = 5

# if c > d:
#     print(c)
# elif d > c:
#     print(d)
# else:
#     print(c , 'equals', d)

# import random

# a=5
# b=100
# random_num= random.randint(a,b)
# print(random_num) 

# waga = float(input('Podaj wagę w kg: '))
# wzrost= float(input('Podaj wzrost w m: '))

# bmi = waga / wzrost**2
# result = round(bmi,2)
# print("Twoje BMI to:" , result)
# if result < 20:
#     print("Za mało")
# elif result > 25:
#     print("Za dużo")
# else:
#     print("w sam raz")


# import random
# lucky = random.randint(0,100)
# print(lucky)
# number = int(input("Podaj liczbę całkowitą z przedzialu od 0 do 100: "))

# while number != lucky:
#     if number > lucky:
#         print("za duzo")
#     else:
#         print("za mało")
        
#     print("Sprobuj jeszcze raz")
#     number = int(input("Podaj liczbę całkowitą z przedzialu od 0 do 100: "))
# print("Gratulacje")

# from math import sqrt

# a = float(input("Podaj współczynnik a: "))
# b = float(input("Podaj współczynnik b: "))
# c = float(input("Podaj współczynnik c: "))

# delta = b ** 2 - 4 * a * c

# if delta > 0:
#     x1 = (-b - sqrt(delta)) / (2 * a)
#     x2 = (-b + sqrt(delta)) / (2 * a)
#     print("x1={:.2f}, x2={:.2f}".format(x1,x2))
   
# elif delta == 0:
#     x = -b / (2 * a)
#     print("x={:.2f}".format(x))
    
# else:
#     print("To równanie nie ma rozwiązań rzeczywistych")


# Zadanie opisuje program, który znajduje i wypisuje liczby doskonałe w przedziale od 1 do 10000. Liczba doskonała to taka liczba naturalna, która jest sumą swoich dzielników właściwych (czyli wszystkich dzielników, z wyłączeniem samej siebie).




# Liczby Armstronga (lub liczby narcystyczne) to takie liczby naturalne, które są równy sumie swoich cyfr podniesionych do potęgi liczby cyfr. Na przykład, 153 to liczba Armstronga, ponieważ 1^3 + 5^3 + 3^3 = 153.

# def findArmstrong(start, end):
#     list=[]
#     for num in range (start, end +1):
#         numStr = str(num)
#         leng = len(numStr)
#         result = sum(int(digit) ** leng for digit in numStr)
#         if result == num:
#             list.append(num)
#     return list

# print(findArmstrong(1,1000))




# napisz program, który znajduje liczby doskonałe w zadanym zakresie.
# Liczba doskonała to liczba, która jest równa sumie swoich dzielników właściwych (dzielników, z pominięciem samej liczby). Na przykład, 28 to liczba doskonała, ponieważ 1 + 2 + 4 + 7 + 14 = 28.



def perfectNum(start, end):
    result = []

    for num in range(start, end +1):
        sum = 0
        for i in range(1, num):
            if num%i ==0:
                sum +=i
        if sum == num:
            result.append(num)
    return result

start = 1
end = 100
print(perfectNum(start, end))