import sys
import requests as req
import os

CWD = os.getcwd()

url ="https://restcountries.com/v3.1"

def menu():
    print("Welcome")
    print("1. Search country")
    print("2. Download flag")
    print("3. Play country")
    print("q. exit")
    
def pretty_print(country):
    for k,v in country.items():
        print(f"{k.upper()}: {v}")

def get_country(country_name: str) -> tuple:
    keys = ("capital", "population", "area", "languages")
    result = {k:None for k in keys}
    res = req.get(f"{url}/name/{country_name}").json()
    if len(res) >= 1:
        country = res[0]
        result["capital"] = country["capital"][0]
        result["population"] = country["population"]
        result["area"] = country["area"]
        result["languages"] = tuple(country["languages"].values())
        return (result, tuple(country["flags"].values())[0])


def download_flag(url: str) -> bool:
    flag_name = url[-6:]
    flag_img = req.get(url)
    if flag_img.status_code == 200:
        flag_img = flag_img.content
        flag_file = open(f"{CWD}/flags/{flag_name}", "wb")
        flag_file.close()
        return True
    return False




