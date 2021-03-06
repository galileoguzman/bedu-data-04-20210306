lista_de_nombres_personas = [
    'JOSEPH BANKS',
    'PHILLIP HAMILTON',
    'ALEXANDER HAMILTON',
    'Galileo GUZman',
    'Guillermo Jimenez'
]

lista_nombres_homogenizados = []
for nombre in lista_de_nombres_personas:
    nombre_limpio = nombre.lower().strip().replace(' ', '_')
    lista_nombres_homogenizados.append(nombre_limpio)

print(lista_nombres_homogenizados)
