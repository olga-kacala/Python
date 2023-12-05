
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


def summary(*args):
    sum = 0
    args = list(args)
    args[0]=100
    for i in args:
        sum += i
    return sum
print(summary(1,2,3,))