import requests

# Endpoint de la API para obtener el resumen diario
url = "https://findic.cl/api/"

# Reutilizamos una sesión para enviar las mismas cabeceras en cada consulta
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




{
    "version": "1.3.0",
    "autor": "findic.cl",
    "fecha": "2025-11-04",
    "uf": {
        "codigo": "uf",
        "nombre": "Unidad de fomento (UF)",
        "unidad_medida": "Pesos",
        "fecha": "2025-11-04",
        "valor": 39618.08
    },
    "ivp": {
        "codigo": "ivp",
        "nombre": "Indice de valor promedio (IVP)",
        "unidad_medida": "Pesos",
        "fecha": "2025-11-04",
        "valor": 41163.96
    },
    "dolar": {
        "codigo": "dolar",
        "nombre": "Dólar observado",
        "unidad_medida": "Pesos",
        "fecha": "2025-11-04",
        "valor": 940.53
    },
    "dolar_intercambio": {
        "codigo": "dolar_intercambio",
        "nombre": "Dólar acuerdo",
        "unidad_medida": "Pesos",
        "fecha": "2018-01-09",
        "valor": 837.59
    },
    "euro": {
        "codigo": "euro",
        "nombre": "Euro (pesos por euro)",
        "unidad_medida": "Pesos",
        "fecha": "2025-11-04",
        "valor": 1084.68
    },
    "ipc": {
        "codigo": "ipc",
        "nombre": "Indice de Precios al Consumidor (IPC)",
        "unidad_medida": "Porcentaje",
        "fecha": "2025-09-01",
        "valor": 0.4
    },
    "utm": {
        "codigo": "utm",
        "nombre": "Unidad Tributaria Mensual (UTM)",
        "unidad_medida": "Pesos",
        "fecha": "2025-11-01",
        "valor": 69542.0
    },
    "imacec": {
        "codigo": "imacec",
        "nombre": "Imacec",
        "unidad_medida": "Porcentaje",
        "fecha": "2025-09-01",
        "valor": 3.2
    },
    "tpm": {
        "codigo": "tpm",
        "nombre": "Tasa Política Monetaria (TPM)",
        "unidad_medida": "Porcentaje",
        "fecha": "2025-11-04",
        "valor": 4.75
    },
    "libra_cobre": {
        "codigo": "libra_cobre",
        "nombre": "Libra de Cobre",
        "unidad_medida": "Dólar",
        "fecha": "2025-11-04",
        "valor": 4.93
    },
    "tasa_desempleo": {
        "codigo": "tasa_desempleo",
        "nombre": "Tasa de desempleo Mensual",
        "unidad_medida": "Porcentaje",
        "fecha": "2025-09-01",
        "valor": 8.53
    },
    "ipsa": {
        "codigo": "ipsa",
        "nombre": "IPSA (Índice de Precios Selectivo de Acciones)",
        "unidad_medida": "Puntos",
        "fecha": "2025-10-29",
        "valor": 9326.5
    },
    "yen": {
        "codigo": "yen",
        "nombre": "Yen (pesos por yen)",
        "unidad_medida": "Pesos",
        "fecha": "2025-11-04",
        "valor": 6.1
    },
    "bitcoin": {
        "codigo": "bitcoin",
        "nombre": "Bitcoin",
        "unidad_medida": "Dólar",
        "fecha": "2025-11-03",
        "valor": 106547.52
    },
    "ethereum": {
        "codigo": "ethereum",
        "nombre": "Ethereum",
        "unidad_medida": "Dólar",
        "fecha": "2025-11-03",
        "valor": 3602.31
    },
    "monero": {
        "codigo": "monero",
        "nombre": "Monero",
        "unidad_medida": "Dólar",
        "fecha": "2025-11-03",
        "valor": 345.42
    },
    "solana": {
        "codigo": "solana",
        "nombre": "Solana",
        "unidad_medida": "Dólar",
        "fecha": "2025-11-03",
        "valor": 166.09
    }
}        