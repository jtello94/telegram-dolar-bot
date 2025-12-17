import requests
from pprint import pprint
'''
Separamos responsabilidades (buena practica)
- El bot queda como está
- Creamos un archivo nuevo solo para probar precios
'''

# URL de la api a consumir

URL = "https://dolarapi.com/v1/dolares"


def get_dolar():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()


data = get_dolar()

for item in data:
    if item['casa'] in ['bolsa', 'cripto']:
        print(
            f'{item['nombre']}:'
            f'compra {item['compra']} | '
            f'venta {item['venta']} | '
            f'fecha {item['fechaActualizacion']}'
        )
