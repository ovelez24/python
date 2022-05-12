def run():
    mi_diccionario = {
        "llave1" : 1,
        "llave2" : 2,
        "llave3" : 3,
    }
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

    poblacion_paises = {
        "argentina" : 44938712,
        "brasil" : 210147125,
        "colombia" : 50372424,
    }

    # print(poblacion_paises["argentina"])

    # for pais in poblacion_paises.keys():# aqui muestra la llave
    #     print(pais)

    # for pais in poblacion_paises.values(): #aqui muestra los valores dentro de la llave
    #     print(pais)

    for pais, poblacion in poblacion_paises.items(): #aqui muestra tanto la llave como los valores
        print(pais + " tiene " + str(poblacion) + " habitantes ")


if __name__ == '__main__':
    run()
