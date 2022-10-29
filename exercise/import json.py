import json

texto = '{"atributo1": "valor 1", "atributo2": 23}'

objeto = json.loads(texto)

print(objeto['atributo1'])