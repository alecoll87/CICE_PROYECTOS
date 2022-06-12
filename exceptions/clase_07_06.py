a = "hola"
b = 3

try:
    c
    b / 0
except TypeError:
    print("Ha sucedido un TypeError")
except ZeroDivisionError as e:
    print("Zero division")
    print("e")
except Exception as e:
    print ("Algo ha ido mal")
    print(e)
    print(Exception.__name__)

def get_doubles(array):
    if type(array) != list or type(array) != tuple:
        raise TypeError("No admintioms iterables != a listas o tuplas")
    result = []
    i = 0
    while i < len(array):
        result.append(arrai[i]**2)
        i += 1
    return result

benford = {"1":30.3, "2": 14.3, "3": 8}
print(get_doubles(benford.values()))

print("fin")