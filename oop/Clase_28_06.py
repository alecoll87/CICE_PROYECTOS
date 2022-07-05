from typing import Tuple
from os import getcwd
import json
from uuid import uuid4
from hashlib import sha1
from functools import wraps
import datetime as dt

class Auth:

    def __init__(self, file_path):
        self.file_path = file_path

    @property    
    def users(self):
        file = open(self.file_path, encoding="utf8")
        data = json.load(file)
        file.close()
        return data
    
    def write(self, data):
        file = open(self.file_path, mode="w")
        json.dump(data, file, indent=4, ensure_ascii=False)
        return True

    def get_by_name(self, name: str) -> Tuple[dict, bool]:
        return next(filter(lambda user: user["name"] == name, self.users["data"]), False)

    def create_user(self, name, pwd):
        is_user = self.get_by_name(name)
        if is_user:
            return False
        pwd = sha1(pwd.encode()).hexdigest()
        user = {
            "id": uuid4().hex,
            "name": name,
            "pwd": pwd
        }
        users_copy = self.users.copy()
        users_copy["data"].append(user)
        self.write(users_copy)
        return True

file_path = f"{getcwd()}/user.json"
test = Auth(file_path)
test.create_user("tes_4", "1234")
