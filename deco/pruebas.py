from functools import wraps
from datetime import *

def logs(func):
    @wraps(func)
    def write_logs(*args):
        with open("funcs.log", "a") as file:
            file.write(f"{datetime.now()} | la función {func.__name__} ha generado un registro")
        return func(*args)
    return write_logs

