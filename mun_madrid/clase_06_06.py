import requests as req

url = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json"

res = req.get(url).json()

print("1. Obtener municipio por código INE\n")

data = res["data"]

def get_by_ine(mun_ine):
    for mun in data:
        if mun["municipio_codigo_ine"] == mun_ine:
            return mun

print(get_by_ine("280014"), "\n")


print("2. Obtener el municipio más grande\n")

def max_surface():
    max_num = 0.0
    municipio = ""
    for surface in data:
        if surface["superficie_km2"] > max_num:
            max_num = surface["superficie_km2"]
            municipio = surface
    return municipio 
print(max_surface(), "\n")

print("3. Obtener superficie total\n")

total_surface = sum([mun["superficie_km2"] for mun in data])

print (total_surface, "\n")

print("4. Obtener densidad total\n")

total_density = sum([mun["densidad_por_km2"] for mun in data])

print (total_density, "\n")

print("5. Obtener la población de Madrid\n")

madrid_population = total_surface * total_density

print (madrid_population, "\n")

print("6. Obtener la población media de los municipios\n")

def population():
    result = 0
    for mun in data:
        result += mun["superficie_km2"] * mun["densidad_por_km2"]
    return result
print(population()/len(data), "\n")

print("7.Comprobar la ley de Benford\n")











