def leer_archivo_csv(archivo) -> dict:
    lista = []
    with open(archivo, "r", encoding="utf-8") as file:
        for linea in file:
            linea = linea.replace("\n", "")
            lista.append(linea.split(","))
    try:
        for linea in lista:
            linea[0] = int(linea[0])
    except:
        pass
    diccionario = {}
    for linea in lista:
        diccionario[linea[0]] = linea[1:]
    return diccionario

def escribir_archivo_csv(archivo, diccionario):
    lista = []
    for clave, valor in diccionario.items():
        lista.append([clave] + valor)
    with open(archivo, "w", encoding="utf-8") as file:
        for linea in lista:
            file.write(",".join(linea) + "\n")

def imprimir_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(clave, valor)

def imprimir_animales(diccionario):
    for clave, valor in diccionario.items():
        print(clave)

def filtrar_por_clase(diccionario, clase):
    diccionario_filtrado = {}
    for clave, valor in diccionario.items():
        if valor[16] == clase:
            diccionario_filtrado[clave] = valor
    return diccionario_filtrado

def filtrar_por_caracteristica(diccionario, caracteristica, patas=None):
    diccionario_filtrado = {}
    for clave, valor in diccionario.items():
        if patas:
            if valor[caracteristica] == patas:
                diccionario_filtrado[clave] = valor
        else:
            if valor[caracteristica] == "1":
                diccionario_filtrado[clave] = valor
    return diccionario_filtrado

def agregar_animal(diccionario, nombre, caracteristicas):
    animal = []
    for caracteristica in caracteristicas:
        animal.append(caracteristica)
    diccionario[nombre] = animal

if __name__ == "__main__":
    print("Este archivo es para importar funciones.")