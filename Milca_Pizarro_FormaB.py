#que denbe hacer el programa 
#que entra -primero validar si puede entrar
#que devuelve
#que errores se puede cometer
#que devuelve

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción"))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida")
        except:
            print("Debe seleccionar una opción valida")




def buscar_codigo(codigo, peliculas):
    codigo = codigo.upper()
    for cod in peliculas:
        if cod.upper() == codigo:
            return True
    return False










def cupos_genero(genero, peliculas, cartelera):
    total = 0
    genero = genero.lower()

    for codigo in peliculas:
        if peliculas[codigo][1].lower() == genero:
            total += cartelera[codigo][1]

    print("Los cupos que quedan son", total)









def busqueda_precio(p_min, p_max, peliculas, cartelera):
    lista = []

    for codigo in cartelera:
        precio = cartelera[codigo][0]#??? si en cero
        cupos = cartelera[codigo][1] 

        if p_min <= precio <= p_max and cupos != 0:
            titulo = peliculas[codigo][0]#??? si en cero
            lista.append(titulo + "--" + codigo)
            lista.sort()




    if len(lista) == 0:
        print("No hay peliculas con estos precios")
    else:
        print("Las peliculas encontradas son", lista)










def actualizar_precio(codigo, nuevo_precio, peliculas, cartelera):

    if buscar_codigo(codigo, peliculas): 

        codigo = codigo.upper()

        for cod in cartelera:
            if cod.upper() == codigo:
                cartelera[cod][0] = nuevo_precio
                return True

    return False


def eliminar_pelicula(codigo, peliculas, cartelera):

    if buscar_codigo(codigo, peliculas):

        codigo = codigo.upper()

        codigo_real = ""
        for cod in peliculas:
            if cod.upper() == codigo:
                codigo_real = cod
                break

        del peliculas[codigo_real]
        del cartelera[codigo_real]

        return True

    return False


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):

    if buscar_codigo(codigo, peliculas):
        return False

    peliculas[codigo] = [titulo, genero, duracion, clasificacion, idioma, es_3d]
    cartelera[codigo] = [precio, cupos]
    return True


#VALIDArciones

def validar_codigo(codigo, peliculas):
    if codigo.strip() == "":
        return False
    
    if buscar_codigo(codigo, peliculas):
        return False
    return True



def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_duracion(duracion):
    return duracion > 0

def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ["A", "B","C"]

def validar_idioma(idioma):
    return idioma.strip() != ""

def validar_3d(valor):
    return valor.lower() in ["s","n"]

def validar_precio(precio):
    return precio > 0

def validar_cupos(cupos):
    return cupos >= 0


#diccionareios al incicio del program a
peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12], 
    'P105': [8990, 8],
    'P106': [7490, 3]
}

while True:

    print("\n========== MENÚ PRINCIPAL ==========\n")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")

    opcion = leer_opcion()

#1

    if opcion == 1:

        genero = input("Ingrese género a consultar")
        cupos_genero(genero,peliculas,cartelera)

#opcion2

    elif opcion == 2:

        while True:
            try:
                p_min = int(input("Ingrese precio mín"))
                p_max = int(input("Ingrese precio máx"))

                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    break
                else:
                    print("Debe ingresar valores enteros")

            except:
                print("Los numeros deben ser enteros")

        busqueda_precio(p_min,p_max,peliculas,cartelera)

    #3
    elif opcion == 3:

        while True:

            codigo = input("Ingrese codigo de pelicula")
#hasta aqui funviona 
            while True:
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio"))

                    if nuevo_precio > 0:
                        break
                    else:
                        print("Precio invalido")
                except:
                    print("Precio invalido")

            if actualizar_precio(codigo,nuevo_precio,peliculas,cartelera):
                print("Actualizado con éxito")
            else:
                print("El codigo ingresado no es incorrecto")

            seguir = input("¿Desea actualizar otro precio (s/n)? ")

            if seguir == "n":
                break

  







#los not llevaban continuhe
  #Nro 4
    elif opcion == 4:

        codigo = input("Ingrese codigo de pelicula")

        if not validar_codigo(codigo, peliculas):
            print("Código invalido o ya existe")
            continue

        titulo = input("Ingrese título")

        if not validar_titulo(titulo):
            print("Titulo inalido")
            continue

        genero = input("Ingrese genero ")

        if not validar_genero(genero):
            print("Genero invalido")
            continue

        try:
            duracion = int(input("Ingrese duración: "))
        except:
            print("Duración inválida")
            continue

        if not validar_duracion(duracion):
            print("Duración invalida")
            continue

        clasificacion = input("Ingrese clasificación: ").upper()

        if not validar_clasificacion(clasificacion):
            print("Clasificación invalida")
            continue

        idioma = input("Ingrese idioma: ")

        if not validar_idioma(idioma):
            print("Idioma invalido")
            continue

        es3d = input("¿Es 3D?").lower()

        if not validar_3d(es3d):
            print("Valor inválido para 3D")
            continue

        es3d = True if es3d == "s" else False

        try:
            precio = int(input("Ingrese precio: "))
        except:
            print("Precio inválido")
            continue

        if not validar_precio(precio):
            print("Precio invalido")
            continue

        try:
            cupos = int(input("Ingrese cupos: "))
        except:
            print("Cupos inválidos")
            continue

        if not validar_cupos(cupos):
            print("Cupos invalidos")
            continue

        if agregar_pelicula(codigo, titulo,genero,duracion, clasificacion, idioma,es3d, precio,cupos, peliculas,cartelera):

            print("Pelicula agregada")

        else:
            print("El ya esta registrado")

        #5
    elif opcion == 5:

        codigo = input("Ingrese codigo de pelicula")

        if eliminar_pelicula(codigo, peliculas, cartelera):
            print("Eliminada")
        else: 
            print("El codigo no existe, reintente")

#salida
    elif opcion == 6:
        print("Saliendo")
        break
