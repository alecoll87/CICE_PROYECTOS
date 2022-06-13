import requests as req

url ="https://restcountries.com/v3.1/all"

res = req.get(url).json()

print(res)


