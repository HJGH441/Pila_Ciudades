from collections import deque
pila = []

Ciudades_Caminos = {
    'Salina Cruz': ['Tehuanepec','Huatulco'],
    'Huatulco': ['Salina Cruz','Puerto Escondido'],
    'Puerto Escondido': ['Huatulco'],
    'Tehuanepec': ['Salina Cruz', 'Oaxaca'],
    'Oaxaca': ['Tehuanepec','Puebla'],
    'Puebla': ['Cd. Mexico','Orizaba', 'Oaxaca'],
    'Cd. Mexico': ['Puebla'],
    'Orizaba': ['Puebla','Cordoba'],
    'Cordoba': ['Orizaba','Veracruz'],
    'Veracruz': ['Cordoba','Jalapa', 'Poza Rica'],
    'Jalapa': ['Veracruz'],
    'Poza Rica': ['Veracruz', 'Tuxpan'],
    'Tuxpan': ['Poza Rica', 'Tampico'],
    'Tampico': ['Matamoros', 'Tuxpan'],
    'Matamoros': ['Tampico', 'Reynosa'],
    'Reynosa': ['Matamoros']
}

def busqueda(x, y, z):
    cola = deque()
    cola.append((y, []))
    visitados = set()

    while cola:
        actual, camino = cola.popleft()
        if actual in visitados:
            continue
        if actual == z:
            return camino + [actual]
        visitados.add(actual)
        for vecino in x[actual]:
            cola.append((vecino, camino + [actual]))
    return None

camino = busqueda(Ciudades_Caminos,'Salina Cruz', 'Reynosa')

print(camino)
