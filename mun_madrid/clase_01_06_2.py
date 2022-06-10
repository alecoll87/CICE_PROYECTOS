import requests as req

res = req.get("https://www.deamadrid.com/numbers")

if res.status_code >= 200:
    print(res.content)
    pass

