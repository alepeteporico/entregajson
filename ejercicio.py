from funciones import * 
import json
with open("movies.json") as fichero:
    datos=json.load(fichero)

while True:
    print("====================MENÚ====================")
    print("1. Listar el título, año y duración de todas las películas.")
    print("2. Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una.")
    print("3. Mostrar las películas que contengan en la sinopsis dos palabras dadas.")
    print("4. Mostrar las películas en las que ha trabajado un actor dado.")
    print("5. Mostrar el título y la url del póster de las tres películas con una media de puntuaciones más alta y lanzadas entre dos fechas dadas.")
    print("6. Salir.")
    print("============================================")
    opc=int(input("Elige una opción: "))

    if opc==1:
        for i in ej1(datos):
            print("-",i["titulo"])
            print("-",i["año"])
            print("-",i["duracion"])
            print("--------------------------------")
        print("--------------------------------")
        print("")
    
    elif opc==2:
        for i in ej2(datos):
            print("-",i["titulo"])
            print("-",i["actores"])
            print("--------------------------------")
        print("--------------------------------")
        print("")
    
    elif opc==3:
        cad1=input("Dime una palabra: ")
        cad2=input("Dime otra palabra: ")
        for i in ej3(datos,cad1,cad2):
            print("-",i)
        print("--------------------------------")
        print("")
    
    elif opc==6:
        break

    else:
        print("ERROR")
        print("--------------------------------")
        print("")