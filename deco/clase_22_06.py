from functools import wraps
from datetime import *

def date_func():
    date = datetime.now()
    return date

def logs(func):
    @wraps(func)
    def write_logs(*args):
        with open("funcs.log", "a") as file:
            file.write(f"{datetime.now()} | la función {func.__name__} ha generado un registro")
        return func(*args)
    return write_logs

def outter (func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("Ejecutando", func.__name__)
        print(date_func())
        return func(*args, **kwargs)
    return inner

@outter
def greeting():
    return "Hola sin adornos"

@outter
def add():
    return sum ((1,2,3,4,5,6,7))

@outter
def double():
    return 5 * 2

print(add())
print(double())
print(greeting())

