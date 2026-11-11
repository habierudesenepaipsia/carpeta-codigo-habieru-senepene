import requests

#la informacion web que nos da la informacion del perro
url = "https://api.thedogapi.com/v1/images/search"

#le pedimos los datos al servidor
respuesta = requests.get(url)

#transformamos la respuesta en un diccionario/lista de python
datos = respuesta.json()

#como la API nos devuelve una lista con un elemento dentro, sacamos el primer resultado
perro = datos[0]

#extraemos la informacion que necesitamos 
link_foto = perro["url"]
id_perro = perro["id"]

print("ID del perro: ", id_perro)
print("Link de su foto: ", link_foto)