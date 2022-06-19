import json
from os import *
from utils import *

system("clear")
user = ""
while user != "q":
    menu()
    user = input ("option: ")
    system("clear")
    menu()
    if user == "1":
        country_name = input("Country: ")
        system("clear")
        menu()
        country, flag = get_country(country_name)
        if country:
            pretty_print(country)
        else:
            print("Not found")
        input(": ")
        system ("clear")

    elif user == "2":
        system ("clear")
        # country_name = input("Country: ")
        country, flag = get_country(country_name)
        is_flag = input("Download flag?(Y/N): ").lower()
        if is_flag == "y":
            if download_flag(flag):
                print("Download successful")
                input("...")
        system ("clear")


    elif user == "3":
        system ("clear")
        flags = os.listdir(f"{CWD}/flags")
        for i, flag in enumerate(flags):
            print(f"{i+1}. {flag}")
        
        user = int(input("Do you want to erase any glags?(indicate number): "))
        os.remove(f"{CWD}/flags/{flags[user-1]}")
        
        system ("clear")
   