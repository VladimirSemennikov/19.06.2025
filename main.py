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





