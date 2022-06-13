# Operadores ternarios

#SINTAXIS: _true_result_if condition_else_false_result_

# >=18 es adulto
from xml.dom.minidom import Element


age = 26
is_adult= True if age >= 18 else False

# if is_adult:
#     print("Puede comprar cerveza")
# else:
#     print("No puede comprar cerveza")

carnet= "carnet mayor" if age >= 65 else "carnet adulto" if age >= 26 else "carnet joven"
# result_1 | result_2
# print(carnet)

a = [1,2,3,4]
# __ for __ in __ s
# print([num for num in a if num % 2 == 0])

# print([num**2 if num %2 ==0 else num **3 for num in a])

map(lambda num: num ** 2 if num % 2 == 0 else num ** 3, a)

# args cuando queremos recibir n numero de argumentos

# def add(*args):
    # print(args)
    # print(sum(args))

add = (1,2,3,4,5,6,7)

def add(num_type, *args):
    result = sum(args)
    if num_type == "int":
        return int(result)
    else:
        return float(result)

print(add("float", 1,2,3,4,4,123,3442))

def add_2(x, y, is_int=True):
    if is_int:
        return int(x, y)
    else:
        return float (x + y)

def add_3(**kwargs):
    if kwargs.get("is_int"):
        print(int(x + y))

add_3(a=3, b=4)

b = zip(a,a)
c = enumerate(a)
d = filter(lambda num: num % 2 == 0, a)

def my_filter(array):
    for num in array:
        if num % 2 == 0:
            yield num

e =my_filter(a)


print(next(e))
print(next(e))

def my_filter(func, array):
    for element in array:
        if func(element):
            yield element
       
e = my_filter(lambda num: num % 2 == 0, a)
print(list(e))

def my_map(func, array):
    for element in array:
        yield func(element)

def my_map_2(func, *args):
    for element in zip(*args):
        yield func(*element)

my_m = map(x, y)

print(next(element for element in a))
(element for element in a)
[element for element in a]


def add(x: int, y: int) -> int:
    if type(x) != int or type(y) != int:
        raise TypeError (f"{x} and {y} must be intergers")
        



