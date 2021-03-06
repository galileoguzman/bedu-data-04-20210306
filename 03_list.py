def aplicar_iva(precio):
    return precio * 1.16


lista_precios = [
    200,
    100,
    50
]

lista_precios_iva = list(map(aplicar_iva, lista_precios))
print(lista_precios_iva)
