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

Ciudades_Caminos2 = {
    'Salina Cruz': ['Tehuanepec','Huatulco'],
    'Huatulco': ['Salina Cruz','Puerto Escondido'],
    'Puerto Escondido': ['Huatulco'],
    'Tehuanepec': ['Salina Cruz', 'Oaxaca','Juchitan'],
    'Juchitan': ['Ixtepec','Tonala', 'Tehuanepec','Acayucan'],
    'Acayucan': ['Juchitan','Veracruz','Minatitlan'],
    'Oaxaca': ['Tehuanepec','Puebla'],
    'Puebla': ['Cd. Mexico','Orizaba', 'Oaxaca'],
    'Cd. Mexico': ['Puebla'],
    'Orizaba': ['Puebla','Cordoba'],
    'Cordoba': ['Orizaba','Veracruz'],
    'Veracruz': ['Cordoba','Jalapa', 'Poza Rica','Acayucan'],
    'Jalapa': ['Veracruz'],
    'Poza Rica': ['Veracruz', 'Tuxpan'],
    'Tuxpan': ['Poza Rica', 'Tampico'],
    'Tampico': ['Matamoros', 'Tuxpan'],
    'Matamoros': ['Tampico', 'Reynosa'],
    'Reynosa': ['Matamoros'],
    'Ixtepec': ['Ixcatepec', 'Juchitan'],
    'Ixcatepec': ['Ixtepec'],
    'Tonala': ['Tuxla Gutierrez','Pijijipan', 'Juchitan'],
    'Pijijipan': ['Huixtla', 'Tonala'],
    'Huixtla': ['Pijijipan', 'Tapachula'],
    'Tapachula': ['Huixtla'],
    'Tuxla Gutierrez': ['Villahermosa','Tonala'],
    'Villahermosa': ['Cardenaz','Palenque', 'Cd. del Carmen','Tuxla Gutierrez'],
    'Cardenaz': ['Coatzacoalcos','Villahermosa'],
    'Coatzacoalcos': ['Minatitlan','Cardenaz'],
    'Minatitlan': ['Acayucan','Coatzacoalcos'],
    'Palenque': ['Ococingo','Villahermosa'],
    'Ococingo': ['Palenque','San Cristobal'],
    'San Cristobal': ['Comitan','Ococingo'],
    'Comitan': ['San Cristobal'],
    'Cd. del Carmen': ['Villahermosa','Campeche'],
    'Campeche': ['Chetumal','Merida', 'Cd. del Carmen'],
    'Chetumal': ['Campeche','Playa del carmen'],
    'Playa del carmen': ['Chetumal','Cancun'],
    'Cancun': ['Playa del carmen','Merida'],
    'Merida': ['Campeche','Cancun']


    


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

camino = busqueda(Ciudades_Caminos2,'Salina Cruz', 'Reynosa')
print(camino)


