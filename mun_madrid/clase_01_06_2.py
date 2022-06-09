import requests as req

res = req.get("https://github.com/alecoll87/CICE_PROYECTOS")
print(res.content)

