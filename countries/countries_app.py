import json
from os import system
from utils import menu, get_country, pretty_print, download_flag

system("clear")
user = ""
while user != "q":
    menu()
    user = input ("option: ")
    system("clear")
    menu()
    if user == "1":
        country_name = input("Country: ")
        country, flag = get_country(country_name)
        pretty_print(country)
        input(": ")
        system ("clear")

        menu()
    if user == "2":
        country, flag = get_country(country_name)
        is_flag = input("Download flag?(Y/N): ").lower()
        if is_flag == "y":
            if download_flag(flag):
                print("Download successful")
                input("...")
    system("clear")