import funciones as f

def menu(animales,clases):
    print("Lista de Animales de Zoológico")
    print("----------------------------")
    print("1. Filtrar por Clase")
    print("2. Filtrar por Característica")
    print("3. Agregar Animal")
    print("4. Salir")

    opcion = input("Eliga una opción:")

    if opcion == "1":
        print("Lista de Clases")
        print("---------------")
        for i in range(len(clases)-1):
            print(f"{i+1}. {clases[str(i+1)][0]}")
        opcion_clase = input("Eliga una clase:")
        animales_filtrado = f.filtrar_por_clase(animales,opcion_clase)
        f.imprimir_animales(animales_filtrado)
    elif opcion == "2":
        print("Lista de Características")
        print("------------------------")
        for i in range(len(caracteristicas)):
            print(f"{i+1}. {caracteristicas[i]}")
        opcion_caracteristica = input("Eliga una característica:")
        if opcion_caracteristica == "13":
            opcion_patas = input("Eliga el número de patas:")
            animales_filtrado = f.filtrar_por_caracteristica(animales,int(opcion_caracteristica)-1,opcion_patas)
        else:
            animales_filtrado = f.filtrar_por_caracteristica(animales,int(opcion_caracteristica)-1)
        f.imprimir_animales(animales_filtrado)
    elif opcion == "3":
        print("Agregar Animal")
        print("--------------")
        nombre = input("Ingrese el nombre del animal:")
        caracteristica_list = []
        print("Ingrese las características del animal (responda 0 o 1, si tiene o no la caracteristica, para el caso de patas poner la cantidad y para clase el numero de la clase):")
        for i in range(len(caracteristicas)+1):
            if i == 16:
                for i in range(len(clases)-1):
                    print(f"{i+1}. {clases[str(i+1)][0]}")
                caracteristica = input(f"Ingrese clase:")
            else:
                caracteristica = input(f"Ingrese {caracteristicas[i]}:")
            
            caracteristica_list.append(caracteristica)
        try:
            f.agregar_animal(animales,nombre,caracteristica_list)
            f.escribir_archivo_csv("zoo.csv",animales)
            f.leer_archivo_csv("zoo.csv")
            print("Animal agregado con éxito.")
        except:
            print("Error al agregar el animal.")
    elif opcion == "4":
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción inválida, intente de nuevo.")
        menu()

if __name__ == "__main__":
    animales = f.leer_archivo_csv("zoo.csv")
    clases = f.leer_archivo_csv("clases.csv")
    caracteristicas = animales['nombre_animal'][:16]
    # f.imprimir_diccionario(diccionario)
    menu(animales,clases)
