# funciones anónimas/lambda
# built in functions map - filter - reduce
# generators
# iterable - iterator
# operadores ternarios / ternary operators
# args & kwargs

def greeting(name):
    return f"hola {name}"

lambda name: f"hola {name}"

maths = {
    "double": lambda num: num**2,
    "triple": lambda num: num**3,
    "square": lambda num: num**0.5
}

# print(maths["double"](2))


f_add = lambda num_1, num_2: num_1 + num_2
b = f_add(1,2)
# print(b)

ej_1 = lambda word: (word*2).upper()
# print(ej_1("ale"))

ej_2 = lambda num_1, num_2: num_1 ** num_2
# print(ej_2(2,8))

# map

a= [1,2,3,4]
b = map(lambda num: num**2,a)
# print(b)
# print(list(b))

'''
1. un bucle: todo elemento de a es pasado como argumento al parámetro num / for
2. se ejecuta la función / ()
3. se retornan los valores / return
4. se guardan en un iterable / append

'''

def double(num):
    return num**2
a = [1,2,3,4]
b = list(map(double, a))
# print(b)


'''
1. un bucle: todo elemento de a es pasado como argumento al parámetro num / for
2. se ejecuta la función / ()
3. se retornan los valores / return
4. if stament
5. se guardan en un iterable / append

'''

values = [1,2,3,4]
result = list(filter(lambda num: num %2 == 0, values))
# print(result) 

def a(data):
    result = []
    for num in data:
        if num %2 == 0:
            result.append(num)
        return result

values = [1,2,3,4]

def b(num):
    if num % 2 == 0:
        return num

result = list(filter(b, values))
# print(result)

values = [1,2,3,4]

filter_values = filter(lambda num: num %2 != 0, values)

values.remove(1)

# print(list(filter_values))


# print(tuple(zip((1,2,3,4), ("a", "b", "c", "d"))))

a = (1,2,3,4,5)
b = ("a", "b", "c", "d", "e")

print(list(map(lambda num1, num2: (num1, num2),a ,b)))