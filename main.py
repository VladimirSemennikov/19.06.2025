# Наследование и super()

"""
Для вызова объектов с помощью super() используется следующая конструкция:
super().метод()
super().атрибут
"""
#Обращение к методу

# class Cat:
#     def hello_cat(self):
#         self.name = 'hello cat'
# class Dog(Cat):
#     def hello_dog(self):
#         super().hello_cat()
#
# test = Dog()
# test.hello_dog()        #вызвали метод дочернего класса hello_dog
#
# print(test.name)        #hello cat


#Обращение к атрибуту

# class Cat:
#     name = 'cat'
# class Dog(Cat):
#     def print_name(self):
#         print(super().name)
# test = Dog()
# test.print_name()           # cat



# с использованием __init__ и super()

# class Cat:
#     def __init__(self):
#         self.cat = 'котик'
# class Test(Cat):
#     def __init__(self):
#         super().__init__()
#         self.dog = 'песик'
#
# test = Test()
#
# print(test.cat)     #котик
# print(test.dog)     #песик

"""
Важные моменты
1) Функция super() используется в методах дочернего класса и позволяет обращаться к методам родительского класса
2) Функция super() позволяет обращаться и к атрибутам родительного класса, но не позволяет создавать или изменять их.
3) Функция super() позволяет обращаться к объектам родительского класса, без явного использования его имени, что
делает код более гибким, так как имя класса может измениться.
4) Функция super() имеет необязательные атрибуты, они чаще используются во множественно наследовании, но об этом позже
"""

# class Minecraft:
#     def hello_creeper(self):
#         self.name = 'Hello, Creeper!'
#         print('Hello, Creeper!')
#
# class Roblox(Minecraft):
#     def hello_all(self):
#         super().hello_creeper()
#         print("Hello, Pozzy!")
# hello = Roblox()
# hello.hello_all()
#
# print(hello.name)


# class Alfa:
#     def sum_number(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.x +self.y)
# class Beta(Alfa):
#     def result(self, x, y, z):
#         super().sum_number(x, y)
#         self.z = z
#         print(self.z)
# test = Beta()
# test.result(10, 20, 50)


"""
Важные моменты
1) в команде super().sum_number(x,y) мы должны обязательно указать параметры x,y
"""

# class Alfa():
#     @staticmethod
#     def sum_numbers(x, y):
#         return x + y
# class Beta(Alfa):
#     def result(self, x, y, z):
#         summa = super().sum_numbers(x, y)
#         print(summa / z)
# test = Beta()
# test.result(10,20,30)


# class Person:
#     def __init__(self, name, age, height, weight):          #создает 4 атрибута
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
# class Student(Person):                  #студент
#     def __init__(self, name, age, height, weight, class_number, hobby):
#         super().__init__(name, age, height, weight)                     #запускаем инит родитеслького класса
#         self.class_number = class_number
#         self.hobby = hobby
# class Worker(Person):                       #сотрудники
#     def __init__(self, name, age, height, weight, work, experience):
#         super().__init__(name, age, height, weight)
#         self.work = work
#         self.experience = experience
# id1 = Student('Tanya', 6, 100, 25, 1, 'cook')
# id2 = Worker('Vasya', 28, 180, 70, 'driver', 6)
#
# print(id1.__dict__)
# print(id2.__dict__)

#1 способ
# class Parent:
#     def grout(self):
#         print("Hello from Parent")
# class Child(Parent):
#     def grout(self):
#         super().grout()
#         print("Hello from Child")
# c = Child()
# c.grout()

#2 способ
# class Parent:
#     def grout(self):
#         print("Hello from Parent")
# class Child(Parent):
#     def grout(self):
#         super(Child, self).grout()
#         print("Hello from Child")
# c = Child()
# c.grout()


#Множественные наследования

# class A:
#     def method1(self):
#         print("Method 1 from A")
# class B:
#     def method2(self):
#         print("Method 2 from B")
# class C(A, B):
#     def method3(self):
#         print("Method 3 from C")
# child = C()
#
# child.method1()     #Method 1 from A
# child.method2()     #Method 2 from B
# child.method3()     #Method 3 from C



# class King:
#     a = 4
# class Queen:
#     b = 6
# class Prince(King, Queen):
#     c = 10
#
# count = Prince()
# print(f"Результат сложения: {count.a + count.b + count.c}")


#Пример влияния порядка наследования

# class A:
#     def __init__(self):
#         print("Метод класса А")
# class B:
#     def __init__(self):
#         print("Метод класса В")
# class C(A, B):
#     def __init__(self):
#         print("Метод класса С")
#
# c = C()

"""
Атрибут __mro__
MRO - (method resolution order) - это порядокв котором Python ищет методы в иерархии
класса при наследовании. (С3 Linearization) для определения MRO. 
"""

# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B, C):
#     pass
# print(D.__mro__)
#(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

"""
MRO особенно полезен при множественном наследовании. когда у класса есть несколько родительских классов.
Он помогает избежать проблем с дублированием методов и позволяет определить, какой метод будет вызван
в случае конфликта имен методов а разных классах
"""