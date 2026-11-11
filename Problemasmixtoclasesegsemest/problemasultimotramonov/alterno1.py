import requests

URL = "https://findic.cl/api/"

request = requests.get(URL)

data = request.json()
question = data("results")

with requests.Session() as session:
    session.headers.update({
        "User-Agent": "findic-docs-python/1.0",
        "Accept": "application/json",
    })

    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Obtenemos el valor de UF
        uf = data["uf"]

        print(f"Fecha: {uf['fecha']}")
        print(f"Valor UF: $ {uf['valor']}")
    except requests.RequestException as error:
        print(f"Error en la solicitud: {error}")    
