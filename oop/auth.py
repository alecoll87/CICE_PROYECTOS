from os import getcwd
import json
from uuid import uuid4
from hashlib import sha1
from functools import wraps
import datetime as dt

def o(func):
    @wrpas(func)
    def i(*args):
        return func()
    return i


CWD = getcwd()
file_path = f"{CWD}/user.json"

user_name = None

def accesslog(func):
    @wraps(func)
    def inner(*args):
        print(f"{dt.datetime.now()} | {user_name} | {func.__name__} ")
        return func (*args)
    return inner

def read(file_path):
    file = open(file_path, encoding="utf8")
    data = json.load(file)
    file.close()
    return data

def write(file_path, data):
    file = open(file_path, mode="w")
    json.dump(data, file, indent=4, ensure_ascii=False)
    return True

def get_by_name(name, users):
    return next(filter(lambda user: user["name"] == name, users), False)

def get_by_key(key, value, users):
    return next(filter(lambda user: user[key] == value, users), False)

def create_user(name, pwd):
    users = read(file_path)
    is_user = get_by_name(name, users["data"])
    if is_user:
        return False
    pwd = sha1(pwd.encode()).hexdigest()
    user = {
        "id": uuid4().hex,
        "name": name,
        "pwd": pwd
    }
    users["data"].append(user)
    write(file_path, users)
    return True

def is_authenticated(name, pwd):
    users = read(file_path)["data"]
    user = get_by_name(name, users)
    if user:
        if user["pwd"] == sha1(pwd.encode()).hexdigest():
            return True
    return False




if __name__ == "__main__":
    #TESTING:
    print(create_user("test_10", "1234"))
    print(is_authenticated("test_10", "1233"))