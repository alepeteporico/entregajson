def ej1(datos):
    lista=[]
    for descripcion in datos:
        lista.append({"titulo":descripcion.get("title"),"año":descripcion.get("year"),"duracion":descripcion.get("duration")})
    return lista

def ej2(datos):
    lista=[]
    for descripcion in datos:
        lista.append({"titulo":descripcion.get("title"),"actores":len(descripcion.get("actors"))})
    return lista

def ej3(datos,cad1,cad2):
    lista=[]
    for descripcion in datos:
        if cad1 in descripcion["storyline"] and cad2 in descripcion["storyline"]:
            lista.append(descripcion.get("title"))
    return lista