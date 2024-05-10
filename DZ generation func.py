# Фабрика функций для умножения и деления:
def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x * y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x / y
        return subtract

my_func_add = create_operation("add")
print(my_func_add(1,2))
my_func_add = create_operation("subtract")
print(my_func_add(1,2))

# Пример лямбда функции с аналогом через def, возведение в степень
multiply = lambda x, y: x ** y
print(multiply(2, 3)) # Выводит 6

def multiply_def(x, y):
   return x ** y
print(multiply_def(2, 3)) # Выводит 6

# Пример создания вызываемого объекта
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


square = Rect(5, 10)
print(square())

