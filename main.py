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
потому что
"""

class Alfa():
    @staticmethod
    def sum_numbers(x, y):
        return x + y
class Beta(Alfa):
    def result(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        summa = self.sum_numbers(x, y)
        print(summa / z)
test = Beta()
test.result(10,20,30)