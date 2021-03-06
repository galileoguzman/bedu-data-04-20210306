def funcion_para_homogenizar_nombres(nombre):
    return nombre.lower().strip().replace(' ', '_')

lista_de_nombres_personas = [
    'JOSEPH BANKS',
    'PHILLIP HAMILTON',
    'ALEXANDER HAMILTON',
    'Galileo GUZman',
    'Guillermo Jimenez'
]

nombres_homogenizados = list(map(
        funcion_para_homogenizar_nombres,
        lista_de_nombres_personas
    )
)
print(type(nombres_homogenizados))
