import sys
import requests as req
import os
import random as rd
import auth

CWD = os.getcwd()

url ="https://restcountries.com/v3.1"


def menu():
    print("Welcome")
    print("1. Search country")
    print("2. Download flag")
    print("3. Remove flag")
    print("4. Play Game")
    print("q. exit")
    
def pretty_print(country):
    for k,v in country.items():
        print(f"{k.upper()}: {v}")

def get_country(country_name: str) -> tuple:
    keys = ("capital", "population", "area", "languages")
    result = {k:None for k in keys}
    res = req.get(f"{url}/name/{country_name}?fullText=True")
    country = res if res.status_code == 200 else req.get(f"{url}/name/{country_name}")
    country = country.json() if res.status_code == 200 else False
    if country:
        country = country[0]
        result["capital"] = country["capital"][0]
        result["population"] = country["population"]
        result["area"] = country["area"]
        result["languages"] = tuple(country["languages"].values())
        return (result, tuple(country["flags"].values())[0])
    return False

@auth.accesslog
def download_flag(url: str) -> bool:
    flag_name = url[-6:]
    flag_img = req.get(url)
    if flag_img.status_code == 200:
        flag_img = flag_img.content
        flag_file = open(f"{CWD}/flags/{flag_name}", "wb")
        flag_file.close()
        return True
    return False



def menu_continent():
    print("1. American continent")
    print("2. African continent")
    print("3. Asian continent")
    print("4. European Continent")
    print("5. Continent of Oceania")
    print("q. exit")



region = req.get(f"{url}/region/americas").json()
rd.shuffle(region)



questions = [
    {
        "q": "*@*'s Capital",
        "key": "capital"
    },
    {
        "q": "*@*'s Population",
        "key": "capital"
    },
    {
        "q": "*@*'s Surface",
        "key": "capital"
    }

]

for q in questions:
    i = rd.randint(0, len(region))
    country = region[i]
    q["q"] = q["q"].replace("*@*", region[i]["name"]["common"])
    q["a"] = country[q["key"]]
    print(q["q"])
    if type(q["a"]) == list:
        print(q["a"][0])
    else:
        print(q["a"])


